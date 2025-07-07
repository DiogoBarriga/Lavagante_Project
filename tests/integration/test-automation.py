import pytest
from src.automation.metrics-automation import MetricsCollector
from src.automation.reporting-automation import ReportGenerator

@pytest.fixture
def setup_metrics_collector():
    collector = MetricsCollector()
    yield collector
    collector.cleanup()

@pytest.fixture
def setup_report_generator():
    generator = ReportGenerator()
    yield generator
    generator.cleanup()

def test_metrics_collection(setup_metrics_collector):
    metrics = setup_metrics_collector.collect_metrics()
    assert metrics is not None
    assert isinstance(metrics, dict)
    assert 'performance' in metrics
    assert 'quality' in metrics

def test_report_generation(setup_report_generator):
    report = setup_report_generator.generate_report()
    assert report is not None
    assert 'summary' in report
    assert 'details' in report
    assert isinstance(report['details'], list)  # Ensure details is a list

def test_automation_integration(setup_metrics_collector, setup_report_generator):
    metrics = setup_metrics_collector.collect_metrics()
    report = setup_report_generator.generate_report(metrics)
    assert report is not None
    assert report['summary'] == "Metrics Report"
    assert len(report['details']) > 0  # Ensure there are details in the report