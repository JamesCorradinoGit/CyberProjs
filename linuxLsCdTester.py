import tkinter as tk
import random

currentLocal = 0 #0 is root terminal, increased num = deeper in "files"
numDirects = random.randint(3, 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    
    
    def __str__(self):
        return str(self.data)

test = Node([1,"hi"])
print(test)