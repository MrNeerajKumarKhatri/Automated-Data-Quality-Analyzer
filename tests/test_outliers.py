import pandas as pd

from src.outliers import analyze_outliers


def test_outliers():

    df = pd.DataFrame({
        "Age": [20, 21, 22, 23, 24, 100]
    })

    result = analyze_outliers(df)

    assert 100 in result["Age"]