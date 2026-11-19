
import os
import sys
import unittest

REFERENCE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, REFERENCE_DIR)

from log_analyzer import LogAnalyzer


class TestEdgeCases(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def make_log(self, ip, status):
        return (
            f'{ip} - - [19/Nov/2026:10:00:00 +0000] '
            f'"GET /index.html HTTP/1.1" {status} 1024'
        )

    def test_redirect_is_not_error(self):
        result = self.analyzer.analyze([
            self.make_log("192.168.1.1", 301)
        ])
        self.assertEqual(result["error_requests"], 0)

    def test_server_error(self):
        result = self.analyzer.analyze([
            self.make_log("192.168.1.1", 503)
        ])
        self.assertEqual(result["error_requests"], 1)

    def test_ipv6_address(self):
        result = self.analyzer.analyze([
            self.make_log("2001:db8::1", 200)
        ])
        self.assertEqual(result["total_requests"], 1)

    def test_invalid_status_code(self):
        result = self.analyzer.analyze([
            self.make_log("192.168.1.1", 600)
        ])
        self.assertEqual(result["total_requests"], 0)

    def test_multiple_same_ip(self):
        logs = [
            self.make_log("192.168.1.1", 200),
            self.make_log("192.168.1.1", 404),
            self.make_log("192.168.1.1", 500)
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["unique_visitors"], 1)


if __name__ == "__main__":
    unittest.main()
