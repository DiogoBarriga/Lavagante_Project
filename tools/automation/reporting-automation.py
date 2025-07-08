import json
import os

def generate_report(data, report_type):
    """
    Generate a report based on the provided data and report type.
    
    Args:
        data (dict): The data to include in the report.
        report_type (str): The type of report to generate (e.g., 'daily', 'sprint', 'metrics').
    
    Returns:
        str: The generated report as a string.
    """
    report = f"--- {report_type.capitalize()} Report ---\n\n"
    for key, value in data.items():
        report += f"{key}: {value}\n"
    return report

def save_report(report, report_name):
    """
    Save the generated report to a file.
    
    Args:
        report (str): The report content to save.
        report_name (str): The name of the report file.
    """
    report_path = os.path.join("reports", "automated", f"{report_name}.md")
    with open(report_path, "w") as file:
        file.write(report)
    print(f"Report saved to {report_path}")

def main():
    # Example data for the report
    report_data = {
        "Date": "2023-10-01",
        "Total Tasks": 15,
        "Completed Tasks": 10,
        "Pending Tasks": 5,
        "Sprint Progress": "67%"
    }
    
    # Generate and save the report
    report = generate_report(report_data, "sprint")
    save_report(report, "sprint-summary")

if __name__ == "__main__":
    main()