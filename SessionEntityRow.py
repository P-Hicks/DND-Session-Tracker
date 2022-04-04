import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import EntityStatsWindowGUI
import DamageWindow

class EntityRow:
    def __init__(self, window, entity):
        self.window = window
        self.entity = entity
        self.frame = Frame(window, width= 800)
        self.nameLabel = Label(self.frame, text = "{:20}".format(entity.name))
        self.sheetButton = Button(self.frame, text ="Open", command = self.openChar)
        self.healthLabel = Label(self.frame, text = "{:>4} / {:<4} : ({:>4}%)".format(self.entity.health.currentHP, self.entity.health.maxHP, self.entity.health.realHealthPercentage))
        self.damageButton = Button(self.frame, text ="Do Damage", command = self.doDamage)
        self.effectsButton = Button(self.frame, text ="Effects (?)", command = self.effectsWin)
        self.boolVal = IntVar(self.frame, 0)
        self.checkbox = Checkbutton(self.frame, variable = self.boolVal, onvalue = 1, offvalue = 0)

        self.checkbox.grid(row=0, column = 0)
        self.nameLabel.grid(row = 0, column = 1)
        self.sheetButton.grid(row = 0, column = 2)
        self.healthLabel.grid(row = 0, column = 3)
        self.damageButton.grid(row = 0, column = 4)
        self.effectsButton.grid(row = 0, column = 5)

    def openChar(self):
        self.win = EntityStatsWindowGUI.CharSheetWindow(self.entity, row = self)

    def update(self):
        #print("ROW")
        self.healthLabel.config(text = "{:>4} / {:<4} : ({:>4}%)".format(self.entity.health.currentHP, self.entity.health.maxHP, self.entity.health.realHealthPercentage))
        self.nameLabel.config(text = "{:20}".format(self.entity.name))
        

    def doDamage(self):
        damageWin = DamageWindow.DamageWindow([self.entity], [self])

    def effectsWin(self):
        pass

    def heal(self):
        pass
    
    def checked(self):
        return self.boolVal.get()

    
