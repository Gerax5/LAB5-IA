from abc import ABC, abstractmethod

class Problem(ABC):
    def __init__(self, initial_state):
        self.initial_state = initial_state

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, action):
        pass

    @abstractmethod
    def goal_test(self, state):
        pass

    @abstractmethod
    def step_cost(self, state, action, new_state):
        pass
