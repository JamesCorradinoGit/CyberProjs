import tkinter as tk
import random

#region Nodes
class Node: #USE SELF ON ALL INSTANCE METHODS
    def __init__(self, nodeName:str):
        self.nodeName = nodeName
        self.children = []
        self.treePos = 0
    
    def setTreePos(self, num:int):
        self.treePos = num

    def addChildren(self, dat):
        self.children.extend(dat)

    def checkForChild(self, targetChildName):
        for i in range(0, len(self.children)):
            if self.children[i].nodeName == targetChildName:
                return True
            else:
                return False
                
    def getChild(self, targetChildName): #optimize with index command?
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
        tempAddList.append(Node(directList[i]))
    nodeToAddD.addChildren(tempAddList)

def createRootNodes():
    rootNode = Node("root")
    tempNodes = [Node("Documents"), Node("Pictures"), Node("Videos")]
    rootNode.addChildren(tempNodes)

    docDirectNameList = ["Homework","Worksheets","VisualStudio","GoogleDocs","MicrosoftWord","CipherKit"]
    imagDirectNameList = ["GraduationPhotos", "Screenshots", "MobilePictures", "SlideshowAssets", "StockImages", "GIFs"] 
    vidDirectNameList = ["n", "o", "p", "q", "r", "s"]
    # ^THESE ARE NOT FILE NAMES!! THESE ARE FOLDER-ESQ NAMES

    populateNode(rootNode.getChild("Documents"), docDirectNameList, random.randint(2,6))
    populateNode(rootNode.getChild("Pictures"), imagDirectNameList, random.randint(2,6))
    populateNode(rootNode.getChild("Videos"), vidDirectNameList, random.randint(2,6))
    return rootNode
#endregion

termName = "root"
instRootNodes = createRootNodes()
currentNode = instRootNodes

def lsSim(nodeToList:Node):
    print(nodeToList.children)

def cdSim(rootNode:Node, input:str):
    global termName
    global currentNode
    tempTermName = ""
    if input == "..":
        nodeStrToRemove = termName[termName.rfind("/"):]
        tempTermName = termName.removesuffix(nodeStrToRemove)
        currentStrToRemove = termName[termName.find("/")+1:termName.rfind("/"):]
        currentNode = rootNode.getChild(currentStrToRemove)
        
        termName = tempTermName
    elif currentNode.checkForChild(input):
        tempTermName = termName + "/"+input
        currentNode = currentNode.getChild(input)
        
        termName = tempTermName
    else:
        print("Please route to a valid directory.")

cdSim(instRootNodes, "Documents")
lsSim(currentNode)
cdSim(instRootNodes, "Homework")
cdSim(instRootNodes, "..")
print(termName)