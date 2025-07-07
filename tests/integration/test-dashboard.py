import pytest
from src.dashboard.metrics-collector import collect_metrics
from src.dashboard.report-generator import generate_report
from src.dashboard.visualization import visualize_metrics

def test_collect_metrics():
    metrics = collect_metrics()
    assert isinstance(metrics, dict), "Metrics should be a dictionary"
    assert "performance" in metrics, "Metrics should contain performance data"
    assert "quality" in metrics, "Metrics should contain quality data"

def test_generate_report():
    metrics = {
        "performance": {"speed": 100, "efficiency": 90},
        "quality": {"defects": 2, "coverage": 85}
    }
    report = generate_report(metrics)
    assert isinstance(report, str), "Report should be a string"
    assert "Performance Metrics" in report, "Report should include performance metrics"
    assert "Quality Metrics" in report, "Report should include quality metrics"

def test_visualize_metrics():
    metrics = {
        "performance": {"speed": 100, "efficiency": 90},
        "quality": {"defects": 2, "coverage": 85}
    }
    visualization = visualize_metrics(metrics)
    assert visualization is not None, "Visualization should not be None"
    assert "graph" in visualization, "Visualization should contain a graph element"