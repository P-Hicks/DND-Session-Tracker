import entityV2
import Abilities


skillsNames = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                             'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
                             'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

skillsNamesTuples = [('Acrobatics', 1), ('Animal Handling',5), ('Arcana',3), ('Athletics', 0), ('Deception',5), ('History',3), ('Insight',4),
                             ('Intimidation',5), ('Investigation',3), ('Medicine',4), ('Nature',3), ('Perception',4), ('Performance',5), ('Persuasion',5),
                             ('Religion',3), ('Sleight of Hand', 1), ('Stealth', 1), ('Survival',4)]

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
    
        self.proficiencies = []
        for i in range(len(self.modifiers)):
            self.proficiencies.append(False)

    def changeProficiencyBonus(self, bonus):
        self.proficiencyBonus = bonus

    def passiveCheck(self, skill):
        return 10 + self.checkModifier(skill)

    def getProficiency(self, skill):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        return self.proficiencies[id]

    def setProficiency(self, skill, boolean):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        self.proficiencies[id] = boolean

    def getModifier(self, skill):
        if (isinstance(skill, str)):
            skill = skillsDictionary.get(skill)
        id = skill

        if self.proficiencies[id]:
            return self.modifiers[id] + self.proficiencyBonus
        else:
            return self.modifiers[id]
        

    def updateSkills(self):
        self.modifiers = []
        for i in skillsNamesTuples:
            #print(i)
            self.modifiers.append(self.abilities.getModifier(i[1]))
       
    def update(self):
        self.updateSkills()


    class Exception:

        def __init__(self, index, value):
            self.index = index
            self.value = value





