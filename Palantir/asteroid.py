from abc import abstractmethod
class SpaceObject(object):
    def __init__(self):
        self.shape
        self.speed
        self.direction
        self.position

    def run(self):
        pass

class Spaceship(SpaceObject):
    def __init__(self, controller):
        self.controller = controller
        pass

    def run(self):
        # new thread for controller

class BigYunshi(SpaceObject):
    def decomposition(self):
        for i in range(DECOM_NUM):
            yunshi = Yunshi()
            yunshi.run()

class Yunshi(SpaceObject):
    def destroy(self):


class Game(object):
    def __init__(self):
        self.spaceobjectList

    def run
