from dataclasses import dataclass
import random


@dataclass
class OptimizationResult:
    solution: list
    value: float
    runtime: float


class Optimizer:
    def __init__(self, objective, dimension, lower=-5.0, upper=5.0, seed=42):
        self.objective = objective
        self.dimension = dimension
        self.lower = lower
        self.upper = upper
        self.random = random.Random(seed)

    def clip(self, value):
        return max(self.lower, min(self.upper, value))

    def run(self):
        raise NotImplementedError
