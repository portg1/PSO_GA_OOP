import math


class BenchmarkFunctions:
    @staticmethod
    def ackley(x):
        n = len(x)
        return (-20 * math.exp(-0.2 * math.sqrt(sum(v * v for v in x) / n))
                - math.exp(sum(math.cos(2 * math.pi * v) for v in x) / n)
                + 20 + math.e)

    @staticmethod
    def sphere(x):
        return sum(v * v for v in x)

    @staticmethod
    def rastrigin(x):
        return 10 * len(x) + sum(v * v - 10 * math.cos(2 * math.pi * v) for v in x)

    @staticmethod
    def rosenbrock(x):
        return sum(100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2 for i in range(len(x) - 1))
