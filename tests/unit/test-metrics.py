import pytest
from src.dashboard.metrics-collector import collect_metrics

def test_collect_metrics():
    # Test the metrics collection functionality
    metrics = collect_metrics()
    assert isinstance(metrics, dict), "Metrics should be a dictionary"
    assert "total_tasks" in metrics, "Metrics should include total_tasks"
    assert "completed_tasks" in metrics, "Metrics should include completed_tasks"
    assert metrics["total_tasks"] >= metrics["completed_tasks"], "Total tasks should be greater than or equal to completed tasks"

def test_metrics_format():
    # Test the format of the collected metrics
    metrics = collect_metrics()
    assert isinstance(metrics["total_tasks"], int), "Total tasks should be an integer"
    assert isinstance(metrics["completed_tasks"], int), "Completed tasks should be an integer"
    assert metrics["total_tasks"] >= 0, "Total tasks should not be negative"
    assert metrics["completed_tasks"] >= 0, "Completed tasks should not be negative"