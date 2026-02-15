from patterns.sql_injection import detect_sql_injection
from patterns.xss import detect_xss
from patterns.brute_force import detect_bruteforce

def run_detection(log_lines):
    alerts = {
        "sql_injection": [],
        "xss": [],
        "bruteforce": {}
    }

    for line in log_lines:
        if detect_sql_injection(line):
            alerts["sql_injection"].append(line.strip())

        if detect_xss(line):
            alerts["xss"].append(line.strip())

    alerts["bruteforce"] = detect_bruteforce(log_lines)

    return alerts
