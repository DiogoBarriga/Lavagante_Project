# Metrics Collector for Project Management Dashboard

import os
import json
import time
import requests

class MetricsCollector:
    def __init__(self, api_url, project_id):
        self.api_url = api_url
        self.project_id = project_id
        self.metrics = {
            "task_completion": 0,
            "sprint_velocity": 0,
            "bug_count": 0,
            "code_quality": 0,
            "release_frequency": 0
        }

    def collect_metrics(self):
        self.metrics["task_completion"] = self.get_task_completion()
        self.metrics["sprint_velocity"] = self.get_sprint_velocity()
        self.metrics["bug_count"] = self.get_bug_count()
        self.metrics["code_quality"] = self.get_code_quality()
        self.metrics["release_frequency"] = self.get_release_frequency()

    def get_task_completion(self):
        # Simulate API call to get task completion percentage
        response = requests.get(f"{self.api_url}/projects/{self.project_id}/tasks")
        tasks = response.json()
        completed_tasks = sum(1 for task in tasks if task['status'] == 'completed')
        return (completed_tasks / len(tasks)) * 100 if tasks else 0

    def get_sprint_velocity(self):
        # Simulate API call to get sprint velocity
        response = requests.get(f"{self.api_url}/projects/{self.project_id}/sprints")
        sprints = response.json()
        return sum(sprint['velocity'] for sprint in sprints) / len(sprints) if sprints else 0

    def get_bug_count(self):
        # Simulate API call to get bug count
        response = requests.get(f"{self.api_url}/projects/{self.project_id}/bugs")
        bugs = response.json()
        return len(bugs)

    def get_code_quality(self):
        # Simulate API call to get code quality metrics
        response = requests.get(f"{self.api_url}/projects/{self.project_id}/code-quality")
        quality_data = response.json()
        return quality_data['quality_score'] if 'quality_score' in quality_data else 0

    def get_release_frequency(self):
        # Simulate API call to get release frequency
        response = requests.get(f"{self.api_url}/projects/{self.project_id}/releases")
        releases = response.json()
        return len(releases) / (self.get_project_duration() / (24 * 60 * 60)) if releases else 0

    def get_project_duration(self):
        # Simulate API call to get project duration
        response = requests.get(f"{self.api_url}/projects/{self.project_id}")
        project_data = response.json()
        start_date = time.strptime(project_data['start_date'], "%Y-%m-%d")
        end_date = time.strptime(project_data['end_date'], "%Y-%m-%d")
        return time.mktime(end_date) - time.mktime(start_date)

    def save_metrics(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.metrics, f, indent=4)

if __name__ == "__main__":
    collector = MetricsCollector(api_url="http://api.example.com", project_id="12345")
    collector.collect_metrics()
    collector.save_metrics("project_metrics.json")