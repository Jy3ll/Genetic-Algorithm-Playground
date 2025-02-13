import numpy as np


class Backpack:
    max_quantity = 0
    items = []
    layout = np.zeros(0)
    free_space = -1
    free_space_history = []

    def __init__(self, max_quantity, items):
        self.max_quantity = max_quantity
        self.items = items
        self.rng = np.random.default_rng()
        self.layout = self.rng.integers(0, 2, len(items))
        self.free_space = self._calculate_free_space(self.layout)
        self.free_space_history.append(self.free_space)

    def mutate(self, increased_mutation_rate):
        mutated_layout = self.layout.copy()
        mutated_index = self.rng.integers(len(self.items))
        mutated_layout[mutated_index] = (mutated_layout[mutated_index] + 1) % 2
        if increased_mutation_rate:
            second_mutated_index = self.rng.integers(len(self.items))
            while second_mutated_index == mutated_index:
                second_mutated_index = self.rng.integers(len(self.items))
            mutated_layout[second_mutated_index] = (mutated_layout[second_mutated_index] + 1) % 2
        mutated_free_space = self._calculate_free_space(mutated_layout)

        if self._check_if_free_space_is_better_than_parent(mutated_free_space):
            self.layout = mutated_layout
            self.free_space = mutated_free_space
            self.free_space_history.append(self.free_space)

    def get_any_valid_solution(self):
        minimal_value = min(self.items)
        if minimal_value <= self.max_quantity:
            minimal_index = 0
            while self.items[minimal_index] != minimal_value:
                minimal_index += 1
            final_layout = np.zeros(len(self.items), dtype=np.int64)
            final_layout[minimal_index] = 1

            self.layout = final_layout
            self.free_space = self._calculate_free_space(final_layout)
            self.free_space_history.append(self.free_space)


    def _calculate_free_space(self, layout):
        return self.max_quantity - sum([self.items[i] * layout[i] for i in range(len(self.items))])

    def _check_if_free_space_is_better_than_parent(self, child_free_space):
        if child_free_space < 0 and self.free_space < 0:
            return child_free_space > self.free_space

        if self.free_space < 0:
            return True

        if child_free_space < 0:
            return False

        return child_free_space < self.free_space
