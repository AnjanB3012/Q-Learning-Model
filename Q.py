import random

class Q:
    def __init__(self, situation: list, outcome: int, nodeId: int):
        self.__situation = situation
        self.__outcome = outcome
        self.ID = nodeId
        self.__Q = random.randint(0,1)
    
    def getSituation(self) -> list:
        return self.__situation
    
    def getOutcome(self) -> int:
        return self.__outcome
    
    def getQ(self) -> float:
        return self.__Q
    
    def setQ(self, newQ):
        self.__Q = newQ
    
    def getID(self) -> int:
        return self.ID