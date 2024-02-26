# com_environment.py
#2. Convert the environment to a ‘n’ room environment where n >= 2

class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


from abc import abstractmethod

class Environment(object):
    @abstractmethod
    def __init__(self, n):
        self.n = n
        self.rooms = [Room(chr(65 + i)) for i in range(n)]  # Assuming room names are 'A', 'B', 'C'

    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n
