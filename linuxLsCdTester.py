import tkinter as tk
import random

currentLocal = 0 #0 is root terminal, increased num = deeper in "files"
innitDirects = {}
numDirectsToInnit = random.randint(3, 6)

randDirectoryList = ["Desktop", "Pictures", "Documents", "Videos", "Downloads", "OS"]

class Node: #USE SELF ON ALL INSTANCE METHODS
    def __init__(self, nodeName:str):
        self.nodeName = nodeName
        self.children = []
    
    def addChild(self, name):
        self.children.append(name)
    
    def __str__(self):
        return ("Node name: " + self.nodeName + ", Node contents: " + str(self.children))
    def __repr__(self):
        return (self.nodeName+"Node")

def indentifyNestedNodes(mainNode:Node):
    for i in range(0, len(mainNode.children)):
        if isinstance(mainNode.children[i],Node):
            print(mainNode.children[i].nodeName)

def startInstance(numDirects:int):
    rootNode = Node("root")
    for i in range(0, numDirects):
        randName = randDirectoryList[i]
        nodeToAdd = Node(randName)
        rootNode.addChild(nodeToAdd)
    print(rootNode)

startInstance(numDirectsToInnit)