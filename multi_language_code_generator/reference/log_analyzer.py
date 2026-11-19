
import ipaddress
import re


class LogAnalyzer:
    """Analyze Apache access logs and calculate statistics."""

    LOG_PATTERN = re.compile(
        r'^(\S+)\s+\S+\s+\S+\s+\[[^\]]+\]\s+"[^"]*"\s+(\d{3})\s+\S+'
    )

    def parse_line(self, line: str) -> dict | None:
        """Parse and validate one Apache log entry."""

        match = self.LOG_PATTERN.match(line.strip())

        if not match:
            return None

        ip_address, status_code = match.groups()

        try:
            ipaddress.ip_address(ip_address)
            status = int(status_code)
        except ValueError:
            return None

        if not 100 <= status <= 599:
            return None

        return {
            "ip": ip_address,
            "status": status
        }

    def analyze(self, lines) -> dict:
        """Calculate statistics for valid Apache log entries."""

        total_requests = 0
        error_requests = 0
        unique_visitors = set()

        for line in lines:
            entry = self.parse_line(line)

            if entry is None:
                continue

            total_requests += 1
            unique_visitors.add(entry["ip"])

            if 400 <= entry["status"] <= 599:
                error_requests += 1

        error_rate = (
            round((error_requests / total_requests) * 100, 2)
            if total_requests > 0
            else 0.0
        )

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_visitors),
            "error_requests": error_requests,
            "error_rate": error_rate
        }
