from app.services.condition import analyze_combined


tests = [
    (6.0, 15),
    (7.2, 15),
    (6.0, 3),
    (9.0, 15),
    (9.0, 3),
    (7.2, 3),
]


for ph, turbidity in tests:
    result = analyze_combined(ph, turbidity)

    print("\n----------------------------")
    print(f"pH: {ph}")
    print(f"Turbidity: {turbidity} NTU")
    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Possible cause: {result['likely_cause']}")
    print(f"Recommendation: {result['recommendation']}")