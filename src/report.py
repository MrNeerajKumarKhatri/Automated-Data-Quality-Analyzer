from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def generate_html_report(df, quality_results):
    graph_files = sorted(REPORTS_DIR.glob("*.png"))

    graph_html = ""

    for graph in graph_files:
        graph_name = graph.stem.replace("_", " ").title()

        graph_html += f"""
        <div class="graph">
            <h3>{graph_name}</h3>
            <img src="{graph.name}">
        </div>
        """

    score = quality_results["score"]

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">

        <title>Automated Data Quality Report</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f5f5f5;
                color: #333;
            }}

            .container {{
                max-width: 1100px;
                margin: 40px auto;
                background: white;
                padding: 40px;
                border-radius: 10px;
            }}

            h1 {{
                text-align: center;
                margin-bottom: 10px;
            }}

            .subtitle {{
                text-align: center;
                color: #777;
                margin-bottom: 40px;
            }}

            h2 {{
                margin-top: 40px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }}

            .score {{
                text-align: center;
                font-size: 48px;
                font-weight: bold;
                margin: 30px 0;
            }}

            .summary {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 15px;
            }}

            .card {{
                padding: 20px;
                background-color: #eeeeee;
                border-radius: 8px;
            }}

            .card strong {{
                display: block;
                margin-bottom: 8px;
            }}

            .penalty {{
                color: #b00020;
            }}

            .graph {{
                margin-top: 40px;
                text-align: center;
            }}

            .graph img {{
                max-width: 90%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <h1>Automated Data Quality Report</h1>

            <div class="subtitle">
                Automated analysis of dataset quality and structure
            </div>


            <h2>Dataset Overview</h2>

            <div class="summary">

                <div class="card">
                    <strong>Rows</strong>
                    <p>{df.shape[0]}</p>
                </div>

                <div class="card">
                    <strong>Columns</strong>
                    <p>{df.shape[1]}</p>
                </div>

            </div>


            <h2>Overall Data Quality</h2>

            <div class="score">
                {score} / 100
            </div>


            <h2>Quality Breakdown</h2>

            <div class="summary">

                <div class="card">
                    <strong>Missing Values</strong>

                    <p>
                        {quality_results["missing_values"]}
                    </p>

                    <p class="penalty">
                        Penalty: -{quality_results["missing_penalty"]}
                    </p>
                </div>


                <div class="card">
                    <strong>Duplicate Rows</strong>

                    <p>
                        {quality_results["duplicate_rows"]}
                    </p>

                    <p class="penalty">
                        Penalty: -{quality_results["duplicate_penalty"]}
                    </p>
                </div>


                <div class="card">
                    <strong>Suspicious Values</strong>

                    <p>
                        {quality_results["suspicious_values"]}
                    </p>

                    <p class="penalty">
                        Penalty: -{quality_results["suspicious_penalty"]}
                    </p>
                </div>


                <div class="card">
                    <strong>Potential Outliers</strong>

                    <p>
                        {quality_results["outliers"]}
                    </p>

                    <p class="penalty">
                        Penalty: -{quality_results["outlier_penalty"]}
                    </p>
                </div>

            </div>


            <h2>Visual Analysis</h2>

            {graph_html}

        </div>

    </body>

    </html>
    """

    report_path = REPORTS_DIR / "report.html"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"\nHTML report generated: {report_path}")