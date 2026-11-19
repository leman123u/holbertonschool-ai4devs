import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestUniqueVisitors(unittest.TestCase):
    def test_unique_visitors(self):
        analyzer = LogAnalyzer()
        logs = [
            '192.168.1.1 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '192.168.1.2 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100'
        ]
        self.assertEqual(analyzer.analyze(logs)["unique_visitors"], 2)


if __name__ == "__main__":
    unittest.main()