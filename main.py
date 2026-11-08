"""Find IP addresses claimed by more than one host.

Usage: python3 main.py hosts.csv
CSV columns: host,ip.
An IP used by two or more hosts is a CONFLICT; invalid IPs are
reported as INVALID instead of being silently skipped.
"""
import argparse, csv, ipaddress, sys
from collections import defaultdict

def detect(rows):
    by_ip = defaultdict(list)
    invalid = []
    for row in rows:
        try:
            ip = str(ipaddress.ip_address(row["ip"].strip()))
        except ValueError:
            invalid.append((row["host"], row["ip"].strip()))
            continue
        by_ip[ip].append(row["host"])
    conflicts = [(ip, hosts) for ip, hosts in by_ip.items() if len(hosts) > 1]
    return sorted(conflicts), sorted(invalid)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        conflicts, invalid = detect(list(csv.DictReader(f)))
    for ip, hosts in conflicts:
        print(f"{ip}: CONFLICT ({', '.join(hosts)})")
    for host, ip in invalid:
        print(f"{host}: INVALID IP ({ip})")
    if not conflicts and not invalid:
        print("No IP conflicts found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
