import Entity.Skills as Skills
import Entity.entityV2

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

        self.abiilityScores = [strength, dexterity, constitution, 
                                wisdom, intelligence, charisma]
        
        self.proficiences = [strengthProficiency, dexterityProficiency, constitutionProficiency,  
                            wisdomProficiency, intelligenceProficiency, charismaProficiency]

        if (abilityList != None):
            for i in range(len(abilityList)):
                self.setScore(i, abilityList[i])

        self.updateAbilityModifiers()
   
        if (proficiencyList != None):
            for i in range(len(proficiencyList)):
                self.setProficiency(i, proficiencyList[i])

        self.proficiencyBonus = entity.proficiencyBonus
        self.skills = Skills.Skills(self, self.proficiencyBonus)

    def scoresToArray(self):
        return self.abiilityScores
    def proficienciesToArray(self):
        return self.proficiences

    def passiveCheck(self, ability):
        return 10 + self.checkModifier(ability)

    def getModifier(self, ability):
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability
        
        return self.abilityModifiers[id]

    def getProficiency(self, ability):
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability
        
        return self.proficiences[id]

    def getSavingThrowModifier(self, ability):
        
        
        if (isinstance(ability, str)):
            id = abilitiesDictionary.get(ability)
        else: 
            id = ability

        return self.abilityModifiers[id] + (self.proficiences[id] * self.proficiencyBonus)
        
    def getScore(self, ability):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            
            return self.abiilityScores[id]

    def setScore(self, ability, score):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            
            self.abiilityScores[id] = score

    def setProficiency(self, ability, proficiency):
            if (isinstance(ability, str)):
                id = abilitiesDictionary.get(ability)
            else: 
                id = ability
            
            self.proficiences[id] = proficiency

    def randomGen():
        a = Abilities()
        return a

    def update(self):
        self.updateAbilityModifiers()
        self.skills.update()


    def updateAbilityModifiers(self):
        self.abilityModifiers = self.abiilityScores.copy()
        for i in range(len(self.abilityModifiers)):
            self.abilityModifiers[i] = int((self.abilityModifiers[i] - 10)/2)

    def changeProficiencyBonus(self):
        self.proficiencyBonus = self.entity.proficiencyBonus
        self.skills.changeProficiencyBonus(self.entity.proficiencyBonus)
