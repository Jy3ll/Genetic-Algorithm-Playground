from backpack_problem.solver import Solver
import numpy as np

MAX_SIZE = 2500
ITEM_COUNT = 100
LOW_BOUNDARY = 11
HIGH_BOUNDARY = 90
INCREASED_MUTATION_RATE = 20
NUMBER_OF_GENERATIONS = 10000


if __name__ == "__main__":
    rng = np.random.default_rng()
    items = rng.integers(LOW_BOUNDARY, HIGH_BOUNDARY, ITEM_COUNT)
    solver = Solver(MAX_SIZE, items, NUMBER_OF_GENERATIONS, INCREASED_MUTATION_RATE)
    (result_free_space_history, result_layout) = solver.solve()
    print("Best solution found: ", result_free_space_history[-1], "\n",
          "For Max Size: ", MAX_SIZE, "\n",
          "Items:\n",
          items, "\n",
          "Genome Layout:\n",
          result_layout, "\n",
          "Solution history:\n",
          np.array(result_free_space_history))
