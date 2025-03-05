import Q
import random
import math
import xml.etree.ElementTree as ET
import ast
import os


def loadModel(modelName, inputLearningRate, inputDiscountFactor, inputEpsilon):
        tree = ET.parse(modelName)
        root = tree.getroot()
        highestID = 0
        tempQTable = {}
        outcomes = []
        for qNode in root.findall("node"):
            node_id = int(qNode.get("id"))
            tempSituation = ast.literal_eval(qNode.find("situation").text)
            for i in range(len(tempSituation)):
                tempSituation[i] = float(tempSituation[i])
            tempOutcome = int(qNode.find("outcome").text)
            if(tempOutcome not in outcomes):
                outcomes.append(tempOutcome)
            tempQ = float(qNode.find("Q").text)
            if(node_id>highestID):
                highestID=node_id
            tempQObj = Q.Q(tempSituation,tempOutcome,nodeId=node_id)
            tempQObj.setQ(tempQ)
            tempQTable[tempQObj] = tempQ
        returningModel = Model(inputLearningRate,inputDiscountFactor,inputEpsilon,outcomes,tempQTable,None,highestID+1)
        return returningModel


class Model:
    def __init__(self, learning_rate: float, discount_factor: float, epsilon:float, possible_Outcomes: list, qTable={},ln=None,lID=0):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = qTable
        self.possible_outcomes = possible_Outcomes
        self.__lastNode = ln
        self.lastId= lID

    def compute(self, situation: list) -> int:
        """
        Gives the output from the models q table or adds a point in the q table

        Args:
            situation (list): The situation the agent is in.

        Returns:
            int: The output actions.
        """
        matchingSituations = self.findOrNullQ(situation=situation)
        if random.uniform(0,1)<self.epsilon:
            if(matchingSituations==None):
                tempList = []
                for poutcome in self.possible_outcomes:
                    newQNode = Q.Q(situation=situation,outcome=poutcome, nodeId=self.lastId)
                    self.lastId+=1
                    tempList.append(newQNode)
                    self.q_table[newQNode] = newQNode.getQ()
                returningNode = self.getMaxQinNodes(tempList)
                self.__lastNode = returningNode
                return returningNode.getOutcome()
            else:
                maxNode = self.getMaxQinNodes(matchingSituations)
                self.__lastNode = maxNode
                return maxNode.getOutcome()
        else:
            tempList = matchingSituations
            if(matchingSituations==None):
                tempList = []
                for poutcome in self.possible_outcomes:
                    newQNode = Q.Q(situation=situation,outcome=poutcome, nodeId=self.lastId)
                    self.lastId+=1
                    self.q_table[newQNode] = newQNode.getQ()
                    tempList.append(newQNode)
            returningNode = tempList[random.choice(self.possible_outcomes)]
            self.__lastNode = returningNode
            return returningNode.getOutcome()
        
    def train(self, reward:int):
        z = self.__lastNode.getQ()
        a = self.learning_rate
        b = reward
        c = self.discount_factor
        d = self.getMaxQinNodes(self.findOrNullQ(self.findClosestState(self.__lastNode.getSituation()))).getQ()
        e = c*d
        updatedQValue = z + (a*(b+e-z))
        self.__lastNode.setQ(updatedQValue)
        self.q_table[self.__lastNode] = self.__lastNode.getQ()

    def findOrNullQ(self, situation: list) -> list|None:
        resultNodes = []
        for qNode in self.q_table:
            if(qNode.getSituation()==situation):
                resultNodes.append(qNode)
        if(resultNodes==[]):
            return None
        else:
            return resultNodes
        
    def getMaxQinNodes(self, nodeList:list) -> Q:
        maxNode = random.choice(list(self.q_table.keys()))
        for qNode in nodeList:
            if(qNode.getOutcome()>maxNode.getOutcome()):
                maxNode = qNode
        return maxNode
    
    def findClosestState(self, situation: list) -> list:
        closestNode = None
        closestNodeDistance = 0
        for qNode in self.q_table:
            tempDistance = self.calculateDistance(qNode.getSituation(),situation)
            if(tempDistance>closestNodeDistance):
                closestNodeDistance = tempDistance
                closestNode = qNode
        return closestNode.getSituation()

    def calculateDistance(self, point1:list, point2: list) -> float:
        squares = []
        for p1 in point1:
            for p2 in point2:
                squares.append((p1-p2)**2)
        squaresSum = sum(squares)
        return math.sqrt(squaresSum)

    def saveModel(self,modelName):
        if os.path.exists(f"{modelName}.xml"):
            os.remove(f"{modelName}.xml")
        root = ET.Element("nodes")
        lastIndex = 0
        saveList = []
        for qNode in self.q_table:
            saveList.append(ET.SubElement(root, "node", id=str(qNode.getID())))
            ET.SubElement(saveList[lastIndex],"situation").text = str(qNode.getSituation())
            ET.SubElement(saveList[lastIndex],"outcome").text = str(qNode.getOutcome())
            ET.SubElement(saveList[lastIndex],"Q").text = str(qNode.getQ())
            lastIndex += 1
        tree = ET.ElementTree(root)
        with open(f"{modelName}.xml","wb") as xml_file:
            tree.write(xml_file, encoding="utf-8", xml_declaration=True)
        print(f"XML file '{modelName}.xml' created successfully!")