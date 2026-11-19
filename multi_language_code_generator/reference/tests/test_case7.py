import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestEmptyLogs(unittest.TestCase):
    def test_empty_logs(self):
        result = LogAnalyzer().analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()