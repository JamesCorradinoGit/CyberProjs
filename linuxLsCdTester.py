import tkinter as tk
import random

innitDirects = {}
numDirectsToInnit = random.randint(2, 3)

docDirectNameList = ["a","b","c","d","e","f","g"] 
imagDirectNameList = []
vidDirectNameList = []
# ^THESE ARE NOT FILE NAMES!! THESE ARE FOLDER-ESQ NAMES

class Node: #USE SELF ON ALL INSTANCE METHODS
    def __init__(self, nodeName:str):
        self.nodeName = nodeName
        self.children = []
        self.treePos = 0
    
    def setTreePos(self, num:int):
        self.treePos = num

    def addChildren(self, dat):
        self.children.extend(dat)

    def checkForNodeChild(self):
        for i in range(0, len(self.children)):
            if isinstance(self.children[i], Node):
                print(self.children[i].nodeName)
                
    def findChild(self, targetChildName):
        for i in range(0, len(self.children)):
            if self.children[i].nodeName == targetChildName:
                return self.children[i]
    
    def __str__(self):
        return ("Node name: " + self.nodeName + ", Node contents: " + str(self.children))
    def __repr__(self):
        return (self.nodeName+"Node")

def populateNode(nodeToAddD:Node, directList:list, numNodesToAdd):
    tempAddList = []
    for i in range(0, numNodesToAdd):
        tempAddList.append(directList[i])
    nodeToAddD.addChildren(tempAddList)

def createRootNodes():
    rootNode = Node("root")
    tempNodes = [Node("Documents"), Node("Pictures"), Node("Videos")]
    rootNode.addChildren(tempNodes)
    return rootNode

instRootNodes = createRootNodes()
populateNode(instRootNodes.findChild("Documents"), docDirectNameList, 2)
print(instRootNodes.findChild("Documents"))