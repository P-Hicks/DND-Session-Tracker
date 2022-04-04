import math
import random
import dice
import entityV2
import pickle
from tkinter import *
import HealthAndDamage


class HealthFrame:
    
    def __init__(self, entity, window):
        self.entity = entity
        #TOP ROW
        self.window = LabelFrame(window, text = 'Health & Such', padx = 10, pady = 10)
        

        self.currentHPEntry = Entry(self.window, width = 5)
        self.currentHPEntry.insert(0, (entity.health.currentHP))
        self.maxHPEntry = Entry(self.window, width = 5)
        self.maxHPEntry.insert(0, entity.health.maxHP)
        self.currentHPLabel = Label(self.window, text = 'Current HP:')
        self.maxHPLabel = Label(self.window, text = 'Max HP:')
        self.healthPercentageLabel = Label(self.window, text = 'HP % : {}'.format(self.entity.health.realHealthPercentage))
         
        self.hitDiceLabel = Label(self.window, text = 'Hit Dice:')
        self.hitDiceEntry = Entry(self.window, width = 6)
        self.hitDiceEntry.insert(0, entity.health.hitDice)
        self.hitDiceAmountEntry = Entry(self.window, width = 3)
        self.hitDiceAmountEntry.insert(0, entity.health.hitDiceCount)
        self.hitDiceTotalEntry = Entry(self.window, width = 3)
        self.hitDiceTotalEntry.insert(0, entity.health.maxHitDiceCount)


        self.currentHPLabel.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.maxHPLabel.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.currentHPEntry.grid(row = 0, column = 1, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.maxHPEntry.grid(row = 1, column = 1, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.healthPercentageLabel.grid(row = 0, column = 2, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.hitDiceLabel.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.hitDiceEntry.grid(row = 2, column = 3, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.hitDiceAmountEntry.grid(row = 2, column = 1, rowspan = 1, columnspan = 1, padx = 0, pady = 10)
        self.hitDiceTotalEntry.grid(row = 2, column = 2, rowspan = 1, columnspan = 1, padx = 0, pady = 10)

        self.deathSavesFrame = LabelFrame(self.window, text = 'Death Saves', padx = 10, pady = 10)
        self.deathSavesFrame.grid(row = 3, column = 0, rowspan = 1, columnspan = 3, padx = 0, pady = 10)



        self.deathSavesFailuresLabel = Label(self.deathSavesFrame, text = 'Failures:')
        self.deathSavesSuccessesLabel = Label(self.deathSavesFrame, text = 'Successes:')

        self.deathSavesFailuresLabel.grid(row = 1, column = 0, rowspan = 1, columnspan = 1)
        self.deathSavesSuccessesLabel.grid(row = 0, column = 0, rowspan = 1, columnspan = 1)

        self.deathSavesFailuresVarList = []
        self.deathSavesSuccessesVarList = []
        self.deathSavesSuccessesBoxes = []
        self.deathSavesFailuresBoxes = []

        for i in range(3):
            varSuccess = IntVar(self.window, 0)
            varFailure = IntVar(self.window, 0)
            successBox = Checkbutton(self.deathSavesFrame, variable=varSuccess, onvalue = 1, offvalue = 0)
            successBox.grid(row=0, column = i + 1, sticky=W)
            failureBox = Checkbutton(self.deathSavesFrame, variable=varFailure, onvalue = 1, offvalue = 0)
            failureBox.grid(row=1, column = i + 1, sticky=W)

            self.deathSavesFailuresVarList.append(varFailure)
            self.deathSavesSuccessesVarList.append(varSuccess)
            self.deathSavesSuccessesBoxes.append(successBox)
            self.deathSavesFailuresBoxes.append(failureBox)
            

        self.updateDeathSavesGUI()


    def updateDeathSavesGUI(self):

        deathSavesSuccessess = self.entity.health.deathSavesSuccesses
        deathSavesFailures = self.entity.health.deathSavesFailures

        for i in range(3):
            if deathSavesSuccessess >= i+1:
                self.deathSavesSuccessesBoxes[i].select()
            else: 
                self.deathSavesSuccessesBoxes[i].deselect()
            
            if deathSavesFailures >= i+1:
                self.deathSavesFailuresBoxes[i].select()
            else: 
                self.deathSavesFailuresBoxes[i].deselect()
        


    def updateDeathSavesData(self):

        deathSavesSuccesses = 0
        deathSavesFailures = 0

        for i in range(3):
            print(self.deathSavesFailuresVarList[i].get())
            if self.deathSavesFailuresVarList[i].get():
                deathSavesFailures += 1
            if self.deathSavesSuccessesVarList[i].get():
                deathSavesSuccesses += 1
        
        self.entity.health.deathSavesSuccesses = deathSavesSuccesses
        self.entity.health.deathSavesFailures = deathSavesFailures
        # print("{} {}".format(deathSavesFailures, deathSavesSuccesses))

    def updateEntity(self):
        self.updateDeathSavesData() 
        self.entity.health.hitDice = self.hitDiceEntry.get()
        self.entity.health.hitDiceCount =int(self.hitDiceAmountEntry.get())
        self.entity.health.maxHitDiceCount =int(self.hitDiceTotalEntry.get())
        self.entity.health.maxHP = int(self.maxHPEntry.get())
        self.entity.health.currentHP = int(self.currentHPEntry.get())
        self.entity.health.updateHealth()

    def updateSheet(self):
        
        self.currentHPEntry.delete(0, "end")
        self.maxHPEntry.delete(0, "end")
         
        self.hitDiceEntry.delete(0, "end")
        self.hitDiceAmountEntry.delete(0, "end")
        self.hitDiceTotalEntry.delete(0, "end")


        self.updateDeathSavesGUI()
        #print("HEalth Sheet Updated")
        self.currentHPEntry.insert(0, self.entity.health.currentHP)
        self.maxHPEntry.insert(0, self.entity.health.maxHP)
         
        self.hitDiceEntry.insert(0, self.entity.health.hitDice)
        self.hitDiceAmountEntry.insert(0, self.entity.health.hitDiceCount)
        self.hitDiceTotalEntry.insert(0, self.entity.health.maxHitDiceCount)
        self.healthPercentageLabel.config(text=('HP % : {}'.format(self.entity.health.realHealthPercentage)))
    






    

            
