import entityV2
import Abilities


skillsNames = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                             'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
                             'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

skillsNamesNoSpaces = ['acrobatics', 'animalHandling', 'arcana', 'athletics', 'deception', 'history', 'Insight',
                             'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion',
                             'religion', 'sleightOfHand', 'stealth', 'survival']

skillsDictionary = {
    'Acrobatics' : 0, 
    'Animal Handling' : 1, 
    'Arcana' : 2, 
    'Athletics' : 3, 
    'Deception' : 4, 
    'History' : 5, 
    'Insight' : 6,
    'Intimidation' : 7, 
    'Investigation' : 8, 
    'Medicine' : 9, 
    'Nature' : 10, 
    'Perception' : 11, 
    'Performance' : 12, 
    'Persuasion' : 13,
    'Religion' : 14, 
    'Sleight of Hand'  : 15, 
    'Stealth'  : 16, 
    'Survival' : 17
}


    
    
class Skills:
    
    def __init__(self, abilities, profiencyBonus = 1):
        self.proficiencyBonus = profiencyBonus
        self.abilities = abilities
        self.exceptions = []
        self.updateSkills()
    
        self.acrobaticsProficiency = False
        self.animalHandlingProficiency = False
        self.arcanaProficiency = False
        self.athleticsProficiency = False
        self.deceptionProficiency = False
        self.historyProficiency = False
        self.insightProficiency = False
        self.intimidationProficiency = False
        self.investigationProficiency = False
        self.medicineProficiency = False
        self.natureProficiency = False
        self.perceptionProficiency = False
        self.performanceProficiency = False
        self.persuasionProficiency = False
        self.religionProficiency = False
        self.sleightOfHandProficiency = False
        self.stealthProficiency = False
        self.survivalProficiency = False

    def changeProficiencyBonus(self, bonus):
        self.proficiencyBonus = bonus

    def passiveCheck(self, skill):
        return 10 + self.checkModifier(skill)

    def getProficiency(self, skill):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        if (id == 0):
            return self.acrobaticsProficiency
        elif (id == 1):
            return self.animalHandlingProficiency
        elif (id == 2):
            return self.arcanaProficiency
        elif (id == 3):
            return self.athleticsProficiency
        elif (id == 4):
            return self.deceptionProficiency
        elif (id == 5):
            return self.historyProficiency
        elif (id == 6):
            return self.insightProficiency
        elif (id == 7):
            return self.intimidationProficiency
        elif (id == 8):
            return self.investigationProficiency
        elif (id == 9):
            return self.medicineProficiency
        elif (id == 10):
            return self.natureProficiency
        elif (id == 11):
            return self.perceptionProficiency
        elif (id == 12):
            return self.performanceProficiency
        elif (id == 13):
            return self.persuasionProficiency
        elif (id == 14):
            return self.religionProficiency
        elif (id == 15):
            return self.sleightOfHandProficiency
        elif (id == 16):
            return self.stealthProficiency
        elif (id == 17):
            return self.survivalProficiency

    def changeProficiency(self, skill, boolean):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        if (id == 0):
            self.acrobaticsProficiency = boolean
        elif (id == 1):
            self.animalHandlingProficiency = boolean
        elif (id == 2):
             self.arcanaProficiency = boolean
        elif (id == 3):
            self.athleticsProficiency = boolean
        elif (id == 4):
            self.deceptionProficiency = boolean
        elif (id == 5):
            self.historyProficiency = boolean
        elif (id == 6):
            self.insightProficiency = boolean
        elif (id == 7):
            self.intimidationProficiency = boolean
        elif (id == 8):
            self.investigationProficiency = boolean
        elif (id == 9):
            self.medicineProficiency = boolean
        elif (id == 10):
            self.natureProficiency = boolean
        elif (id == 11):
            self.perceptionProficiency = boolean
        elif (id == 12):
            self.performanceProficiency = boolean
        elif (id == 13):
            self.persuasionProficiency = boolean
        elif (id == 14):
            self.religionProficiency = boolean
        elif (id == 15):
            self.sleightOfHandProficiency = boolean
        elif (id == 16):
            self.stealthProficiency = boolean
        elif (id == 17):
            self.survivalProficiency = boolean

    def getModifier(self, skill):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        if id == 0: 
            if self.acrobaticsProficiency:
                return self.acrobatics + self.proficiencyBonus
            else:
                return self.acrobatics
        elif id == 1: 
            if self.animalHandlingProficiency:
                return self.animalHandling + self.proficiencyBonus
            else:
                return self.animalHandling
        elif id == 2: 
            if self.arcanaProficiency:
                return self.arcana + self.proficiencyBonus
            else:
                return self.arcana
        elif id == 3: 
            if self.athleticsProficiency:
                return self.athletics + self.proficiencyBonus
            else:
                return self.athletics
        elif id == 4: 
            if self.deceptionProficiency:
                return self.deception + self.proficiencyBonus
            else:
                return self.deception
        elif id == 5: 
            if self.historyProficiency:
                return self.history + self.proficiencyBonus
            else:
                return self.history
        elif id == 6: 
            if self.insightProficiency:
                return self.insight + self.proficiencyBonus
            else:
                return self.insight
        elif id == 7: 
            if self.intimidationProficiency:
                return self.intimidation + self.proficiencyBonus
            else:
                return self.intimidation
        elif id == 8: 
            if self.investigationProficiency:
                return self.investigation + self.proficiencyBonus
            else:
                return self.investigation
        elif id == 9: 
            if self.medicineProficiency:
                return self.medicine + self.proficiencyBonus
            else:
                return self.medicine
        elif id == 10: 
            if self.natureProficiency:
                return self.nature + self.proficiencyBonus
            else:
                return self.nature
        elif id == 11: 
            if self.perceptionProficiency:
                return self.perception + self.proficiencyBonus
            else:
                return self.perception
        elif id == 12: 
            if self.performanceProficiency:
                return self.performance + self.proficiencyBonus
            else:
                return self.performance
        elif id == 13: 
            if self.persuasionProficiency:
                return self.persuasion + self.proficiencyBonus
            else:
                return self.persuasion
        elif id == 14: 
            if self.religionProficiency:
                return self.religion + self.proficiencyBonus
            else:
                return self.religion
        elif id == 15: 
            if self.sleightOfHandProficiency:
                return self.sleightOfHand + self.proficiencyBonus
            else:
                return self.sleightOfHand
        elif id == 16: 
            if self.stealthProficiency:
                return self.stealth + self.proficiencyBonus
            else:
                return self.stealth
        elif id == 17: 
            if self.survivalProficiency:
                return self.survival + self.proficiencyBonus
            else:
                return self.survival


    def updateSkills(self):
        self.athletics = self.abilities.strengthModifier
        self.acrobatics = self.abilities.dexterityModifier
        self.sleightOfHand = self.abilities.dexterityModifier
        self.stealth = self.abilities.dexterityModifier
        self.arcana = self.abilities.intelligenceModifier
        self.history = self.abilities.intelligenceModifier
        self.investigation = self.abilities.intelligenceModifier
        self.nature = self.abilities.intelligenceModifier
        self.religion = self.abilities.intelligenceModifier
        self.animalHandling = self.abilities.wisdomModifier
        self.insight = self.abilities.wisdomModifier
        self.medicine = self.abilities.wisdomModifier
        self.perception = self.abilities.wisdomModifier
        self.survival = self.abilities.wisdomModifier
        self.deception = self.abilities.charismaModifier
        self.intimidation = self.abilities.charismaModifier
        self.performance = self.abilities.charismaModifier
        self.persuasion = self.abilities.charismaModifier

       
        


    class Exception:

        def __init__(self, index, value):
            self.index = index
            self.value = value





