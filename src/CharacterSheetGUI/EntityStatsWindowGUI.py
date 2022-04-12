import math
import random
import tkinter
import Dice.dice
import Entity.entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import datetime
import CharacterSheetGUI.AbilitiesGUI as AbilitiesGUI
import CharacterSheetGUI.SkillsGUI as SkillsGUI
import CharacterSheetGUI.SavingThrowsGUI as SavingThrowsGUI
import CharacterSheetGUI.NameBarGUI as NameBarGUI
import CharacterSheetGUI.CurrencyGUI as CurrencyGUI
import CharacterSheetGUI.HealthAndDamageGUI as HealthAndDamageGUI
from tkinter.filedialog import asksaveasfile

class CharSheetWindow:
    def __init__(self, entity, row = None):
        self.entity = entity
        self.row = row
        self.window = Tk()
        self.window.title(entity.name)

        self.nameBar = NameBarGUI.NameFrame(entity = entity, window = self.window)
        self.nameBar.window.grid(row = 0, column = 0, rowspan = 1, columnspan = 4, padx = 10, pady = 10)

        self.abilities = AbilitiesGUI.AbilityFrame(entity=entity, window=self.window)
        self.abilities.window.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')
        
        self.savingThrows = SavingThrowsGUI.SavingThrowsFrame(entity, self.window)
        self.savingThrows.window.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        self.savingThrows.updateEntity()

        self.skills = SkillsGUI.SkillsFrame(entity = entity, window = self.window)
        self.skills.window.grid(row = 1, column = 1, rowspan = 2, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        self.currency = CurrencyGUI.CurrencyFrame(entity = entity, window = self.window)
        self.currency.window.grid(row = 2, column = 3, rowspan = 2, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        self.health = HealthAndDamageGUI.HealthFrame(entity = entity, window = self.window)
        self.health.window.grid(row = 1, column = 3, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        self.button = Button(self.window ,text = "Save To File", command=self.saveBin)
        self.button.grid(row = 0, column = 7)
        
        self.button = Button(self.window ,text = "Save Changes", command=self.saveChanges)
        self.button.grid(row = 0, column = 8)

        #self.button = Button(self.window ,text = "Update Sheet", command=self.updateSheet)
        #self.button.grid(row = 0, column = 9)

        self.window.mainloop()

    def saveBin(self):
        files = [('All Files', '*.*')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        #print(file.name)
        self.entity.saveBin(file.name)

    def saveChanges(self):
        self.nameBar.updateEntity()
        self.abilities.updateEntity()
        self.savingThrows.updateEntity()
        self.skills.updateEntity()
        self.currency.updateEntity()
        self.health.updateEntity()
        self.updateSheet()

    def updateSheet(self):
        self.row.update()
        self.nameBar.updateSheet()
        self.abilities.updateSheet()
        self.savingThrows.updateSheet()
        self.skills.updateSheet()
        self.currency.updateSheet()
        self.health.updateSheet()
        if self.row:
            self.row.update()
        





#char = entityV2.Entity(name="John", abilityList=[7, 13, 16, 12, 24, 20], proficiencyList=[False, True, False, True, False, True])

#char.abilities.charismaProficiency = True

#CharSheetWindow(char)