from load_balancer.balancer import Balancer

class Solver:
    generations_without_improvement_limit = 0
    increased_mutation_rate_threshold = 0

    def __init__(self, tasks, processors, generations_without_improvement_limit, increased_mutation_rate_threshold):
        self.balancer = Balancer(tasks, processors)
        self.generations_without_improvement_limit = generations_without_improvement_limit
        self.increased_mutation_rate_threshold = increased_mutation_rate_threshold

    def solve(self):
        generations_without_improvement = 0
        minimal_execution_time = max(self.balancer.tasks)

        while generations_without_improvement < self.generations_without_improvement_limit:
            current_result = self.balancer.execution_time
            self.balancer.mutate(generations_without_improvement > self.increased_mutation_rate_threshold)

            if current_result == self.balancer.execution_time:
                generations_without_improvement += 1
            else:
                generations_without_improvement = 0

            if self.balancer.execution_time == minimal_execution_time:
                break

        return self.balancer.execution_time_history, self.balancer.task_layout
