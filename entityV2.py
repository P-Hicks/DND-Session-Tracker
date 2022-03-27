
import math
from tkinter.filedialog import LoadFileDialog, SaveFileDialog
import dice
import pickle
import Skills
import Abilities
import Currency
import HealthAndDamage


version = "2.1"



class Entity:

    def __init__(self, randomize=False, name=None, level = 1, abilityList=None, proficiencyList = None, race=None, type=None, health=None):
        self.level = level
        self.proficiencyBonus = 2 + math.floor(self.level/4)
        self.health = health
        self.max_health = self.health
        """self.race = race
        self.type = type
        self.name = name"""
        self.race = ""
        self.type = ""
        self.name = ""
        if name:
            self.name = name
        self.version = version
        self.alignment = "Neutral"
        self.Class = ""
        self.background = ""
        self.currency = Currency.Currency.create("1gp")

        if (abilityList != None):
            self.abilities = Abilities.Abilities(entity = self, abilityList = abilityList, proficiencyList=proficiencyList)
        else: 
            self.abilities = Abilities.Abilities(entity = self)
        



    def updateStats(self):
        self.proficiencyBonus = 2 + math.floor(self.level/4)
        self.abilities.changeProficiencyBonus(self.proficiencyBonus)

    def levelUp(self):
        self.level += 1

    



    def update_skills(self):
        print()

    def update_saving_throws(self):
        print()

    def new_character(self):
        print()

    def save():
        return 1

    def printSelf():
        return 1
    
    def loadBin(fileName):
        
        
        file = open(fileName + '.dat', 'rb')
        self = pickle.load(file)
        if self.version != version:
            print("Warning! FILE ({}) is outdated and of version {}. Current program is version {}.".format(fileName, self.version, version))
        file.close()
        return self

    def saveBin(self, fileName = None):
        if fileName == None :
            fileName = self.name
        file = open(fileName + '.dat', 'wb')
        pickle.dump(self, file)
        file.close()
        

    def loadFile():
        return 1

    def saveFile():
        return 1





   
        







def codeSnip():
    #list = [['Strength',["Athletics"]],['Dexterity',['Acrobatics', 'Sleight of Hand', 'Stealth']],['Constitution',[]],['Intelligence',['Arcana', 'History', 'Investigation', 'Nature', 'Religion']],['Wisdom',['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival']],['Charisma',['Deception', 'Intimidation', 'Performance', 'Persuasion']]]
    #for abil, thing in list:
    #    for skill in thing:
    #        print("self.{}Proficiency = self.abilities.{}Proficiency".format(skill.lower(), abil.lower()))
    for i in range(len(Skills.skillsNames)):
        print("elif id == {}: \n    if self.{}Proficiency:\n        return self.{} + self.proficiencyBonus\n    else:\n        return self.{}".format(i, Skills.skillsNamesNoSpaces[i], Skills.skillsNamesNoSpaces[i], Skills.skillsNamesNoSpaces[i]), end="\n")

#codeSnip()

# money = Currency(silver = 1.3, platinum = 33.124)
# print(money.toString())
# money.simplify()
# print(money.toString())
# Currency.add(money, Currency.create("1gp, 33cp, 1ep, 6pp"))
# print(money.toString())

#a = Entity(name = "Kyle", health = 27)
#a.saveBin(fileName="trialFileV2.1")

#b = Entity.loadBin("trialFileV2.1")
