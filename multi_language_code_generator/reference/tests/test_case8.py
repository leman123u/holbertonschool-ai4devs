import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestInvalidIP(unittest.TestCase):
    def test_invalid_ip(self):
        log = '999.999.999.999 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["total_requests"], 0)


if __name__ == "__main__":
    unittest.main()