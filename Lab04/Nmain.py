# main.py
from Nroom import Environment, Room
from Nagent import VacuumAgent

class MultiRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent):
        super().__init__(n=4)  # Assuming 3 rooms for now
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.get_next_room()
            else:
                self.currentRoom = self.get_previous_room()
            self.displayAction()
            self.step += 1

    def get_next_room(self):
        current_index = self.rooms.index(self.currentRoom)
        return self.rooms[(current_index + 1) % self.n]

    def get_previous_room(self):
        current_index = self.rooms.index(self.currentRoom)
        return self.rooms[(current_index - 1) % self.n]

    def displayPerception(self):
        print("Perception at step %d is [%s, %s]" % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

# Test program
if __name__ == '__main__':
    vacuum_agent = VacuumAgent()
    environment = MultiRoomVacuumCleanerEnvironment(vacuum_agent)
    environment.executeStep(50)

    final_score = vacuum_agent.get_score()
    print("Final Score: {}".format(final_score))