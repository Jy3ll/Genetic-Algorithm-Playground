import numpy as np


class Balancer:
    tasks = []
    processors = []
    task_layout = np.zeros(0)
    execution_time = -1
    execution_time_history = []

    def __init__(self, tasks, processors):
        self.tasks = tasks
        self.processors = processors

        self.rng = np.random.default_rng()
        self.task_layout = self.rng.integers(0, len(processors), len(tasks))
        self.execution_time = self._calculate_execution_time(self.task_layout)
        self.execution_time_history.append(self.execution_time)

    def mutate(self, increased_mutation_rate):
        mutated_layout = self.task_layout.copy()
        mutated_index = self.rng.integers(len(self.tasks))
        mutated_layout[mutated_index] = (mutated_layout[mutated_index] +
                                         self.rng.integers(len(self.processors))) % len(self.processors)
        if increased_mutation_rate:
            second_mutated_index = self.rng.integers(len(self.tasks))
            while second_mutated_index == mutated_index:
                second_mutated_index = self.rng.integers(len(self.tasks))
            mutated_layout[second_mutated_index] = (mutated_layout[second_mutated_index] +
                                                    self.rng.integers(len(self.processors))) % len(self.processors)
        mutated_execution_time = self._calculate_execution_time(mutated_layout)

        if self._execution_time_is_better_than_parent(mutated_execution_time):
            self.task_layout = mutated_layout
            self.execution_time = mutated_execution_time
            self.execution_time_history.append(self.execution_time)

    def _calculate_execution_time(self, calculated_layout):
        processor_execution_times = [self.processors[i] *
                                     sum([self.tasks[j] for j in range(len(self.tasks)) if calculated_layout[j] == i])
                                     for i in range(len(self.processors))]
        return max(processor_execution_times)

    def _execution_time_is_better_than_parent(self, child_execution_time):
        return child_execution_time < self.execution_time
