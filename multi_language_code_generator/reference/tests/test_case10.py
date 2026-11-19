import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestServerError(unittest.TestCase):
    def test_server_error(self):
        log = '192.168.1.5 - - [19/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 500 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["error_requests"], 1)
        self.assertEqual(result["error_rate"], 100.0)


if __name__ == "__main__":
    unittest.main()