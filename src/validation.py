def validate_values(df):
    print("\n--- Suspicious Value Analysis ---")

    numeric_columns = df.select_dtypes(include="number").columns
    suspicious_results = {}

    if len(numeric_columns) == 0:
        print("No numeric columns found.")
        return suspicious_results

    for column in numeric_columns:
        data = df[column].dropna()
        suspicious = data[data < 0]

        suspicious_results[column] = suspicious.tolist()

        print(f"\n{column}:")

        if suspicious.empty:
            print("No negative values detected.")
        else:
            print(f"Negative values → {suspicious.tolist()}")

    return suspicious_results