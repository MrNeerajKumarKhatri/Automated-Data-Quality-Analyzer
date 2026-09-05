def analyze_categorical(df):
    print("\n--- Categorical Analysis ---")

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in categorical_columns:
        print(f"\n{column}:")
        print(df[column].value_counts())