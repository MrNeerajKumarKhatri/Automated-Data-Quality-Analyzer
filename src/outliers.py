def analyze_outliers(df):
    print("\n--- Outlier Analysis ---")

    df_numeric = df.select_dtypes(include="number")
    outlier_results = {}

    for column in df_numeric.columns:

        data = df_numeric[column].dropna()

        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outlier_l = df_numeric[df_numeric[column] < lower_bound]
        outlier_u = df_numeric[df_numeric[column] > upper_bound]

        outliers = (
            outlier_l[column].tolist()
            + outlier_u[column].tolist()
        )

        outlier_results[column] = outliers

        print(f"\n{column}:")

        if not outliers:
            print("No potential outliers detected.")
        else:
            print(f"Potential outliers → {outliers}")

    return outlier_results