import math
import random
import Dice.dice as Dice
import Entity
import Entity.entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import Entity.Abilities as Abilities

class AbilityFrame:

    class Row:

        def __init__(self, scoreLabel, modifierLabel, modifierText, scoreEntry):
            #self.frame = frame
            self.scoreLabel = scoreLabel
            self.modifierLabel = modifierLabel
            self.scoreEntry = scoreEntry
            self.modifierText = modifierText

        def getValue(self):
            return self.scoreEntry.getint()
        
        def changeModifierText(self, string):
            self.modifierText.set(string)
        
        


    def __init__(self, entity, window):
        #Abilities Area
        self.entity = entity
        self.window = LabelFrame(window, text = 'Abilities', padx = 10, pady = 10)

        self.labelFrames = []

        

        for i in range(len(Abilities.abilitiesNames)):
            #newFrame = LabelFrame(self.window, text = entityV2.abilitiesNames[i], padx = 10, pady = 10)
            #newFrame.grid(row = i, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)

            text = StringVar()
            text.set("({:+})".format(self.entity.abilities.getModifier(i)))

            modifierLabel = Label(self.window, textvariable = text)
            scoreLabel = Label(self.window, text = '{} Score:'.format(Abilities.abilitiesNames[i]))
            scoreEntry = Entry(self.window, width = 3)

            scoreLabel.grid(row=i, column = 0)
            scoreEntry.grid(row=i, column = 1)
            scoreEntry.insert(0, entity.abilities.getScore(i))
            modifierLabel.grid(row=i, column = 2)
            
            object = AbilityFrame.Row(scoreLabel, modifierLabel, text, scoreEntry)
            self.labelFrames.append(object)
    
    def updateEntity(self):

        for i in range(len(self.labelFrames)):
            score = int(self.labelFrames[i].scoreEntry.get())
            self.entity.abilities.setScore(i, score)
        self.entity.abilities.update()
        
    
    def updateSheet(self):
        for i in range(len(self.labelFrames)):
            self.labelFrames[i].scoreEntry.delete(0, "end")
            self.labelFrames[i].scoreEntry.insert(0, self.entity.abilities.getScore(i))
            self.labelFrames[i].changeModifierText("({:+})".format(self.entity.abilities.getModifier(i)))





    

            
