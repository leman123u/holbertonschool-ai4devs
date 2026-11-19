import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestMalformedLog(unittest.TestCase):
    def test_malformed_log(self):
        result = LogAnalyzer().analyze(["This is not a valid log"])
        self.assertEqual(result["total_requests"], 0)


if __name__ == "__main__":
    unittest.main()