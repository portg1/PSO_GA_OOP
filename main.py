from benchmark_functions import BenchmarkFunctions
from pso import ParticleSwarmOptimizer
from ga import GeneticAlgorithm


def main():
    functions = {'Ackley': BenchmarkFunctions.ackley, 'Sphere': BenchmarkFunctions.sphere, 'Rastrigin': BenchmarkFunctions.rastrigin, 'Rosenbrock': BenchmarkFunctions.rosenbrock}
    for name, objective in functions.items():
        print(f'\n{name} function - dimension 10')
        for algorithm in (ParticleSwarmOptimizer, GeneticAlgorithm):
            result = algorithm(objective, dimension=10, seed=42).run()
            print(f'{algorithm.__name__}: value={result.value:.8f}, runtime={result.runtime:.6f} seconds')


if __name__ == '__main__':
    main()
