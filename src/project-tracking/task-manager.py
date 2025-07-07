class Task:
    def __init__(self, title, description, assignee=None, status='To Do'):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def assign(self, assignee):
        self.assignee = assignee

    def __repr__(self):
        return f"Task(title='{self.title}', status='{self.status}', assignee='{self.assignee}')"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, assignee=None):
        task = Task(title, description, assignee)
        self.tasks.append(task)
        return task

    def update_task(self, task_index, title=None, description=None, assignee=None, status=None):
        if task_index < len(self.tasks):
            task = self.tasks[task_index]
            if title:
                task.title = title
            if description:
                task.description = description
            if assignee:
                task.assign(assignee)
            if status:
                task.update_status(status)
            return task
        else:
            raise IndexError("Task index out of range.")

    def get_tasks(self, status=None):
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

    def __repr__(self):
        return f"TaskManager(tasks={self.tasks})"


# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    task1 = manager.create_task("Implement feature X", "Details about feature X", assignee="Alice")
    task2 = manager.create_task("Fix bug Y", "Details about bug Y", assignee="Bob")

    print(manager.get_tasks())
    manager.update_task(0, status="In Progress")
    print(manager.get_tasks("In Progress"))