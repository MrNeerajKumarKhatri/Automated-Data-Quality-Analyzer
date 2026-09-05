from pathlib import Path
import pandas as pd
import argparse
from profiler import profile_dataset
from missing_values import analyze_missing_values
from duplicates import analyze_duplicates
from statistics_analysis import numerical_statistics
from categorical import analyze_categorical
from outliers import analyze_outliers
from validation import validate_values
from correlation import analyze_correlation
from visualization import visualize_numerical_distributions, box_plot, visualize_categorical_data, visualize_correlation_heatmap
from quality_score import calculate_quality_score
from report import generate_html_report


BASE_DIR = Path(__file__).resolve().parent.parent

parser = argparse.ArgumentParser(description="Data Quality & EDA Tool")
parser.add_argument("csv_file", help="Path to the CSV file")
args = parser.parse_args()

csv_path = Path(args.csv_file)

if not csv_path.exists():
    print(f"Error: File not found: {csv_path}")
    exit(1)

reports_dir = BASE_DIR / "reports"
reports_dir.mkdir(exist_ok=True)

for graph in reports_dir.glob("*.png"):
    graph.unlink()


try:
    df = pd.read_csv(csv_path)
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
    exit(1)
except pd.errors.ParserError:
    print("Error: Unable to parse the CSV file.")
    exit(1)
except UnicodeDecodeError:
    print("Error: Unable to decode the CSV file. Check its encoding.")
    exit(1)
except Exception as e:
    print(f"Error while reading CSV: {e}")
    exit(1)

profile_dataset(df)
analyze_missing_values(df)
analyze_duplicates(df)
numerical_statistics(df)
analyze_categorical(df)
analyze_outliers(df)
validate_values(df)
analyze_correlation(df)
visualize_numerical_distributions(df)
box_plot(df)
visualize_categorical_data(df)
visualize_correlation_heatmap(df)
quality_results = calculate_quality_score(df)
generate_html_report(df, quality_results)
