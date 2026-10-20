import csv
import math
from pathlib import Path

from benchmark_functions import BenchmarkFunctions
from pso import ParticleSwarmOptimizer
from ga import GeneticAlgorithm

DIMENSIONS = [1, 2, 3, 5, 10, 20, 30, 40, 50, 100]
TRIALS = 10
THRESHOLD = 0.01
OUTPUT_DIR = Path(__file__).parent / 'results'


def run_experiments(function_name, objective):
    rows = []
    for dimension in DIMENSIONS:
        for algorithm in (ParticleSwarmOptimizer, GeneticAlgorithm):
            values, runtimes = [], []
            for trial in range(TRIALS):
                result = algorithm(objective, dimension=dimension, seed=1000 + trial).run()
                values.append(result.value)
                runtimes.append(result.runtime)
            rows.append({
                'function': function_name,
                'dimension': dimension,
                'algorithm': algorithm.__name__,
                'runtime_seconds': sum(runtimes) / TRIALS,
                'rmse': math.sqrt(sum(value * value for value in values) / TRIALS),
                'correctness_percent': 100 * sum(value <= THRESHOLD for value in values) / TRIALS,
            })
    return rows


def main():
    functions = {
        'Ackley': BenchmarkFunctions.ackley,
        'Sphere': BenchmarkFunctions.sphere,
        'Rastrigin': BenchmarkFunctions.rastrigin,
        'Rosenbrock': BenchmarkFunctions.rosenbrock,
    }
    OUTPUT_DIR.mkdir(exist_ok=True)
    all_rows = []
    for name, objective in functions.items():
        rows = run_experiments(name, objective)
        all_rows.extend(rows)
        path = OUTPUT_DIR / f'{name.lower()}_results.csv'
        with path.open('w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f'Saved {name} results to: {path}')

    metric_files = {
        'runtime_results.csv': ['function', 'dimension', 'algorithm', 'runtime_seconds'],
        'rmse_results.csv': ['function', 'dimension', 'algorithm', 'rmse'],
        'correctness_results.csv': ['function', 'dimension', 'algorithm', 'correctness_percent'],
    }
    for filename, fields in metric_files.items():
        path = OUTPUT_DIR / filename
        with path.open('w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows({field: row[field] for field in fields} for row in all_rows)
        print(f'Saved metric table to: {path}')


if __name__ == '__main__':
    main()
