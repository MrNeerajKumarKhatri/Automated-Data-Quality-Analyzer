# Automated Data Quality Analyzer

A modular Python tool for automated dataset profiling, data-quality analysis, statistical exploration, visualization, and HTML report generation.

The project is designed to automate the initial analysis of CSV datasets and identify common data-quality problems before the data is used for further analysis or machine learning workflows.

---

## Overview

Real-world datasets frequently contain issues such as missing values, duplicate records, suspicious values, statistical outliers, and inconsistent distributions.

Manually identifying these issues for every dataset can be repetitive and time-consuming.

**Automated Data Quality Analyzer** provides a reusable analysis pipeline that takes a CSV dataset as input and automatically performs a series of data-quality and exploratory-analysis checks.

The tool produces both:

* Console-based analysis results
* Automatically generated visualizations
* An HTML data-quality report

The project is organized into independent Python modules so that individual analysis components can be tested, maintained, and extended independently.

---

## Key Features

### Dataset Profiling

Automatically provides an overview of the dataset, including:

* Number of rows
* Number of columns
* Column names
* Data types
* First five records
* Pandas dataset information

### Missing Value Analysis

Detects missing values and reports:

* Missing values per column
* Total number of missing values
* Percentage of missing values for affected columns

### Duplicate Detection

Identifies completely duplicated rows and reports the total number of duplicate records.

### Suspicious Value Detection

Checks numerical columns for negative values that may require investigation.

Negative values are classified as **suspicious rather than automatically invalid**, because whether a negative value is valid depends on the meaning of the dataset.

For example:

* Negative temperature can be valid
* Negative age is usually suspicious
* Negative salary may require investigation

### Outlier Detection

Potential statistical outliers are detected using the **Interquartile Range (IQR)** method.

For each numerical feature:

1. Calculate Q1
2. Calculate Q3
3. Calculate IQR
4. Calculate lower and upper bounds
5. Identify observations outside those bounds

The method is useful for detecting unusually large or small observations that may deserve further investigation.

### Numerical Statistical Analysis

The analyzer generates descriptive statistics for numerical columns, including:

* Count
* Mean
* Standard deviation
* Minimum
* 25th percentile
* Median
* 75th percentile
* Maximum

### Categorical Analysis

Categorical columns are analyzed using value-frequency counts.

This provides an overview of the distribution of categorical values within the dataset.

### Correlation Analysis

The tool calculates Pearson correlation coefficients between numerical variables.

This helps identify potential linear relationships between numerical features.

Correlation is used for exploratory analysis and should not be interpreted as evidence of causation.

### Automated Visualization

The analyzer automatically generates:

* Histograms for numerical features
* Box plots for numerical data
* Categorical distribution charts
* Correlation heatmaps

All generated visualizations are saved automatically in the `reports/` directory.

### Automated Data Quality Score

The project calculates a simple **heuristic data-quality score** beginning at 100.

Penalties are applied according to detected issues.

| Detected Issue            | Penalty |
| ------------------------- | ------: |
| Missing value             |      -2 |
| Duplicate row             |      -3 |
| Suspicious negative value |      -4 |
| Potential outlier         |      -1 |

The final score is constrained to a minimum of `0`.

For example, a dataset containing:

* 2 missing values
* 0 duplicate rows
* 1 suspicious value
* 2 potential outliers

receives:

```text
100 - (2 × 2) - (0 × 3) - (1 × 4) - (2 × 1)

= 100 - 4 - 0 - 4 - 2

= 90/100
```

### Important Note About the Score

The score is a **project-defined heuristic**, not an industry-standard or statistically validated data-quality metric.

Different datasets and domains may require different definitions of data quality.

The scoring system is intentionally simple so that it can be extended later with configurable rules and domain-specific validation.

### HTML Report Generation

After the analysis completes, the tool automatically generates an HTML report containing:

* Dataset overview
* Overall data-quality score
* Quality breakdown
* Missing-value information
* Duplicate information
* Suspicious-value information
* Outlier information
* Generated visualizations

The report is generated automatically inside the `reports/` directory.

---

# Analysis Pipeline

The complete processing workflow is:

```text
                    CSV Dataset
                         │
                         ▼
                Dataset Profiling
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Missing Values  Duplicates   Suspicious Values
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
                  Outlier Detection
                         │
                         ▼
               Statistical Analysis
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Categorical Analysis   Correlation Analysis
              │                     │
              └──────────┬──────────┘
                         ▼
                  Visualization
                         │
                         ▼
                  Quality Scoring
                         │
                         ▼
                   HTML Report
```

