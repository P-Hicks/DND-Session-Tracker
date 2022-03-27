import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog


class NameFrame:
    
    def __init__(self, entity, window):
        
        #TOP ROW
        self.window = LabelFrame(window, text = 'Name & Such', padx = 10, pady = 10)
        self.window.grid(row = 0, column = 0, rowspan = 1, columnspan = 3, padx = 10, pady = 10)

        self.nameLabel = Label(self.window, text = 'Name:')
        self.nameEntry = Entry(self.window)
        self.classLabel = Label(self.window, text = 'Class:')
        self.classEntry = Entry(self.window)
        self.levelLabel = Label(self.window, text = 'Level:')
        self.levelEntry = Entry(self.window)
        self.backgroundLabel = Label(self.window, text = 'Background:')
        self.backgroundEntry = Entry(self.window)
        self.raceLabel = Label(self.window, text = 'Race:')
        self.raceEntry = Entry(self.window)
        self.alignmentLabel = Label(self.window, text = 'Alignment:')
        self.alignmentEntry = Entry(self.window)

        self.nameLabel.grid(row=0, column = 0)
        self.nameEntry.grid(row=0, column = 1)
        self.nameEntry.insert(0, entity.name)
        
        self.classLabel.grid(row=1, column = 0)
        self.classEntry.grid(row=1, column = 1)
        self.classEntry.insert(0, entity.Class)
        
        self.levelLabel.grid(row=0, column = 2)
        self.levelEntry.grid(row=0, column = 3)
        self.levelEntry.insert(0, entity.level)
        
        self.backgroundLabel.grid(row=1, column = 2)
        self.backgroundEntry.grid(row=1, column = 3)
        self.backgroundEntry.insert(0, entity.background)
        
        self.raceLabel.grid(row=0, column = 4)
        self.raceEntry.grid(row=0, column = 5)
        self.raceEntry.insert(0, entity.race)
        
        self.alignmentLabel.grid(row=1, column = 4)
        self.alignmentEntry.grid(row=1, column = 5)
        self.alignmentEntry.insert(0, entity.alignment)

    
    def updateEntity(self):
        self.entity.name = self.nameEntry.get()
        self.entity.race = self.raceEntry.get()
        self.entity.background = self.backgroundEntry.get()
        self.entity.alignment = self.alignmentEntry.get()
        self.entity.Class = self.classEntry.get()
        self.entity.level = self.levelEntry.get()
    
    def updateSheet(self):
        self.nameEntry.insert(0, self.entity.name)
        self.raceEntry.insert(0, self.entity.race)
        self.backgroundEntry.insert(0, self.entity.background)
        self.alignmentEntry.insert(0, self.entity.alignment)
        self.classEntry.insert(0, self.entity.Class)
        self.levelEntry.insert(0, self.entity.level)







    

            
