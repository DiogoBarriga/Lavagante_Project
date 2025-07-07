import time
import json
from datetime import datetime

class TimeTracker:
    def __init__(self):
        self.time_records = []

    def start_task(self, task_name):
        """Start tracking time for a specific task."""
        self.current_task = {
            'task_name': task_name,
            'start_time': time.time(),
            'end_time': None,
            'duration': None
        }
        print(f"Started tracking task: {task_name}")

    def stop_task(self):
        """Stop tracking the current task."""
        if hasattr(self, 'current_task'):
            self.current_task['end_time'] = time.time()
            self.current_task['duration'] = self.current_task['end_time'] - self.current_task['start_time']
            self.time_records.append(self.current_task)
            print(f"Stopped tracking task: {self.current_task['task_name']}")
            del self.current_task
        else:
            print("No task is currently being tracked.")

    def save_records(self, file_path='time_records.json'):
        """Save time records to a JSON file."""
        with open(file_path, 'w') as f:
            json.dump(self.time_records, f, default=str)
        print(f"Time records saved to {file_path}")

    def load_records(self, file_path='time_records.json'):
        """Load time records from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                self.time_records = json.load(f)
            print(f"Time records loaded from {file_path}")
        except FileNotFoundError:
            print(f"No records found at {file_path}. Starting fresh.")

    def report(self):
        """Generate a report of the tracked time."""
        report_data = []
        for record in self.time_records:
            report_data.append({
                'task_name': record['task_name'],
                'start_time': datetime.fromtimestamp(record['start_time']).strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': datetime.fromtimestamp(record['end_time']).strftime('%Y-%m-%d %H:%M:%S') if record['end_time'] else 'In Progress',
                'duration': record['duration']
            })
        return report_data

# Example usage
if __name__ == "__main__":
    tracker = TimeTracker()
    tracker.load_records()
    tracker.start_task("Develop Feature A")
    time.sleep(2)  # Simulating task duration
    tracker.stop_task()
    tracker.save_records()
    print(tracker.report())