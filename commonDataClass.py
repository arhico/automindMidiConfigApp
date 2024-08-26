# Parent class w all needed params for objects to interact
# All objects chould be inheireted from this class
class commonData(object):
    def __init__(self) -> None:
        pass
        self.id = 0
        self.globalScreenOffset = [0,0]
        self.occupiedGridPoints = []