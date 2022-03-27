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
        """#Skills
        skills = LabelFrame(entity_win, text = 'Skills', padx = 10, pady = 10)
        skills.grid(row = 3, column = 1, rowspan = 1, columnspan = 1, padx = 10, pady = 10, stick = 'n')
        
        count = 0
        gui_skills_list = []
        #boollist = [] up higher
        for i in entity.skills_list:
            skill_label = Label(skills, text = "{}: ".format(i[0]))
            skill_entry = Entry(skills, width = 3)
            skill_entry.insert(0, "{:+}".format(i[1]))
            skill_label.grid(row=count, column = 1)
            boollist.append(BooleanVar())
            skill_save_checkbox = Checkbutton(skills, variable = boollist[count], onvalue = True, offvalue = False)
            skill_save_checkbox.grid(row=count, column = 0)
            skill_entry.grid(row=count, column=2)
            if i[2] == True:
                skill_save_checkbox.select()
            gui_skills_list.append([skill_save_checkbox, skill_label, boollist[count], skill_entry])
            count += 1"""
        
        
        
        self.entity = entity
        self.window = LabelFrame(window, text = 'Skills', padx = 10, pady = 10)

        self.rows = []

        

        for i in range(len(Skills.skillsNames)):
            #newFrame = LabelFrame(self.window, text = entityV2.abilitiesNames[i], padx = 10, pady = 10)
            #newFrame.grid(row = i, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)

            
            text = StringVar()
            label = Label(self.window, textvariable = text)
            label.grid(row=i, column = 1)
            
            boolVal = BooleanVar()
            checkbox = Checkbutton(self.window, variable = boolVal, onvalue = True, offvalue = False)
            checkbox.grid(row=i, column = 0)
            
            object = SkillsFrame.Row(label, text, boolVal, checkbox)
            self.rows.append(object)
        
        self.updateSheet()
    
    def updateEntity(self):
        for i in range(len(Skills.skillsNames)):
            self.entity.abilities.skills.setProficiency(self.rows[i].boolean.get())
            
    def updateSheet(self):
        for i in range(len(self.rows)):
            self.rows[i].textVariable.set("{} : ({:+})".format(Skills.skillsNames[i], self.entity.abilities.skills.getModifier(i)))
            if (self.entity.abilities.skills.getProficiency(i) and not self.rows[i].boolean.get()):
                self.rows[i].checkbox.select()
            elif (not self.entity.abilities.skills.getProficiency(i) and self.rows[i].boolean.get()):
                self.rows[i].checkbox.select()
                      
