import pandas as pd

from src.quality_score import calculate_quality_score


def test_clean_dataset():

    df = pd.DataFrame({
        "Age": [20, 25, 30],
        "Salary": [50000, 60000, 70000]
    })

    result = calculate_quality_score(df)

    assert result["score"] == 100