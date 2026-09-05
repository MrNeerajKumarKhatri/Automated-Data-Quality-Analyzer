def calculate_quality_score(df):
    score = 100

    # Missing values
    missing = df.isnull().sum()
    total_missing = missing.sum()
    missing_penalty = total_missing * 2
    score -= missing_penalty

    # Duplicate rows
    duplicate = df.duplicated()
    duplicate_count = duplicate.sum()
    duplicate_penalty = duplicate_count * 3
    score -= duplicate_penalty

    # Suspicious negative values
    numeric_columns = df.select_dtypes(include="number").columns

    suspicious_count = 0

    for column in numeric_columns:
        data = df[column].dropna()
        negative_values = data[data < 0]
        suspicious_count += len(negative_values)

    suspicious_penalty = suspicious_count * 4
    score -= suspicious_penalty

    # Outliers
    outlier_count = 0

    for column in numeric_columns:
        data = df[column].dropna()

        if len(data) < 4:
            continue

        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = data[
            (data < lower_bound) |
            (data > upper_bound)
        ]

        outlier_count += len(outliers)

    outlier_penalty = outlier_count
    score -= outlier_penalty

    # Prevent score from going below zero
    score = max(score, 0)

    print("\n--- Data Quality Score ---")
    print("Starting Score: 100")

    print(f"\nMissing Values: {total_missing}")
    print(f"Missing Value Penalty: -{missing_penalty}")

    print(f"\nDuplicate Rows: {duplicate_count}")
    print(f"Duplicate Penalty: -{duplicate_penalty}")

    print(f"\nSuspicious Negative Values: {suspicious_count}")
    print(f"Suspicious Value Penalty: -{suspicious_penalty}")

    print(f"\nPotential Outliers: {outlier_count}")
    print(f"Outlier Penalty: -{outlier_penalty}")

    print(f"\nOverall Quality Score: {score}/100")

    return {
        "score": score,
        "missing_values": total_missing,
        "missing_penalty": missing_penalty,
        "duplicate_rows": duplicate_count,
        "duplicate_penalty": duplicate_penalty,
        "suspicious_values": suspicious_count,
        "suspicious_penalty": suspicious_penalty,
        "outliers": outlier_count,
        "outlier_penalty": outlier_penalty
    }