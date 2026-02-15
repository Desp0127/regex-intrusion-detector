def load_logs(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()
