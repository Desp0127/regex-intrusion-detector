import re
from collections import defaultdict

FAILED_LOGIN_REGEX = re.compile(
    r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"
)

def detect_bruteforce(log_lines, threshold=5):
    ip_counter = defaultdict(int)

    for line in log_lines:
        match = FAILED_LOGIN_REGEX.search(line)
        if match:
            ip = match.group(1)
            ip_counter[ip] += 1

    return {ip: count for ip, count in ip_counter.items() if count >= threshold}
