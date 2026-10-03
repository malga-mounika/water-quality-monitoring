def analyze_combined(ph: float, turbidity: float) -> dict:

    ph_low = ph < 6.5
    ph_high = ph > 8.5
    ph_normal = 6.5 <= ph <= 8.5

    turbidity_high = turbidity > 10
    turbidity_normal = turbidity <= 10

    # Low pH + High Turbidity
    if ph_low and turbidity_high:
        return {
            "diagnosis": "Combined acidic + particulate contamination",
            "likely_cause": (
                "Possible industrial or chemical discharge "
                "mixed with sediment runoff."
            ),
            "recommendation": (
                "Apply coagulation-flocculation to remove suspended "
                "particles, followed by controlled pH neutralization "
                "after appropriate water testing. Single-step "
                "filtration alone will not address both issues."
            )
        }

    # Normal pH + High Turbidity
    elif ph_normal and turbidity_high:
        return {
            "diagnosis": "Particulate contamination with normal pH",
            "likely_cause": (
                "Possible natural sediment from soil erosion, "
                "rainfall runoff, or other suspended material."
            ),
            "recommendation": (
                "Consider sedimentation followed by sand/media "
                "filtration. pH treatment is not required when "
                "the pH is within the configured range."
            )
        }

    # Low pH + Normal Turbidity
    elif ph_low and turbidity_normal:
        return {
            "diagnosis": "Acidic contamination with normal turbidity",
            "likely_cause": (
                "Possible dissolved acidic substances or acidic "
                "input. The specific source requires further testing."
            ),
            "recommendation": (
                "Filtration alone will not correct low pH. "
                "Consider controlled pH neutralization after "
                "appropriate water testing."
            )
        }

    # High pH + High Turbidity
    elif ph_high and turbidity_high:
        return {
            "diagnosis": "Alkaline contamination with particulates",
            "likely_cause": (
                "Possible detergent, alkaline discharge, or other "
                "alkaline input combined with suspended material."
            ),
            "recommendation": (
                "Apply sedimentation/filtration for suspended "
                "particles, combined with controlled pH correction "
                "after appropriate water testing."
            )
        }

    # High pH + Normal Turbidity
    elif ph_high and turbidity_normal:
        return {
            "diagnosis": "Alkaline contamination with normal turbidity",
            "likely_cause": (
                "Possible alkaline input. The specific source "
                "requires further testing."
            ),
            "recommendation": (
                "Consider controlled pH correction after "
                "appropriate water testing."
            )
        }

    # Normal pH + Normal Turbidity
    else:
        return {
            "diagnosis": "No abnormal pH or turbidity contamination detected",
            "likely_cause": None,
            "recommendation": (
                "No pH or turbidity treatment is indicated from "
                "the available measurements. Continue routine monitoring."
            )
        }