import pandas as pd
from src.validation import validate_values


def test_validation():
    df = pd.DataFrame({
        "Age": [20, 25, 30],
        "Temperature": [25, -5, 30]
    })

    result = validate_values(df)

    assert result["Age"] == []
    assert result["Temperature"] == [-5]
