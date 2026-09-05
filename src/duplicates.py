def analyze_duplicates(df):
    print("\n--- Duplicate Analysis ---")

    duplicate = df.duplicated()
    duplicate_count = duplicate.sum()

    print("Total duplicate rows:", duplicate_count)

    print("\nDuplicate rows:")
    print(df[duplicate])
    return duplicate_count