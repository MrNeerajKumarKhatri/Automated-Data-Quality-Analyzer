import pandas as pd

from src.duplicates import analyze_duplicates


def test_duplicates():

    df = pd.DataFrame({
        "Name": ["Vishal", "Sara", "Vishal"],
        "Age": [20, 25, 20]
    })

    result = analyze_duplicates(df)

    assert result == 1