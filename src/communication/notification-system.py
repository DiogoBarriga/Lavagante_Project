# notification-system.py

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationSystem:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return json.load(file)

    def send_email(self, subject, body, to_email):
        msg = MIMEMultipart()
        msg['From'] = self.config['email']['from']
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.config['email']['smtp_server'], self.config['email']['smtp_port']) as server:
                server.starttls()
                server.login(self.config['email']['username'], self.config['email']['password'])
                server.send_message(msg)
            print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def notify_stakeholders(self, subject, message, stakeholders):
        for stakeholder in stakeholders:
            self.send_email(subject, message, stakeholder)

# Example usage
if __name__ == "__main__":
    notification_system = NotificationSystem('config/notification-rules.json')
    stakeholders_list = ['stakeholder1@example.com', 'stakeholder2@example.com']
    notification_system.notify_stakeholders('Project Update', 'This is a notification about the project status.', stakeholders_list)