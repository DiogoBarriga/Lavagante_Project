import json
from datetime import datetime, timedelta

class SprintPlanner:
    def __init__(self, sprint_duration_days=14):
        self.sprint_duration = timedelta(days=sprint_duration_days)
        self.sprint_backlog = []
        self.sprint_goal = ""
        self.start_date = None
        self.end_date = None

    def set_sprint_goal(self, goal):
        self.sprint_goal = goal

    def start_sprint(self):
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.sprint_duration
        print(f"Sprint started: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}")

    def add_to_backlog(self, task):
        self.sprint_backlog.append(task)

    def remove_from_backlog(self, task):
        if task in self.sprint_backlog:
            self.sprint_backlog.remove(task)

    def get_backlog(self):
        return self.sprint_backlog

    def sprint_summary(self):
        return {
            "sprint_goal": self.sprint_goal,
            "sprint_backlog": self.sprint_backlog,
            "start_date": self.start_date.strftime('%Y-%m-%d') if self.start_date else None,
            "end_date": self.end_date.strftime('%Y-%m-%d') if self.end_date else None,
        }

    def save_sprint_summary(self, filename='sprint_summary.json'):
        summary = self.sprint_summary()
        with open(filename, 'w') as f:
            json.dump(summary, f, indent=4)
        print(f"Sprint summary saved to {filename}")

# Example usage
if __name__ == "__main__":
    planner = SprintPlanner()
    planner.set_sprint_goal("Complete user authentication feature")
    planner.start_sprint()
    planner.add_to_backlog("Implement login functionality")
    planner.add_to_backlog("Create registration page")
    planner.save_sprint_summary()