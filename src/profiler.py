def profile_dataset(df):
    print("\n--- Dataset Overview ---")

    print("\nFirst 5 rows:")
    print(df.head(5))

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nDataset Information:")
    df.info()

    print("\nData Types:")
    print(df.dtypes)