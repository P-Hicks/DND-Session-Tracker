import Skills
import entityV2

abilitiesNames = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"]

abilitiesDictionary =  {"Strength" : 0,
                        "Dexterity" : 1, 
                        "Constitution" : 2, 
                        "Wisdom" : 3, 
                        "Intelligence" : 4, 
                        "Charisma" : 5}

class Abilities:

    def __init__(self, entity = None, strength = 10, strengthProficiency=False, dexterity = 10, dexterityProficiency = False, constitution = 10, constitutionProficiency = False, intelligence = 10, intelligenceProficiency = False, wisdom = 10, wisdomProficiency = False, charisma = 10, charismaProficiency = False, abilityList = None, proficiencyList = None):
        self.entity = entity

        

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        if (abilityList != None):
            for i in range(len(abilityList)):
                self.setScore(i, abilityList[i])

        self.updateAbilityModifiers()

        self.strengthProficiency = strengthProficiency
        self.dexterityProficiency = dexterityProficiency
        self.constitutionProficiency = constitutionProficiency
        self.intelligenceProficiency = intelligenceProficiency
        self.wisdomProficiency = wisdomProficiency
        self.charismaProficiency = charismaProficiency
        
        if (proficiencyList != None):
            for i in range(len(proficiencyList)):
                self.setProficiency(i, proficiencyList[i])

        self.proficiencyBonus = entity.proficiencyBonus
        self.skills = Skills.Skills(self, self.proficiencyBonus)

    def scoresToArray(self):
        return [self.strength, self.dexterity, self.constitution,  self.wisdom, self.intelligence, self.charisma]

    def proficienciesToArray(self):
        return [self.strengthProficiency, self.dexterityProficiency, self.constitutionProficiency,  self.wisdomProficiency, self.intelligenceProficiency, self.charismaProficiency]
    
    def passiveCheck(self, ability):
        return 10 + self.checkModifier(ability)

    def getModifier(self, ability):
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability
        
        if (id == 0):
            return self.strengthModifier
        elif (id == 1):
            return self.dexterityModifier
        elif (id == 2):
            return self.constitutionModifier
        elif (id == 3):
            return self.wisdomModifier
        elif (id == 4):
            return self.intelligenceModifier
        elif (id == 5):
            return self.charismaModifier

    def getProficiency(self, ability):
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability
        
        if (id == 0):
            return self.strengthProficiency
        elif (id == 1):
            return self.dexterityProficiency
        elif (id == 2):
            return self.constitutionProficiency
        elif (id == 3):
            return self.wisdomProficiency
        elif (id == 4):
            return self.intelligenceProficiency
        elif (id == 5):
            return self.charismaProficiency

    def getSavingThrowModifier(self, ability):
        
        
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability

        if (id == 0):
            return self.strengthModifier + self.strengthProficiency * self.proficiencyBonus
        elif (id == 1):
            return self.dexterityModifier + self.dexterityProficiency * self.proficiencyBonus
        elif (id == 2):
            return self.constitutionModifier + self.constitutionProficiency * self.proficiencyBonus
        elif (id == 3):
            return self.wisdomModifier + self.wisdomProficiency * self.proficiencyBonus
        elif (id == 4):
            return self.intelligenceModifier + self.intelligenceProficiency * self.proficiencyBonus
        elif (id == 5):
            return self.charismaModifier + self.charismaProficiency * self.proficiencyBonus

    def getScore(self, ability):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            if (id == 0):
                return self.strength
            elif (id == 1):
                return self.dexterity
            elif (id == 2):
                return self.constitution
            elif (id == 3):
                return self.wisdom
            elif (id == 4):
                return self.intelligence
            elif (id == 5):
                return self.charisma

    def setScore(self, ability, score):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            if (id == 0):
                self.strength = score
            elif (id == 1):
                self.dexterity = score
            elif (id == 2):
                self.constitution = score
            elif (id == 3):
                self.wisdom = score
            elif (id == 4):
                self.intelligence = score
            elif (id == 5):
                self.charisma = score

    def setProficiency(self, ability, proficiency):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            if (id == 0):
                self.strengthProficiency = proficiency
            elif (id == 1):
                self.dexterityProficiency = proficiency
            elif (id == 2):
                self.constitutionProficiency = proficiency
            elif (id == 3):
                self.wisdomProficiency = proficiency
            elif (id == 4):
                self.intelligenceProficiency = proficiency
            elif (id == 5):
                self.charismaProficiency = proficiency

    def randomGen():
        a = Abilities()
        return a

    def updateAbilityModifiers(self):
        self.strengthModifier = int((self.strength-10)/2)
        self.dexterityModifier = int((self.dexterity-10)/2)
        self.constitutionModifier = int((self.constitution-10)/2)
        self.intelligenceModifier = int((self.intelligence-10)/2)
        self.wisdomModifier = int((self.wisdom-10)/2)
        self.charismaModifier = int((self.charisma-10)/2)

    def changeProficiencyBonus(self):
        self.proficiencyBonus = self.entity.proficiencyBonus
        self.skills.changeProficiencyBonus(self.entity.proficiencyBonus)
