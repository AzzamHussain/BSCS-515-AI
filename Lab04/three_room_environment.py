
from com_environment import Environment
from com_environment import Room
from com_agent import VaccumAgent

class ThreeRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        '''
        Constructor
        '''
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.move_right()
            elif res == 'left':
                self.move_left()
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    def move_right(self):
        if self.currentRoom == self.r1:
            self.currentRoom = self.r2
        elif self.currentRoom == self.r2:
            self.currentRoom = self.r3

    def move_left(self):
        if self.currentRoom == self.r3:
            self.currentRoom = self.r2
        elif self.currentRoom == self.r2:
            self.currentRoom = self.r1

# Test program
if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = ThreeRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(5)