---

# Project Architecture

The project follows a modular architecture where each component performs a specific responsibility.

```text
Automated-Data-Quality-Analyzer/
│
├── data/
│   ├── sample.csv
│   ├── sample2.csv
│   ├── sample3.csv
│   ├── sample4.csv
│   └── messy_dataset.csv
│
├── reports/
│   └── Generated reports and visualizations
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── profiler.py
│   ├── missing_values.py
│   ├── duplicates.py
│   ├── statistics_analysis.py
│   ├── categorical.py
│   ├── outliers.py
│   ├── validation.py
│   ├── correlation.py
│   ├── visualization.py
│   ├── quality_score.py
│   └── report.py
│
├── tests/
│   ├── test_missing_values.py
│   ├── test_duplicates.py
│   ├── test_outliers.py
│   ├── test_quality_score.py
│   └── test_validation.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

# Module Responsibilities

| Module                   | Responsibility                             |
| ------------------------ | ------------------------------------------ |
| `main.py`                | Coordinates the complete analysis pipeline |
| `profiler.py`            | Dataset structure and overview             |
| `missing_values.py`      | Missing-value detection                    |
| `duplicates.py`          | Duplicate-row detection                    |
| `statistics_analysis.py` | Numerical descriptive statistics           |
| `categorical.py`         | Categorical-value frequency analysis       |
| `outliers.py`            | IQR-based outlier detection                |
| `validation.py`          | Suspicious numerical-value detection       |
| `correlation.py`         | Numerical correlation analysis             |
| `visualization.py`       | Automated chart generation                 |
| `quality_score.py`       | Heuristic quality-score calculation        |
| `report.py`              | HTML report generation                     |

This separation keeps the project modular and makes individual components easier to test and extend.

---

# Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas

### Visualization

* Matplotlib

### Testing

* Pytest

### Development Tools

* Git
* GitHub
* Virtual environments

### Reporting

* HTML
* CSS

---

# Requirements

The project currently requires:

```text
pandas
matplotlib
pytest
```

Python 3.9+ is recommended.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MrNeerajKumarKhatri/Automated-Data-Quality-Analyzer.git
```

Move into the project directory:

```bash
cd Automated-Data-Quality-Analyzer
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

The analyzer accepts a CSV file as a command-line argument.

For example:

```bash
python src/main.py data/messy_dataset.csv
```

The program then performs the complete analysis pipeline.

The generated visualizations and HTML report are saved to:

```text
reports/
```

---

# Example Dataset

The repository includes several sample datasets for testing.

The main demonstration dataset is:

```text
data/messy_dataset.csv
```

This dataset intentionally contains several data-quality problems so that the analyzer's detection capabilities can be demonstrated.

Example issues include:

* Missing values
* Suspicious negative value
* Extremely large numerical value
* Potential statistical outliers

---

# Example Results

Running:

```bash
python src/main.py data/messy_dataset.csv
```

produces results similar to:

```text
--- Missing Values Analysis ---

Total missing values: 2
```

```text
--- Duplicate Analysis ---

Total duplicate rows: 0
```

```text
--- Suspicious Value Analysis ---

Age:
Negative values → [-5]
```

```text
--- Data Quality Score ---

Starting Score: 100

Missing Values: 2
Missing Value Penalty: -4

Duplicate Rows: 0
Duplicate Penalty: -0

Suspicious Negative Values: 1
Suspicious Value Penalty: -4

Potential Outliers: 2
Outlier Penalty: -2

Overall Quality Score: 90/100
```

The program also generates an HTML report and visualization files.

---

# Generated Visualizations

Depending on the dataset, the analyzer can generate:

### Histograms

Used to inspect the distribution of numerical variables.

Example:

```text
histogram_Age.png
histogram_Salary.png
histogram_Rating.png
```

### Box Plot

Used to visually identify potential outliers.

```text
box_plot.png
```

### Categorical Distribution

Used to visualize the frequency of categorical values.

```text
categorical_City.png
```

### Correlation Heatmap

Used to visualize relationships between numerical variables.

```text
correlation_heatmap.png
```

---

# HTML Report

The generated report provides a consolidated view of the analysis.

It includes:

```text
Dataset Overview
       │
       ▼
Data Quality Score
       │
       ▼
Quality Breakdown
       │
       ├── Missing Values
       ├── Duplicate Rows
       ├── Suspicious Values
       └── Potential Outliers
       │
       ▼
