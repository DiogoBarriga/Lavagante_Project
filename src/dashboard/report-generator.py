# Report Generator for Project Management Metrics

import pandas as pd
import matplotlib.pyplot as plt
import os

class ReportGenerator:
    def __init__(self, metrics_data_path, output_path):
        self.metrics_data_path = metrics_data_path
        self.output_path = output_path

    def load_metrics_data(self):
        """Load metrics data from a CSV file."""
        if os.path.exists(self.metrics_data_path):
            return pd.read_csv(self.metrics_data_path)
        else:
            raise FileNotFoundError(f"Metrics data file not found: {self.metrics_data_path}")

    def generate_summary_report(self, metrics_df):
        """Generate a summary report of the metrics."""
        summary = {
            'Total Tasks': metrics_df['tasks'].count(),
            'Completed Tasks': metrics_df[metrics_df['status'] == 'completed']['tasks'].count(),
            'Pending Tasks': metrics_df[metrics_df['status'] == 'pending']['tasks'].count(),
            'Average Completion Time': metrics_df['completion_time'].mean()
        }
        return summary

    def visualize_metrics(self, metrics_df):
        """Create visualizations for the metrics."""
        plt.figure(figsize=(10, 6))
        metrics_df['status'].value_counts().plot(kind='bar', color='skyblue')
        plt.title('Task Status Distribution')
        plt.xlabel('Status')
        plt.ylabel('Number of Tasks')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_path, 'task_status_distribution.png'))
        plt.close()

    def save_report(self, summary):
        """Save the summary report to a text file."""
        report_file = os.path.join(self.output_path, 'summary_report.txt')
        with open(report_file, 'w') as f:
            for key, value in summary.items():
                f.write(f"{key}: {value}\n")
        print(f"Summary report saved to: {report_file}")

    def run(self):
        """Run the report generation process."""
        metrics_df = self.load_metrics_data()
        summary = self.generate_summary_report(metrics_df)
        self.visualize_metrics(metrics_df)
        self.save_report(summary)

if __name__ == "__main__":
    metrics_data_path = 'path/to/metrics_data.csv'  # Update with actual path
    output_path = 'path/to/output'  # Update with actual output path
    report_generator = ReportGenerator(metrics_data_path, output_path)
    report_generator.run()