def analyze_correlation(df):
    print("\n--- Correlation Analysis ---")

    df_numeric = df.select_dtypes(include="number")

    correlation = df_numeric.corr()

    print(correlation)