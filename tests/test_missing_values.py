import pandas as pd

from src.missing_values import analyze_missing_values


def test_missing_values():

    df = pd.DataFrame({
        "Name": ["Rahul", "Subash", "Vishal"],
        "Age": [20, None, 25]
    })

    result = analyze_missing_values(df)

    assert result["Age"] == 1
    assert result["Name"] == 0