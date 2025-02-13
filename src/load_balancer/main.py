from load_balancer.solver import Solver
import numpy as np

USE_RANDOM_PROCESSORS = True
TASK_COUNT = 100
PROCESSOR_COUNT = 4
LOW_EXECUTION_TASK_BOUNDARY = 10
HIGH_EXECUTION_TASK_BOUNDARY = 91
LOW_PROCESSOR_MULTIPLIER_BOUNDARY = 1.0
HIGH_PROCESSOR_MULTIPLIER_BOUNDARY = 2.0
INCREASED_MUTATION_RATE = 5000
GENERATIONS_WITHOUT_IMPROVEMENT_LIMIT = 100000


def random_or_predefined_processors(random_processors_condition):
    generator = np.random.default_rng()
    if random_processors_condition:
        return generator.random(PROCESSOR_COUNT) * (
            HIGH_PROCESSOR_MULTIPLIER_BOUNDARY - LOW_PROCESSOR_MULTIPLIER_BOUNDARY) + LOW_PROCESSOR_MULTIPLIER_BOUNDARY
    return [1.0, 1.25, 1.5, 1.75]


if __name__ == "__main__":
    rng = np.random.default_rng()
    tasks = rng.integers(LOW_EXECUTION_TASK_BOUNDARY, HIGH_EXECUTION_TASK_BOUNDARY, TASK_COUNT)
    processors = random_or_predefined_processors(USE_RANDOM_PROCESSORS)
    solver = Solver(tasks, processors, GENERATIONS_WITHOUT_IMPROVEMENT_LIMIT, INCREASED_MUTATION_RATE)
    (result_execution_time_history, result_layout) = solver.solve()
    processor_usage = [len([j for j in result_layout if j == i]) for i in range(len(processors))]
    print("Best solution found: ", result_execution_time_history[-1], "\n",
          "For Processors:\n",
          processors, "\n",
          "Tasks:\n",
          tasks, "\n",
          "Genome Layout:\n",
          result_layout, "\n",
          "Processor usage:\n",
          processor_usage, "\n",
          "Solution history:\n",
          np.array(result_execution_time_history))
