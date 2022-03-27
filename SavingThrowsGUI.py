import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import Abilities

class SavingThrowsFrame:

    class Row:

        def __init__(self, label, textVariable, boolean, checkbox):
            #self.frame = frame
            self.textVariable = textVariable
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

            
            text = StringVar()
            text.set("{} : ({:+})".format(Abilities.abilitiesNames[i], entity.abilities.getSavingThrowModifier(i)))
            label = Label(self.window, textvariable = text)
            label.grid(row=i, column = 1)
            
            boolVal = BooleanVar()
            checkbox = Checkbutton(self.window, variable = boolVal, onvalue = True, offvalue = False)
            checkbox.grid(row=i, column = 0)
            
            object = SavingThrowsFrame.Row(label, text, boolVal, checkbox)
            self.rows.append(object)
        self.updateSheet()
    
    def updateEntity(self):
        for i in range(len(self.rows)):
            self.entity.abilities.setProficiency(i, self.rows[i].boolean.get())
            
    def updateSheet(self):
        for i in range(len(self.rows)):
            self.rows[i].textVariable.set("{} : ({:+})".format(Abilities.abilitiesNames[i], self.entity.abilities.getSavingThrowModifier(i)))
            if (self.entity.abilities.proficienciesToArray()[i] and not self.rows[i].boolean.get()):
                self.rows[i].checkBox.select()
            elif (not self.entity.abilities.proficienciesToArray()[i] and self.rows[i].boolean.get()):
                self.rows[i].checkBox.select()
            print(self.rows[i].boolean.get())
                      




    

            
