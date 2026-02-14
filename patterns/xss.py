import re

XSS_PATTERNS = [
    re.compile(r"(?i)<script.*?>"),
    re.compile(r"(?i)javascript:"),
    re.compile(r"(?i)onerror\s*="),
]

def detect_xss(line: str) -> bool:
    return any(p.search(line) for p in XSS_PATTERNS)
