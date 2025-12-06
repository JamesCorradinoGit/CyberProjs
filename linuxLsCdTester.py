import tkinter as tk
import random

termName = "root"

#region tk
rootTk = tk.Tk()
rootTk.config(background="grey8") #TODO finish ui
rootTk.geometry("400x200")

def submitPrompt(event):
    inputtedStr = commandPrompt.get()
    if inputtedStr.startswith("cd"):
        improvImputtedStr = inputtedStr[inputtedStr.find("cd")+3:]
        cdSim(instRootNodes, improvImputtedStr)
    elif inputtedStr.startswith("ls"):
        lsSim(currentNode)
    event.widget.delete(0, tk.END) #TODO check for cd or ls and the input

directNameLabel = tk.Label(rootTk, text=termName, font=("Courier New", 10, "bold"), fg="white", bg="grey8").place(x=15, y=10)
commandPrompt = tk.Entry(rootTk, width=45, bg="grey8", font=("Courier New", 10, "bold"), fg="white", highlightthickness=1, highlightcolor="white", highlightbackground="white", insertbackground="white")
commandPrompt.bind("<Return>", submitPrompt)
commandPrompt.place(x=15, y=33)
#endregion

#region Functionality
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
instRootNodes = createRootNodes()
currentNode = instRootNodes

def createTarget(rootNode:Node): 
    targetToReturn = "root"
    randParentDirect:Node = rootNode.children[random.randint(0,2)]
    targetToReturn += "/"+str(randParentDirect.nodeName)
    
    randChildDirect:Node = randParentDirect.children[random.randint(0, len(randParentDirect.children)-1)]
    targetToReturn += "/"+str(randChildDirect.nodeName)
    return(targetToReturn)

def checkTarget(targetStr:str):
    if termName == targetStr:
        return True
    else:
        return False

def lsSim(nodeToList:Node):
    if type(nodeToList) is Node:
        print(nodeToList.children)
#TODO fix cd to root
def cdSim(rootNode:Node, input:str): #INTENDED TO ONLY USE TWO DIRECTORIES (eg. root/Documents/Homework is the furthest you can go) 
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
#endregion

createTarget(instRootNodes)
rootTk.mainloop()