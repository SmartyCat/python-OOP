from __future__ import annotations
import time


class AdvancedTimer:
    def __init__(self) -> None:
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self) -> AdvancedTimer:
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.last_run = time.perf_counter() - self.start
        self.runs.append(self.last_run)
        self.min, self.max = min(self.runs), max(self.runs)

