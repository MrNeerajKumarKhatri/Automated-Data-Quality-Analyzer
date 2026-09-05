def analyze_missing_values(df):
    print("\n--- Missing Values Analysis ---")

    missing = df.isnull().sum()
    print(missing)

    total_missing = missing.sum()
    print("\nTotal missing values:", total_missing)

    print("\nColumns with missing values:")

    for column, count in missing.items():
        if count > 0:
            percentage = (count / len(df)) * 100
            print(f"{column} → {count} missing ({percentage:.2f}%)")

    return missing