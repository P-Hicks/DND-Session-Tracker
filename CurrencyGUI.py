import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import Currency

class CurrencyFrame:

    class Row:

        def __init__(self, amountLabel, amountEntry):
            #self.frame = frame
            self.amountLabel = amountLabel
            self.amountEntry = amountEntry
            

        def getValue(self):
            return self.amountEntry.getint()
        
        def changeModifierText(self, string):
            self.modifierText.set(string)
        
        


    def __init__(self, entity, window):
        #Abilities Area
        self.entity = entity
        self.window = LabelFrame(window, text = 'Currency', padx = 10, pady = 10)

        self.labelFrames = []

        
        for i in range(5):
            
            
            amountLabel = Label(self.window, text = '{} Pieces:'.format(Currency.indexToTypeDictionary[i].title()))
            amountEntry = Entry(self.window, width = 3)

            amountLabel.grid(row=i, column = 0)
            amountEntry.grid(row=i, column = 1)
            amountEntry.insert(0, entity.currency.getAmount(i))
            
            object = CurrencyFrame.Row(amountLabel, amountEntry)
            self.labelFrames.append(object)
    
    def updateEntity(self):

        for i in range(len(self.labelFrames)):
            amount = int(self.labelFrames[i].amountEntry.get())
            self.entity.currency.setAmount(i, amount)
    
    def updateSheet(self):
        for i in range(5):
            self.labelFrames[i].amountEntry.delete(0, "end")
            self.labelFrames[i].amountEntry.insert(0, self.entity.currency.getAmount(i))





    

            
