import math
import random
import Dice.dice
import Entity.entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import Entity.Abilities as Abilities

class SavingThrowsFrame:

    class Row:

        def __init__(self, label, boolean, checkbox):
            #self.frame = frame
            #self.textVariable = textVariable
            self.label = label
            self.boolean = boolean
            self.checkBox = checkbox

        def getValue(self):
            return self.checkbox
        
        


    def __init__(self, entity, window):
        #Abilities Area
        self.entity = entity
        self.window = LabelFrame(window, text = 'Saving Throws', padx = 10, pady = 10)


        self.rows = []

        

        for i in range(len(Abilities.abilitiesNames)):
            #newFrame = LabelFrame(self.window, text = entityV2.abilitiesNames[i], padx = 10, pady = 10)
            #newFrame.grid(row = i, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)

            
            #text = StringVar()
            #text.set("{} : ({:+})".format(Abilities.abilitiesNames[i], entity.abilities.getSavingThrowModifier(i)))
            label = Label(self.window, text = "{} : ({:+})".format(Abilities.abilitiesNames[i], entity.abilities.getSavingThrowModifier(i)))
            label.grid(row=i, column = 1)
            
            boolVal = IntVar(self.window, 0)
            checkbox = Checkbutton(self.window, variable = boolVal, onvalue = 1, offvalue = 0)
            checkbox.grid(row=i, column = 0)
            
            object = SavingThrowsFrame.Row(label, boolVal, checkbox)
            self.rows.append(object)
        self.updateSheet()


        
    
    def updateEntity(self):
        for i in range(len(self.rows)):
            self.entity.abilities.setProficiency(i, self.rows[i].boolean.get())
            #print(self.rows[i].boolean.get())
            
    def updateSheet(self):
        for i in range(len(self.rows)):
            #self.rows[i].textVariable.set("{} : ({:+})".format(Abilities.abilitiesNames[i], self.entity.abilities.getSavingThrowModifier(i)))
            self.rows[i].label.config(text = "{} : ({:+})".format(Abilities.abilitiesNames[i], self.entity.abilities.getSavingThrowModifier(i)))
            if (self.entity.abilities.getProficiency(i)):
                self.rows[i].checkBox.select()
            else:
                self.rows[i].checkBox.deselect()
            #print(self.rows[i].boolean.get())
                      




    

            
