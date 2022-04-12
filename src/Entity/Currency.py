
indexDictionary = {
        "copper" : 0,
        "silver"  : 1,
        "electrum" : 2,
        "gold" : 3,
        "platinum" : 4
    }

indexToTypeDictionary = {
        0 : "copper",
        1 : "silver",
        2 : "electrum",
        3 : "gold",
        4 : "platinum"
    }

currencyExchange = [[1, 10, 50, 100, 1000],
                    [1, 1, 5, 10, 100],
                    [1, 1/5, 1, 2, 20],
                    [1, 1/10, 1/2, 1, 10],
                    [1/1000, 1/100, 1/20, 1/10, 1]]


class Currency:

    def __init__(self, gold=0, copper=0, silver=0, electrum=0, platinum=0):
        self.amounts = [copper, silver, electrum, gold, platinum]
    
    def add(currency1, currency2):
        for i in range(len(5)):
            currency1.amounts[i] += currency2.amounts[i]
        
    def getAmount(self, type):
        if (isinstance(type, str)):
            id = indexToTypeDictionary.get(type)
        else: 
            id = type
        return self.amounts[id]
    
    def setAmount(self, type, amount):
        if (isinstance(type, str)):
            id = indexToTypeDictionary.get(type)
        else: 
            id = type
        self.amounts[id] = amount

    def create(string):
        stringList = string.split(",")
        copper, silver, electrum, gold, platinum = 0, 0, 0, 0, 0
        for str in stringList:
            str = str.lower()
            if str.lower().find("cp") != -1:
                copper += int(str.lower().removesuffix("cp"))
            elif str.lower().find("sp") != -1:
                silver += int(str.lower().removesuffix("sp"))
            elif str.lower().find("ep") != -1:
                electrum += int(str.lower().removesuffix("ep"))
            elif str.lower().find("gp") != -1:
                gold += int(str.lower().removesuffix("gp"))
            elif str.lower().find("pp") != -1:
                platinum += int(str.lower().removesuffix("pp"))
        return Currency(gold = gold, silver = silver, platinum = platinum, copper = copper, electrum = electrum)

    def toString(self):
        return "{}cp {}sp {}ep {}gp {}pp".format(self.amounts[0], self.amounts[1], self.amounts[2], self.amounts[3], self.amounts[4])

    def simplify(self):
        for i in range(1,5).reversed():
            if not isinstance(self.amounts[i], int):
                extra = self.amounts[i] - int(self.amounts[i])
                self.amounts[i-1] += int(extra * Currency.conversionRate(i, i-1))
                self.amounts[i] = int(self.amounts[i])
        self.amounts[0] = int(self.amounts[0])

    def conversionRate(curr1, curr2):
        if (isinstance(curr1, str)):
            curr1 = indexDictionary.get(curr1)
            
        if (isinstance(curr2, str)):
            curr2 = indexDictionary.get(curr2)
        return currencyExchange[curr2][curr1]