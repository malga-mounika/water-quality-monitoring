def calculate_wqi(ph: float, turbidity_ntu: float) -> float:
    """
    Calculate a prototype Water Quality Index (WQI)
    using pH and turbidity.

    This is a simplified project-level WQI and should
    not be treated as a complete drinking-water safety index.
    """

    # pH quality score
    if 6.5 <= ph <= 8.5:
        ph_score = 100
    elif 5.5 <= ph < 6.5 or 8.5 < ph <= 9.5:
        ph_score = 70
    elif 4.5 <= ph < 5.5 or 9.5 < ph <= 10.5:
        ph_score = 40
    else:
        ph_score = 20

    # Turbidity quality score
    if turbidity_ntu <= 1:
        turbidity_score = 100
    elif turbidity_ntu <= 5:
        turbidity_score = 80
    elif turbidity_ntu <= 10:
        turbidity_score = 60
    elif turbidity_ntu <= 20:
        turbidity_score = 40
    else:
        turbidity_score = 20

    # Equal weighting for the two available parameters
    wqi = (ph_score + turbidity_score) / 2

    return round(wqi, 2)


def get_quality_status(wqi: float) -> str:
    """
    Convert WQI score into a simple quality status.
    """

    if wqi >= 80:
        return "Good"
    elif wqi >= 50:
        return "Moderate"
    else:
        return "Poor"