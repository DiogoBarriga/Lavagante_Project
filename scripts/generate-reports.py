import os
import json
from datetime import datetime

def generate_reports():
    reports_dir = "reports/automated"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Generate daily standup report
    daily_report = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "updates": [
            {"team_member": "Alice", "update": "Completed user authentication feature."},
            {"team_member": "Bob", "update": "Fixed bugs in the payment module."},
            {"team_member": "Charlie", "update": "Started working on the dashboard UI."}
        ]
    }
    with open(os.path.join(reports_dir, "daily-standup.md"), "w") as f:
        f.write("# Daily Standup Report\n")
        f.write(f"**Date:** {daily_report['date']}\n\n")
        for update in daily_report["updates"]:
            f.write(f"- **{update['team_member']}:** {update['update']}\n")

    # Generate sprint summary report
    sprint_summary = {
        "sprint_number": 1,
        "completed_tasks": 10,
        "total_tasks": 15,
        "velocity": 20,
        "retrospective": "The team performed well, but we need to improve our communication."
    }
    with open(os.path.join(reports_dir, "sprint-summary.md"), "w") as f:
        f.write("# Sprint Summary Report\n")
        f.write(f"**Sprint Number:** {sprint_summary['sprint_number']}\n")
        f.write(f"**Completed Tasks:** {sprint_summary['completed_tasks']} / {sprint_summary['total_tasks']}\n")
        f.write(f"**Velocity:** {sprint_summary['velocity']}\n")
        f.write(f"**Retrospective:** {sprint_summary['retrospective']}\n")

    # Generate metrics report
    metrics = {
        "total_commits": 150,
        "open_issues": 5,
        "closed_issues": 20,
        "pull_requests": 10
    }
    with open(os.path.join(reports_dir, "metrics-report.md"), "w") as f:
        f.write("# Metrics Report\n")
        f.write(f"**Total Commits:** {metrics['total_commits']}\n")
        f.write(f"**Open Issues:** {metrics['open_issues']}\n")
        f.write(f"**Closed Issues:** {metrics['closed_issues']}\n")
        f.write(f"**Pull Requests:** {metrics['pull_requests']}\n")

    print("Reports generated successfully.")

if __name__ == "__main__":
    generate_reports()