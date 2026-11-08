import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import detect

def row(h, ip):
    return {"host": h, "ip": ip}

class TestIPConflict(unittest.TestCase):
    def test_conflict_found(self):
        conflicts, _ = detect([row("A", "10.0.0.5"), row("B", "10.0.0.5")])
        self.assertEqual(conflicts, [("10.0.0.5", ["A", "B"])])
    def test_no_conflict(self):
        conflicts, _ = detect([row("A", "10.0.0.5"), row("B", "10.0.0.6")])
        self.assertEqual(conflicts, [])
    def test_invalid_reported(self):
        _, invalid = detect([row("A", "999.1.1.1")])
        self.assertEqual(invalid, [("A", "999.1.1.1")])
    def test_three_way_conflict(self):
        conflicts, _ = detect([row("A", "10.0.0.5"), row("B", "10.0.0.5"), row("C", "10.0.0.5")])
        self.assertEqual(len(conflicts[0][1]), 3)
