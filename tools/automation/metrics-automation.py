import os
import json
import requests

class MetricsAutomation:
    def __init__(self, metrics_endpoint, report_path):
        self.metrics_endpoint = metrics_endpoint
        self.report_path = report_path

    def collect_metrics(self):
        """Collect metrics from the specified endpoint."""
        try:
            response = requests.get(self.metrics_endpoint)
            response.raise_for_status()
            metrics_data = response.json()
            self.save_metrics(metrics_data)
        except requests.exceptions.RequestException as e:
            print(f"Error collecting metrics: {e}")

    def save_metrics(self, metrics_data):
        """Save collected metrics to a report file."""
        with open(self.report_path, 'w') as report_file:
            json.dump(metrics_data, report_file, indent=4)
        print(f"Metrics saved to {self.report_path}")

    def run(self):
        """Run the metrics automation process."""
        self.collect_metrics()

if __name__ == "__main__":
    # Configuration
    METRICS_ENDPOINT = os.getenv("METRICS_ENDPOINT", "http://localhost:5000/metrics")
    REPORT_PATH = os.getenv("REPORT_PATH", "reports/automated/metrics-report.json")

    # Create an instance of MetricsAutomation and run it
    metrics_automation = MetricsAutomation(METRICS_ENDPOINT, REPORT_PATH)
    metrics_automation.run()