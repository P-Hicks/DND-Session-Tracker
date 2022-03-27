import math
import random
from tokenize import Name
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import datetime
import AbilitiesGUI
import SkillsGUI
import SavingThrowsGUI
import NameBarGUI
import CurrencyGUI

class CharSheetWindow:
    def __init__(self, entity):
        self.entity = entity

        self.window = Tk()
        self.window.title(entity.name)

        nameBar = NameBarGUI.NameFrame(entity = entity, window = self.window)
        nameBar.window.grid(row = 0, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10)

        abilities = AbilitiesGUI.AbilityFrame(entity=entity, window=self.window)
        abilities.window.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')
        
        savingThrows = SavingThrowsGUI.SavingThrowsFrame(entity, self.window)
        savingThrows.window.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        savingThrows.updateEntity()

        skills = SkillsGUI.SkillsFrame(entity = entity, window = self.window)
        skills.window.grid(row = 1, column = 1, rowspan = 2, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

        currency = CurrencyGUI.CurrencyFrame(entity = entity, window = self.window)
        currency.window.grid(row = 1, column = 3, rowspan = 2, columnspan = 1, padx = 10, pady = 10, sticky = 'n')
        
        
        self.window.mainloop()





char = entityV2.Entity(name="John", abilityList=[7, 13, 16, 12, 24, 20], proficiencyList=[False, True, False, True, False, True])

#char.abilities.charismaProficiency = True

CharSheetWindow(char)