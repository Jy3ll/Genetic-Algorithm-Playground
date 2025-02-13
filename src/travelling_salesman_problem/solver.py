from travelling_salesman_problem.salesman import Salesman


class Solver:
    limit_of_generations = 0
    increased_mutation_rate_threshold = 0

    def __init__(self, road_matrix, limit_of_generations, increased_mutation_rate_threshold):
        self.salesman = Salesman(road_matrix)
        self.limit_of_generations = limit_of_generations
        self.increased_mutation_rate_threshold = increased_mutation_rate_threshold

    def solve(self):
        generations_without_improvement = 0

        for i in range(self.limit_of_generations):
            current_result = self.salesman.time_consumed
            self.salesman.mutate(generations_without_improvement > self.increased_mutation_rate_threshold)

            if current_result == self.salesman.time_consumed:
                generations_without_improvement += 1
            else:
                generations_without_improvement = 0

        return self.salesman.time_consumed_history, self.salesman.road_layout
