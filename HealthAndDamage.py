import entityV2
import dice 
import HealthAndDamage

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
        self.hitDice = "1d34"
        self.maxHitDiceCount = self.entity.level
        self.maxHP = 1
        self.currentHP = 1
        self.tempHP = 1
        self.hitDiceCount = entity.level
        self.totalHealthPercentage = 1
        self.realHealthPercentage = 1

        self.deathSavesSuccesses = 0
        self.deathSavesFailures = 0
        self.stable = True

        self.isDead = False

        self.damageResistances = []
        self.damageImmunities = []
        self.damageVulnerabilities = []
        for i in range(len(damageTypes)):
            self.damageResistances.append(False)
            self.damageImmunities.append(False)
            self.damageVulnerabilities.append(False)

        self.updateHealth()
        #print("HEALTH MADE")
        
    def getResistance(self, damage):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        if (self.damageImmunities[damage]):
            return 0
        elif (self.damageResistances[damage]):
            return 0.5
        elif self.damageVulnerabilities[damage]:
            return 2
        else:
            return 1
    
    def setImmunity(self, damage, value):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        self.damageImmunities[damage] = value
    
    def setVulnerability(self, damage, value):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        self.damageVulnerabilities[damage] = value


    def setResistance(self, damage, value):    
        if (isinstance(damage, str)):
            damage = damageTypeDictionary.get(damage)
        
        self.damageResistances[damage] = value

    def doDamage(self, amount, type = None):
        if (type):
            res = self.getResistance(type)
        else:
            res = 1
        
        self.takeHealth(amount * res)

        self.updateHealth()

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
        
        self.updateIsDead()

        self.updateHealth()
    
    def addTempHP(self, amount):
        self.tempHP += amount

        self.updateHealth()
    
    def addHP(self, amount):
        self.currentHP += amount

        self.updateHealth()

    def updateHealth(self):
        #print("HET")
        self.totalHealthPercentage = (((self.currentHP + self.tempHP) / self.maxHP) * 100)
        self.realHealthPercentage = ((self.currentHP / self.maxHP) * 100)
        #print("Total Health % : {} \n Real Health % : {}".format(self.totalHealthPercentage, self.realHealthPercentage))
        self.updateIsDead()
    
    def updateIsDead(self):
        if (self.currentHP <= 0 and self.tempHP <= 0 and self.deathSavesFailures >= 3):
            self.isDead = True
            return True
        else:
            self.isDead = False
            return False


        






