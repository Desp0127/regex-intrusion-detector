import re

SQL_INJECTION_PATTERNS = [
    re.compile(r"(?i)(union\s+select)"),
    re.compile(r"(?i)(or\s+1=1)"),
    re.compile(r"(--|\#|/\*)"),
]

def detect_sql_injection(line: str) -> bool:
    return any(p.search(line) for p in SQL_INJECTION_PATTERNS)

