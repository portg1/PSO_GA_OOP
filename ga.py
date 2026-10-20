import time
from optimizer import Optimizer, OptimizationResult


class GeneticAlgorithm(Optimizer):
    def __init__(self, objective, dimension, population_size=40, generations=100, **kwargs):
        super().__init__(objective, dimension, **kwargs)
        self.population_size = population_size; self.generations = generations

    def run(self):
        start = time.perf_counter(); r = self.random
        population = [[r.uniform(self.lower, self.upper) for _ in range(self.dimension)] for _ in range(self.population_size)]
        for _ in range(self.generations):
            population.sort(key=self.objective); next_population = population[:2]
            while len(next_population) < self.population_size:
                p1 = r.choice(population[:self.population_size // 2]); p2 = r.choice(population[:self.population_size // 2])
                child = [a if r.random() < 0.5 else b for a, b in zip(p1, p2)]
                for d in range(self.dimension):
                    if r.random() < 0.15: child[d] = self.clip(child[d] + r.gauss(0.0, 0.2))
                next_population.append(child)
            population = next_population
        best = min(population, key=self.objective)
        return OptimizationResult(best, self.objective(best), time.perf_counter() - start)
