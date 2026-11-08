# ip-conflict-detector

Find IP addresses claimed by more than one host in a hosts CSV — a classic cause of flaky connectivity — and report invalid IPs instead of skipping them.

## How to run

```sh
python3 main.py hosts.csv
```

## Example output

```
10.0.0.5: CONFLICT (PC-07, PC-12)
PC-99: INVALID IP (999.1.1.1)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
