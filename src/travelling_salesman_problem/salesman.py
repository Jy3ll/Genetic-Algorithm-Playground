import numpy as np


class Salesman:
    road_cost_matrix = np.zeros((0, 0))
    road_layout = np.zeros(0)
    time_consumed = -1
    time_consumed_history = []

    def __init__(self, road_cost_matrix):
        self.road_cost_matrix = road_cost_matrix
        self.road_layout = (np.arange(self.road_cost_matrix.shape[0]) + 1) % self.road_cost_matrix.shape[0]

        self.rng = np.random.default_rng()
        self.time_consumed = self._calculate_time_consumed(self.road_layout)
        self.time_consumed_history.append(self.time_consumed)

    def mutate(self, increased_mutation_rate):
        mutated_layout = self.road_layout.copy()
        mutated_start_index = self.rng.integers(mutated_layout.shape[0])
        mutated_end_index = self.rng.integers(mutated_layout.shape[0])
        while mutated_end_index == mutated_start_index or \
                mutated_layout[mutated_start_index] == mutated_end_index or \
                mutated_layout[mutated_end_index] == mutated_start_index:
            mutated_end_index = self.rng.integers(mutated_layout.shape[0])

        tmp_swap = mutated_layout[mutated_start_index]
        mutated_layout[mutated_start_index] = mutated_layout[mutated_end_index]
        mutated_layout[mutated_end_index] = tmp_swap

        if increased_mutation_rate:
            second_mutated_start_index = self.rng.integers(mutated_layout.shape[0])
            while second_mutated_start_index == mutated_start_index:
                second_mutated_start_index = self.rng.integers(mutated_layout.shape[0])

            second_mutated_end_index = self.rng.integers(mutated_layout.shape[0])
            while second_mutated_end_index == mutated_end_index or \
                    second_mutated_end_index == second_mutated_start_index or \
                    mutated_layout[second_mutated_start_index] == second_mutated_end_index or \
                    mutated_layout[second_mutated_end_index] == second_mutated_start_index:
                second_mutated_end_index = self.rng.integers(mutated_layout.shape[0])

            tmp_swap = mutated_layout[second_mutated_start_index]
            mutated_layout[second_mutated_start_index] = mutated_layout[second_mutated_end_index]
            mutated_layout[second_mutated_end_index] = tmp_swap

        mutated_time_consumed = self._calculate_time_consumed(mutated_layout)

        if self._time_consumed_is_better_than_parent(mutated_time_consumed):
            self.road_layout = mutated_layout
            self.time_consumed = mutated_time_consumed
            self.time_consumed_history.append(self.time_consumed)

    def _calculate_time_consumed(self, calculated_layout):
        calculated_time = 0
        for i in range(calculated_layout.shape[0]):
            calculated_time += self.road_cost_matrix[i, calculated_layout[i]]
        return calculated_time

    def _time_consumed_is_better_than_parent(self, child_time_consumed):
        return child_time_consumed < self.time_consumed
