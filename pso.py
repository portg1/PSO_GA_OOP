import time
from optimizer import Optimizer, OptimizationResult


class ParticleSwarmOptimizer(Optimizer):
    def __init__(self, objective, dimension, particles=30, iterations=100, **kwargs):
        super().__init__(objective, dimension, **kwargs)
        self.particles = particles
        self.iterations = iterations

    def run(self):
        start = time.perf_counter(); r = self.random
        positions = [[r.uniform(self.lower, self.upper) for _ in range(self.dimension)] for _ in range(self.particles)]
        velocities = [[r.uniform(-1, 1) for _ in range(self.dimension)] for _ in range(self.particles)]
        personal = [p[:] for p in positions]
        values = [self.objective(p) for p in personal]
        best_i = min(range(self.particles), key=values.__getitem__)
        global_best, global_value = personal[best_i][:], values[best_i]
        for _ in range(self.iterations):
            for i in range(self.particles):
                for d in range(self.dimension):
                    velocities[i][d] = (0.7 * velocities[i][d] + 1.5 * r.random() * (personal[i][d] - positions[i][d]) + 1.5 * r.random() * (global_best[d] - positions[i][d]))
                    positions[i][d] = self.clip(positions[i][d] + velocities[i][d])
                value = self.objective(positions[i])
                if value < values[i]:
                    personal[i], values[i] = positions[i][:], value
                    if value < global_value: global_best, global_value = positions[i][:], value
        return OptimizationResult(global_best, global_value, time.perf_counter() - start)
