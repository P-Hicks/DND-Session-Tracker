import entityV2
import dice 


damageTypes = ['Slashing',
'Piercing',
'Bludgeoning',
'Poison',
'Acid',
'Fire',
'Cold',
'Radiant',
'Necrotic',
'Lightning',
'Thunder',
'Force',
"Psychic"]

damageTypeDictionary = {'Slashing' : 0,
'Piercing' : 1,
'Bludgeoning' : 2,
'Poison' : 3,
'Acid' : 4,
'Fire' : 5,
'Cold' : 6,
'Radiant' : 7,
'Necrotic' : 8,
'Lightning' : 9,
'Thunder' : 10,
'Force' : 11,
'Psychic' : 12}

class HealthAndDamage:

    def __init__(self, entity):
        self.entity = entity
        self.hitDice = 0
        self.maxHP = 0
        self.currentHP = 0
        self.tempHP = 0
        self.hitDiceCount = entity.level

        self.deathSavesSuccesses = 0
        self.deathSavesFailures = 0
        self.stable = True

        self.isDead = False

        self.damageResistances = []
        self.damageImmunities = []
        for i in range(len(damageTypes)):
            self.damageResistances.append(False)
            self.damageImmunities.append(False)
        
    def getResistance(self, damage):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        if (self.damageImmunities[damage]):
            return 1
        elif (self.damageResistances[damage]):
            return 0.5
        else:
            return 0
    
    def setImmunity(self, damage, value):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        self.damageImmunities[damage] = value
        
    def setResistance(self, damage, value):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        self.damageResistances[damage] = value

    def doDamage(self, amount, type = None):
        if (type):
            res = self.getResistance(type)
        else:
            res = 0
        
        self.currentHP -= amount * (1-res)
    
    def takeHealth(self, amount, critical = False):
        if (self.tempHP > 0):
            if (amount < self.tempHP):
                self.tempHP-=amount
                amount = 0
            else:
                amount -= self.tempHP
                self.tempHP = 0

        if (amount > 0):
            if (amount < self.currentHP):
                self.currentHP -= amount
                amount = 0
            if (amount >= self.currentHP):
                if (amount - self.currentHP >= self.maxHP):
                    #DIE IMMEDIATE
                    self.deathSavesFailiures = 3
                    self.currentHP = 0
                    amount = 0
                    self.stable = False
                elif (self.currentHP == 0):
                    if not critical:
                        self.deathSavesFailiures += 1
                    else:
                        self.deathSavesFailiures += 2
                    amount = 0
                else: 
                    self.currentHP = 0
                    amount = 0
        
        self.isDead()
    
    def addTempHP(self, amount):
        self.tempHP += amount
    
    def addHP(self, amount):
        self.currentHP += amount
    
    def isDead(self):
        if (self.currentHP <= 0 and self.tempHP <= 0 and self.deathSavesFailures >= 3):
            self.isDead = True
            return True
        else:
            self.isDead = False
            return False


    



            


    def updateHealth(self):
        return


        






