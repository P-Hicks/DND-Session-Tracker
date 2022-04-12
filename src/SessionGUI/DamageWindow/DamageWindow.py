import Entity.HealthAndDamage
from tkinter import *

class DamageWindow:

    def __init__(self, entityList = [], rowList=[]):
        self.entityList = entityList
        self.rowList = rowList

        self.win = Tk()
        #Define the geometry
        #self.win.geometry("300x300")
        
        #Create a Frame
        self.frame= LabelFrame(self.win, height=30, text = 'Damage', padx = 10, pady = 10)
        self.frame.grid(row = 0, column = 0)
        # Dropdown menu options
        options = ['Slashing',
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
                    "Psychic", 
                    "None"]
        
        # datatype of menu text
        self.clicked = StringVar()
        
        # initial menu text
        self.clicked.set("None")
        
        # Create Dropdown menu
        self.drop = OptionMenu( self.frame , self.clicked , *options)
        
        self.drop.grid(column = 1, row = 0)
        
        # Create button, it will change label text
        self.button = Button( self.frame , text = "Do Damage", command = self.do)
        self.button.grid(row = 1, column = 0)
        
        # Create Label
        self.entry = Entry(self.frame, width=10)
        self.entry.grid(row = 0, column = 0)

        #self.win.mainloop()
    
    def do(self):
        type = self.clicked.get()
        #print(type)
        amount = int(self.entry.get())
        if type=="None":
            type = None
        #print(self.entityList)
        for entity in self.entityList:
            entity.health.doDamage(amount, type)
        #print(self.rowList)
        for row in self.rowList:
            row.update()
        self.win.destroy()
  
