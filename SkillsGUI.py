import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import Skills

class SkillsFrame:

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
        self.window = LabelFrame(window, text = 'Skills', padx = 10, pady = 10)

        self.rows = []

        

        for i in range(len(Skills.skillsNames)):
            #newFrame = LabelFrame(self.window, text = entityV2.abilitiesNames[i], padx = 10, pady = 10)
            #newFrame.grid(row = i, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)

            
            text = StringVar()
            label = Label(self.window, text = "")
            label.grid(row=i, column = 1)
            
            boolVal = IntVar(self.window, 0)
            checkbox = Checkbutton(self.window, variable = boolVal, onvalue = 1, offvalue = 0)
            checkbox.grid(row=i, column = 0)
            
            object = SkillsFrame.Row(label, text, boolVal, checkbox)
            self.rows.append(object)
        
        self.updateSheet()


                
    
    def updateEntity(self):
        for i in range(len(Skills.skillsNames)):
            self.entity.abilities.skills.setProficiency(i, self.rows[i].boolean.get())
            #print(Skills.skillsNames[i] + " : " + str(self.rows[i].boolean.get()))
        
            
    def updateSheet(self):
        for i in range(len(self.rows)):
            #self.rows[i].textVariable.set("{} : ({:+})".format(Skills.skillsNames[i], self.entity.abilities.skills.getModifier(i)))
            self.rows[i].label.config(text = "{} : ({:+})".format(Skills.skillsNames[i], self.entity.abilities.skills.getModifier(i)))
            if (self.entity.abilities.skills.getProficiency(i)):
                self.rows[i].checkBox.select()
            elif (not self.entity.abilities.skills.getProficiency(i)):
                self.rows[i].checkBox.deselect()