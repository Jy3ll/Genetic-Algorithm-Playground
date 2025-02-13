from backpack_problem.backpack import Backpack


class Solver:
    limit_of_generations = 0
    increased_mutation_rate_threshold = 0

    def __init__(self, max_quantity, items, limit_of_generations, increased_mutation_rate_threshold):
        self.backpack = Backpack(max_quantity, items)
        self.limit_of_generations = limit_of_generations
        self.increased_mutation_rate_threshold = increased_mutation_rate_threshold

    def solve(self):
        generations_without_improvement = 0

        for i in range(self.limit_of_generations):
            current_result = self.backpack.free_space
            self.backpack.mutate(generations_without_improvement > self.increased_mutation_rate_threshold)

            if current_result == self.backpack.free_space:
                generations_without_improvement += 1
            else:
                generations_without_improvement = 0

            if self.backpack.free_space == 0:
                break

        if self.backpack.free_space < 0 and min(self.backpack.items) <= self.backpack.max_quantity:
            self.backpack.get_any_valid_solution()

        return self.backpack.free_space_history, self.backpack.layout
