# com_agent.py
from abc import abstractmethod

class Agent(object):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

class VacuumAgent(Agent):
    def __init__(self):
        self.score = 0

    def sense(self, env):
        self.environment = env

    def act(self):
        current_room = self.environment.currentRoom

        if current_room.status == 'dirty':
            self.score += 25  # +25 points for cleaning a dirty room
            return 'clean'

        if current_room.location == 'A':
            self.score -= 1  # -1 point for moving from room A
            return 'right'
        elif current_room.location == 'B':
            self.score -= 1  # -1 point for moving from room B
            return 'right'
        elif current_room.location == 'C':
            self.score -= 1  # -1 point for moving from room C
            return 'right'
        elif current_room.location == 'D':
            self.score -= 1  # -1 point for moving from room D
            return 'left'
        elif current_room.location == 'E':
            self.score -= 1  # -1 point for moving from room E
            return 'left'
        elif current_room.location == 'F':
            self.score -= 1  # -1 point for moving from room F
            return 'left'
        return 'stay'  # Default action if no condition matches

    def get_score(self):
        return self.score