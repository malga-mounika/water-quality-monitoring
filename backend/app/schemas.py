from pydantic import BaseModel, Field


class WaterReadingCreate(BaseModel):
    device_id: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # Core sensor readings - required
    ph: float = Field(
        ...,
        ge=0,
        le=14
    )

    turbidity_ntu: float = Field(
        ...,
        ge=0
    )

    # GPS readings - optional when GPS has no satellite fix
    latitude: float | None = Field(
        default=None,
        ge=-90,
        le=90
    )

    longitude: float | None = Field(
        default=None,
        ge=-180,
        le=180
    )