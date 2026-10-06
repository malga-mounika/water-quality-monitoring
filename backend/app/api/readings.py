from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import WaterReading
from app.schemas import WaterReadingCreate
from app.services.wqi import calculate_wqi, get_quality_status
from app.services.condition import analyze_combined


router = APIRouter(
    prefix="/api/readings",
    tags=["Readings"]
)


@router.post("/")
def create_reading(
    reading: WaterReadingCreate,
    db: Session = Depends(get_db)
):
    # --------------------------------------------------
    # 1. Calculate WQI
    # --------------------------------------------------
    wqi_score = calculate_wqi(
        reading.ph,
        reading.turbidity_ntu
    )

    # --------------------------------------------------
    # 2. Determine overall quality status
    # --------------------------------------------------
    quality_status = get_quality_status(wqi_score)

    # --------------------------------------------------
    # 3. Analyze pH + turbidity together
    # --------------------------------------------------
    contamination = analyze_combined(
        reading.ph,
        reading.turbidity_ntu
    )

    # --------------------------------------------------
    # 4. Save reading to database
    # --------------------------------------------------
    water_reading = WaterReading(
        device_id=reading.device_id,
        ph=reading.ph,
        turbidity_ntu=reading.turbidity_ntu,
        latitude=reading.latitude,
        longitude=reading.longitude,
        wqi_score=wqi_score,
        quality_status=quality_status,
        detected_contaminants=[
            {
                "diagnosis": contamination["diagnosis"],
                "likely_cause": contamination["likely_cause"]
            }
        ],
        ai_recommendation=contamination["recommendation"]
    )

    db.add(water_reading)
    db.commit()
    db.refresh(water_reading)

    # --------------------------------------------------
    # 5. Return complete result
    # --------------------------------------------------
    return {
        "message": "Water reading saved successfully",
        "data": {
            "id": water_reading.id,
            "device_id": water_reading.device_id,
            "ph": water_reading.ph,
            "turbidity_ntu": water_reading.turbidity_ntu,
            "latitude": water_reading.latitude,
            "longitude": water_reading.longitude,
            "wqi_score": water_reading.wqi_score,
            "quality_status": water_reading.quality_status,
            "detected_contaminants": water_reading.detected_contaminants,
            "ai_recommendation": water_reading.ai_recommendation,
            "timestamp": water_reading.timestamp
        }
    }


@router.get("/send")
def send_reading(
    device_id: str = Query(..., min_length=1, max_length=100),
    ph: float = Query(..., ge=0, le=14),
    turbidity_ntu: float = Query(..., ge=0),
    latitude: float | None = Query(default=None, ge=-90, le=90),
    longitude: float | None = Query(default=None, ge=-180, le=180),
    db: Session = Depends(get_db)
):
    # --------------------------------------------------
    # 1. Calculate WQI
    # --------------------------------------------------
    wqi_score = calculate_wqi(
        ph,
        turbidity_ntu
    )

    # --------------------------------------------------
    # 2. Determine overall quality status
    # --------------------------------------------------
    quality_status = get_quality_status(wqi_score)

    # --------------------------------------------------
    # 3. Analyze pH + turbidity together
    # --------------------------------------------------
    contamination = analyze_combined(
        ph,
        turbidity_ntu
    )

    # --------------------------------------------------
    # 4. Save reading to database
    # --------------------------------------------------
    water_reading = WaterReading(
        device_id=device_id,
        ph=ph,
        turbidity_ntu=turbidity_ntu,
        latitude=latitude,
        longitude=longitude,
        wqi_score=wqi_score,
        quality_status=quality_status,
        detected_contaminants=[
            {
                "diagnosis": contamination["diagnosis"],
                "likely_cause": contamination["likely_cause"]
            }
        ],
        ai_recommendation=contamination["recommendation"]
    )

    db.add(water_reading)
    db.commit()
    db.refresh(water_reading)

    # --------------------------------------------------
    # 5. Return complete result
    # --------------------------------------------------
    return {
        "message": "Water reading received successfully",
        "data": {
            "id": water_reading.id,
            "device_id": water_reading.device_id,
            "ph": water_reading.ph,
            "turbidity_ntu": water_reading.turbidity_ntu,
            "latitude": water_reading.latitude,
            "longitude": water_reading.longitude,
            "wqi_score": water_reading.wqi_score,
            "quality_status": water_reading.quality_status,
            "detected_contaminants": water_reading.detected_contaminants,
            "ai_recommendation": water_reading.ai_recommendation,
            "timestamp": water_reading.timestamp
        }
    }


@router.get("/latest")
def get_latest_reading(
    db: Session = Depends(get_db)
):
    latest = (
        db.query(WaterReading)
        .order_by(WaterReading.timestamp.desc())
        .first()
    )

    if latest is None:
        return {
            "message": "No readings found",
            "data": None
        }

    return {
        "message": "Latest water reading",
        "data": {
            "id": latest.id,
            "device_id": latest.device_id,
            "ph": latest.ph,
            "turbidity_ntu": latest.turbidity_ntu,
            "latitude": latest.latitude,
            "longitude": latest.longitude,
            "wqi_score": latest.wqi_score,
            "quality_status": latest.quality_status,
            "detected_contaminants": latest.detected_contaminants,
            "ai_recommendation": latest.ai_recommendation,
            "timestamp": latest.timestamp
        }
    }


@router.get("/")
def get_readings(
    db: Session = Depends(get_db)
):
    readings = (
        db.query(WaterReading)
        .order_by(WaterReading.timestamp.desc())
        .all()
    )

    return {
        "message": "Water readings retrieved successfully",
        "count": len(readings),
        "data": [
            {
                "id": reading.id,
                "device_id": reading.device_id,
                "ph": reading.ph,
                "turbidity_ntu": reading.turbidity_ntu,
                "latitude": reading.latitude,
                "longitude": reading.longitude,
                "wqi_score": reading.wqi_score,
                "quality_status": reading.quality_status,
                "detected_contaminants": reading.detected_contaminants,
                "ai_recommendation": reading.ai_recommendation,
                "timestamp": reading.timestamp
            }
            for reading in readings
        ]
    }


@router.get("/history")
def get_reading_history(
    limit: int = 50,
    db: Session = Depends(get_db)
):
    readings = (
        db.query(WaterReading)
        .order_by(WaterReading.timestamp.desc())
        .limit(limit)
        .all()
    )

    return {
        "message": "Reading history retrieved successfully",
        "count": len(readings),
        "data": [
            {
                "id": reading.id,
                "device_id": reading.device_id,
                "ph": reading.ph,
                "turbidity_ntu": reading.turbidity_ntu,
                "latitude": reading.latitude,
                "longitude": reading.longitude,
                "wqi_score": reading.wqi_score,
                "quality_status": reading.quality_status,
                "detected_contaminants": reading.detected_contaminants,
                "ai_recommendation": reading.ai_recommendation,
                "timestamp": reading.timestamp
            }
            for reading in readings
        ]
    }