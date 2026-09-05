import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)


def visualize_numerical_distributions(df):
    df_numeric = df.select_dtypes(include="number")

    if df_numeric.empty:
        print("No numeric columns found for histograms.")
        return

    for column in df_numeric.columns:
        plt.hist(df_numeric[column].dropna(), bins="auto")
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(REPORTS_DIR / f"histogram_{column}.png")
        plt.close()


def box_plot(df):
    df_numeric = df.select_dtypes(include="number")

    if df_numeric.empty:
        print("No numeric columns found for box plot.")
        return

    plt.boxplot(df_numeric.dropna())
    plt.title("Box Plot of Numeric Features")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "box_plot.png")
    plt.close()


def visualize_categorical_data(df):
    categorical_columns = df.select_dtypes(
        include=["object", "category", "string"]
    ).columns

    if len(categorical_columns) == 0:
        print("No categorical columns found.")
        return

    for column in categorical_columns:
        unique_values = df[column].value_counts()

        plt.bar(unique_values.index.astype(str), unique_values.values)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(REPORTS_DIR / f"categorical_{column}.png")
        plt.close()


def visualize_correlation_heatmap(df):
    df_numeric = df.select_dtypes(include="number")

    if df_numeric.shape[1] < 2:
        print("At least two numeric columns are required for correlation heatmap.")
        return

    correlation = df_numeric.corr()

    plt.imshow(correlation)
    plt.xticks(
        range(len(df_numeric.columns)),
        df_numeric.columns,
        rotation=45
    )
    plt.yticks(
        range(len(df_numeric.columns)),
        df_numeric.columns
    )
    plt.title("Correlation Heatmap of Numeric Features")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "correlation_heatmap.png")
    plt.close()