from travelling_salesman_problem.solver import Solver

import sys
import numpy as np

ROAD_MATRIX_SIZE = 100
LOW_ROAD_COST_BOUNDARY = 10
HIGH_ROAD_COST_BOUNDARY = 91
INCREASED_MUTATION_RATE = 5000
GENERATIONS_WITHOUT_IMPROVEMENT_LIMIT = 100000

if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)
    rng = np.random.default_rng()
    road_matrix = rng.integers(LOW_ROAD_COST_BOUNDARY, HIGH_ROAD_COST_BOUNDARY, (ROAD_MATRIX_SIZE, ROAD_MATRIX_SIZE))
    np.fill_diagonal(road_matrix, 0)

    solver = Solver(road_matrix, GENERATIONS_WITHOUT_IMPROVEMENT_LIMIT, INCREASED_MUTATION_RATE)
    (result_time_consumed_history, result_layout) = solver.solve()

    print("Best solution found: ", result_time_consumed_history[-1], "\n",
          "For Road Matrix:\n",
          road_matrix, "\n",
          "Genome Layout:\n",
          result_layout, "\n",
          "Solution history:\n",
          np.array(result_time_consumed_history))
