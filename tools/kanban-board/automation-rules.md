# Automation Rules for Kanban Board

This document outlines the automation rules implemented for the Kanban board in the Lavagante project management system. These rules help streamline workflows, enhance productivity, and ensure that tasks move smoothly through the various stages of the project lifecycle.

## Automation Rules

1. **Task Creation**
   - When a new task is created, it is automatically assigned to the "To Do" column.
   - A default assignee can be set based on the project team configuration.

2. **Task Movement**
   - When a task is moved from "To Do" to "In Progress":
     - The start date is automatically recorded.
     - A notification is sent to the assigned team member.
   - When a task is moved from "In Progress" to "Review":
     - The task is automatically assigned to the designated reviewer.
     - A notification is sent to the reviewer.

3. **Task Completion**
   - When a task is moved to "Done":
     - The completion date is recorded.
     - A summary report is generated and sent to stakeholders.
     - The task is archived after 30 days.

4. **Due Date Reminders**
   - Automated reminders are sent to assignees 3 days before a task's due date.
   - If a task is overdue, a notification is sent to the assignee and their manager.

5. **Daily Standup Updates**
   - At the start of each day, a summary of tasks in "In Progress" and "Review" is sent to the team via the notification system.

6. **Weekly Reporting**
   - A weekly report is generated summarizing the status of tasks in each column and sent to stakeholders every Friday.

## Implementation Notes

- These automation rules are configured using GitHub Actions and integrated with the Kanban board tool.
- Custom scripts may be utilized to handle specific notifications and reporting tasks.
- Regular reviews of these rules should be conducted to ensure they meet the evolving needs of the project team.