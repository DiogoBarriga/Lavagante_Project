import pytest
from src.project_tracking.task_manager import TaskManager

def test_add_task():
    task_manager = TaskManager()
    task_manager.add_task("Test task", "This is a test task.")
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0]["title"] == "Test task"
    assert task_manager.tasks[0]["description"] == "This is a test task."

def test_complete_task():
    task_manager = TaskManager()
    task_manager.add_task("Test task", "This is a test task.")
    task_manager.complete_task(0)
    assert task_manager.tasks[0]["completed"] is True

def test_remove_task():
    task_manager = TaskManager()
    task_manager.add_task("Test task", "This is a test task.")
    task_manager.remove_task(0)
    assert len(task_manager.tasks) == 0

def test_get_all_tasks():
    task_manager = TaskManager()
    task_manager.add_task("Test task 1", "This is the first test task.")
    task_manager.add_task("Test task 2", "This is the second test task.")
    tasks = task_manager.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Test task 1"
    assert tasks[1]["title"] == "Test task 2"