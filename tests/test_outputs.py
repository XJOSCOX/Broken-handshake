import json
from pathlib import Path

import pytest


REPORT = Path("/app/report.json")
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_CLIENTS = ["10.0.0.5", "192.168.0.1", "192.168.0.2"]
EXPECTED_PATH_COUNTS = {
    "/about.html": 2,
    "/api/login": 1,
    "/index.html": 3,
}
EXPECTED_TOP_PATH = "/index.html"


@pytest.fixture
def report_text():
    return REPORT.read_text()


@pytest.fixture
def report(report_text):
    return json.loads(report_text)


def test_report_is_valid_json(report):
    """Criterion 1: /app/report.json is valid JSON."""
    assert isinstance(report, dict)


def test_total_requests(report):
    """Criterion 2: total_requests is the total number of non-empty log lines."""
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS


def test_unique_clients(report):
    """Criterion 3: unique_clients is the number of distinct client IPs."""
    assert report.get("unique_clients") == len(EXPECTED_CLIENTS)


def test_clients(report):
    """Criterion 4: clients is the sorted list of distinct client IPs."""
    assert report.get("clients") == EXPECTED_CLIENTS


def test_path_counts(report):
    """Criterion 5: path_counts maps each requested path to its request count."""
    assert report.get("path_counts") == EXPECTED_PATH_COUNTS


def test_top_path(report):
    """Criterion 6: top_path is the most requested path with lexicographic tie-break."""
    assert report.get("top_path") == EXPECTED_TOP_PATH
