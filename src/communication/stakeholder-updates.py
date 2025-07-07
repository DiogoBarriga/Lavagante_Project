# stakeholder-updates.py

import json
import datetime

class StakeholderUpdates:
    def __init__(self, stakeholders):
        self.stakeholders = stakeholders
        self.updates = []

    def add_update(self, update):
        timestamp = datetime.datetime.now().isoformat()
        self.updates.append({
            'timestamp': timestamp,
            'update': update
        })

    def send_updates(self):
        for stakeholder in self.stakeholders:
            self._send_update_to_stakeholder(stakeholder)

    def _send_update_to_stakeholder(self, stakeholder):
        # Placeholder for sending updates (e.g., email, notification)
        print(f"Sending update to {stakeholder['name']} at {stakeholder['email']}")
        print(f"Update: {self.updates[-1]['update']}")

    def save_updates_to_file(self, filename='stakeholder_updates.json'):
        with open(filename, 'w') as f:
            json.dump(self.updates, f, indent=4)
        print(f"Updates saved to {filename}")

# Example usage
if __name__ == "__main__":
    stakeholders = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    
    updates_manager = StakeholderUpdates(stakeholders)
    updates_manager.add_update("Project is on track for the next milestone.")
    updates_manager.send_updates()
    updates_manager.save_updates_to_file()