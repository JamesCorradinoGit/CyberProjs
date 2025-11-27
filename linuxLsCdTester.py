import tkinter as tk
import random

currentLocal = 0 #0 is root terminal, increased num = deeper in "files"
numDirects = random.randint(3, 6)

class Node: #USE SELF ON ALL INSTANCE METHODS
    def __init__(self, nodeName:str):
        self.nodeName = nodeName
        self.children = []
    
    def addChild(self, name:str):
        self.children.append(name)
    
    def __str__(self):
        return ("Node name: " + self.nodeName + ", Node contents: " + str(self.children))

test = Node("Documents")
test.addChild("goon.txt")
test.addChild("brainrot.txt")
print(test)