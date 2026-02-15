def generate_report(alerts: dict):
    print("\n=== Intrusion Detection Report ===\n")

    for attack, results in alerts.items():
        print(f"[{attack.upper()}]")
        if not results:
            print("  No detections\n")
            continue

        if isinstance(results, dict):
            for ip, count in results.items():
                print(f"  IP {ip} → {count} failed attempts")
        else:
            for entry in results:
                print(f"  {entry}")

        print()