Visual Analysis
```

The report can be opened using a web browser after running the analyzer.

---

# Testing

The project uses **Pytest** for automated unit testing.

Run the complete test suite:

```bash
pytest
```

The tests currently cover:

* Missing-value detection
* Duplicate-row detection
* Outlier detection
* Quality-score calculation
* Suspicious-value detection

The tests use small controlled datasets to verify the behavior of individual analysis modules.

---

# Example Test

The outlier detector is tested using a dataset containing an intentionally extreme age value.

Conceptually:

```text
Age
20
21
22
23
24
100
```

The test verifies that `100` is identified as a potential outlier.

---

# Design Principles

The project follows several software-engineering principles.

## Modularity

Each analysis task is implemented as a separate module.

This avoids putting the entire application into a single large Python file.

## Separation of Responsibilities

Different components are responsible for:

* Analysis
* Visualization
* Scoring
* Reporting
* Testing

## Reusability

The analyzer accepts arbitrary CSV files rather than being designed around only one dataset.

## Testability

Individual analysis functions return results that can be tested independently.

## Automation

The complete workflow can be executed using a single command:

```bash
python src/main.py <dataset.csv>
```

---

# Limitations

The current implementation is designed as an automated **initial data-quality and exploratory-analysis tool** rather than a complete data-cleaning framework.

Some limitations include:

### Heuristic Suspicious-Value Detection

The current implementation flags negative numerical values.

However, negative values are not inherently incorrect.

For example:

```text
Temperature = -5
```

may be completely valid, while:

```text
Age = -5
```

would usually require investigation.

### Heuristic Quality Score

The current scoring system uses fixed penalties.

These penalties are useful for demonstrating the concept but are not universally applicable to every dataset.

### CSV Input

The current command-line workflow focuses on CSV datasets.

### Limited Validation Rules

The current version does not yet automatically understand the semantic meaning of every column.

For example, it cannot automatically determine that:

```text
Age
```

should normally fall within a particular domain-specific range.

---

# Future Improvements

The project can be extended in several directions.

## Configurable Quality Rules

Allow users to define custom penalties and validation rules.

For example:

```text
Age:
minimum = 0
maximum = 120
```

## Advanced Data Validation

Add checks for:

* Invalid ranges
* Unexpected data types
* Impossible dates
* Invalid categorical values
* Inconsistent formatting

## Automatic Data Cleaning Suggestions

Instead of only detecting problems, the system could suggest possible solutions.

Examples:

```text
Missing values detected in Salary.

Possible actions:
- Median imputation
- Mean imputation
- Remove affected rows
```

## JSON Reporting

Add machine-readable reports for integration with other software systems.

## Command-Line Configuration

Allow users to configure analysis behavior directly from the command line.

Example:

```bash
python src/main.py dataset.csv --score-config config.json
```

## Additional File Formats

Potential support for:

* Excel
* JSON
* Parquet

## Interactive Dashboard

A future version could provide an interactive dashboard for exploring dataset quality.

## Expanded Test Coverage

Increase automated test coverage for edge cases and unusual datasets.

## Data Quality Configuration

Allow quality rules to be customized according to different domains such as:

* Finance
* Healthcare
* Retail
* Scientific research
* Machine learning datasets

---

# Project Goals

This project was developed to gain practical experience with:

* Python programming
* Pandas
* Data analysis
* Statistical analysis
* Data visualization
* Data-quality engineering
* Modular software architecture
* Automated testing
* Command-line applications
* HTML report generation
* Git and GitHub
* Reproducible analysis workflows

---

# Why This Project?

Data preparation is an important part of real-world data science and machine learning workflows.

Before training a model or performing statistical analysis, understanding the structure and quality of the underlying dataset is essential.

This project focuses on automating that initial inspection process and demonstrates how individual data-analysis operations can be combined into a reusable software pipeline.

---

# Current Status

**Status: Functional**

The current version supports:

* CSV dataset input
* Dataset profiling
* Missing-value detection
* Duplicate detection
* Suspicious-value detection
* IQR-based outlier detection
* Numerical statistics
* Categorical analysis
* Correlation analysis
* Automated visualization
* Heuristic quality scoring
* HTML report generation
* Automated unit testing

---

# Author

**Neeraj Kumar**

Computer Science Undergraduate

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Analysis
* Software Engineering
* Research

---

# License

This project is currently intended as an educational and portfolio project.
