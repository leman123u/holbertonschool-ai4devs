import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestErrorRequests(unittest.TestCase):
    def test_error_requests(self):
        analyzer = LogAnalyzer()
        logs = [
            '192.168.1.1 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '192.168.1.2 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 404 100'
        ]
        self.assertEqual(analyzer.analyze(logs)["error_requests"], 1)


if __name__ == "__main__":
    unittest.main()