
import unittest
import os
import sys

# Add the reference directory to Python's import path
REFERENCE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, REFERENCE_DIR)

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def make_log(self, ip, status):
        return (
            f'{ip} - - [19/Nov/2026:10:00:00 +0000] '
            f'"GET /index.html HTTP/1.1" {status} 1024'
        )

    def test_empty_file(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_single_request(self):
        result = self.analyzer.analyze([
            self.make_log("192.168.1.1", 200)
        ])
        self.assertEqual(result["total_requests"], 1)

    def test_unique_visitors(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            self.make_log("192.168.1.2", 200),
            self.make_log("192.168.1.1", 200)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["unique_visitors"], 2)

    def test_error_requests(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            self.make_log("192.168.1.2", 404),
            self.make_log("192.168.1.3", 500)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_requests"], 2)

    def test_error_rate(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            self.make_log("192.168.1.2", 404),
            self.make_log("192.168.1.3", 200),
            self.make_log("192.168.1.4", 500)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 50.0)

    def test_no_errors(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            self.make_log("192.168.1.2", 301)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 0.0)

    def test_all_errors(self):
        logs = [
            self.make_log("192.168.1.1", 404),
            self.make_log("192.168.1.2", 500)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 100.0)

    def test_malformed_entry(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            "this is not a valid Apache log",
            self.make_log("192.168.1.2", 404)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 2)

    def test_invalid_ip(self):
        logs = [
            self.make_log("999.999.999.999", 200),
            self.make_log("192.168.1.1", 200)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)

    def test_missing_status_code(self):
        logs = [
            '192.168.1.1 - - [19/Nov/2026:10:00:00 +0000] '
            '"GET /index.html HTTP/1.1"',
            self.make_log("192.168.1.2", 200)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)

    def test_boundary_error_codes(self):
        logs = [
            self.make_log("192.168.1.1", 399),
            self.make_log("192.168.1.2", 400),
            self.make_log("192.168.1.3", 599),
            self.make_log("192.168.1.4", 600)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["error_requests"], 2)


if __name__ == "__main__":
    unittest.main()
