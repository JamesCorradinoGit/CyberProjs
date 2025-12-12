import tkinter as tk
import random

termName = "root"
score = 0
currentTargetStr = ""

#region tk
rootTk = tk.Tk()
rootTk.config(background="grey8") 
rootTk.geometry("400x200")
rootTk.resizable(False, False)

def outputText(inputText, colStyle):
    outputField.delete("1.0", tk.END)
    outputField.insert(tk.END, inputText+"\n", colStyle)
def submitPrompt(event):
    inputtedStr = commandPrompt.get()
    if inputtedStr.startswith("@"):
        adminCmds(inputtedStr)
    elif inputtedStr.startswith("cd"):
        improvImputtedStr = inputtedStr[inputtedStr.find("cd")+3:]
        cdSim(instRootNodes, improvImputtedStr)
    elif inputtedStr.startswith("ls"):
        lsSim(currentNode)
    elif inputtedStr.lower() == "check":
        checkTarget(currentTargetStr)
    else:
        outputText("ERROR: Not a valid command.", "ErrorText")
    event.widget.delete(0, tk.END)

directNameLabel = tk.Label(rootTk, text=termName, font=("Courier New", 10, "bold"), fg="white", bg="grey8")
directNameLabel.place(x=15, y=10)
def updateMainLabel():
    directNameLabel.config(text=termName)

tk.Label(rootTk, text="Output:", font=("Courier New", 10, "bold"), fg="white", bg="grey8").place(x=15, y=60)
outputField = tk.Text(width=45, height= 6, font=("Courier New", 10, "bold"), fg="white", bg="grey8", highlightthickness=1, highlightcolor="white", highlightbackground="white", insertbackground="white")
outputField.bind("<Key>", lambda breakieBreaker: "break")

outputField.tag_config("ErrorText", foreground="red")
outputField.tag_config("CheckText", foreground="DeepSkyBlue2")

outputField.place(x=15, y=85)

commandPrompt = tk.Entry(rootTk, width=45, bg="grey8", font=("Courier New", 10, "bold"), fg="white", highlightthickness=1, highlightcolor="white", highlightbackground="white", insertbackground="white")
commandPrompt.bind("<Return>", submitPrompt)
commandPrompt.place(x=15, y=33)
#endregion

#region cdlsFunctionality
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
        return (self.nodeName)

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
    imagDirectNameList = ["GradPhotos", "Screenshots", "MobilePictures", "SlideshowAssets", "StockImages", "GIFs"] 
    vidDirectNameList = ["Captures", "NVIDIA", "gallery", "Games", "Replays", "Saves"]
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
    global score
    if termName == targetStr:
        score += 1
        outputText("Correct!", "CheckText")
        updateScore()
        updateTarget()
        return True
    else:
        outputText("Wrong! Try again!", "CheckText")
        return False

def lsSim(nodeToList:Node):
    if type(nodeToList) is Node:
        outputText(str(nodeToList.children)+"\n", "")
def cdSim(rootNode:Node, input:str): #INTENDED TO ONLY USE TWO DIRECTORIES (eg. root/Documents/Homework is the furthest you can go) 
    global termName
    global currentNode
    if currentNode == instRootNodes and input == "..":
        outputText("ERROR: You cannot go past the root.\n", "ErrorText")
    else:
        tempTermName = ""
        if input == "..":
            nodeStrToRemove = termName[termName.rfind("/"):]
            tempTermName = termName.removesuffix(nodeStrToRemove)
            currentStrToRemove = termName[termName.find("/")+1:termName.rfind("/"):]
            if tempTermName == "root":
                currentNode = instRootNodes
            else:
                currentNode = rootNode.getChild(currentStrToRemove)
            termName = tempTermName
            updateMainLabel()
        elif currentNode.checkForChild(input):
            tempTermName = termName + "/"+input
            currentNode = currentNode.getChild(input)
            
            termName = tempTermName
            updateMainLabel()
        else:
            outputText("ERROR: Please route to a valid directory.\n", "ErrorText")

#endregion

#region gameFunctionality&tk
targetLabel = tk.Label(rootTk, text="TARGET DIRECTORY", font=("Courier New", 10, "bold"), fg="DeepSkyBlue2", bg="grey8")
scoreLabel = tk.Label(rootTk, text="Score: "+str(score), font=("Courier New", 10, "bold"), fg="DeepSkyBlue2", bg="grey8")

def gameReset():
    global currentNode, score, instRootNodes, termName
    termName = "root"
    targetLabel.config(text="TARGET DIRECTORY")
    currentNode = instRootNodes
    updateMainLabel()
    instRootNodes = createRootNodes()
    targetLabel.place_forget()
    scoreLabel.place_forget()
    resetScore()
    createTarget(instRootNodes)
def updateTarget():
    global instRootNodes, currentTargetStr
    trgt = createTarget(instRootNodes)
    targetLabel.config(text=trgt)
    currentTargetStr = trgt
def startGame():
    targetLabel.place(x=75, y=60)
    scoreLabel.place(x=310, y=60)
    updateTarget()
def resetScore():
    global score
    score = 0
def updateScore():
    scoreLabel.config(text="Score: "+str(score))

def adminCmds(input:str):
    improvImputtedStr = input[input.find("@")+1:].replace(" ","")
    if improvImputtedStr == "reset":
        gameReset()
    elif improvImputtedStr == "start":
        startGame()
    elif improvImputtedStr == "resetscore":
        resetScore()
#endregion

rootTk.mainloop()