def analyze_categorical(df):
    print("\n--- Categorical Analysis ---")

    categorical_columns = df.select_dtypes(
        include=["object", "category", "string"]
    ).columns

    if len(categorical_columns) == 0:
        print("No categorical columns found.")
        return {}

    categorical_results = {}

    for column in categorical_columns:
        print(f"\n{column}:")

        value_counts = df[column].value_counts()

        print(value_counts)

        categorical_results[column] = value_counts

    return categorical_results