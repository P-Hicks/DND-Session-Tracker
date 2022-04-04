
#Import the required library
from tkinter import *
import tkinter
import entityV2
import SessionEntityRow
from tkinter import filedialog as fd
import EntityStatsWindowGUI
import DamageWindow

class SessionGUI:
   def __init__(self, entityList = []):
      #Create an instance of tkinter frame or window
      win = Tk()
      #Define the geometry
      win.geometry("750x400")
      #Create a Frame
      self.frame= LabelFrame(win, height=30, text = 'Entities', padx = 10, pady = 10)
      
      #Adding a scrollbar
      myscrollbar = Scrollbar(self.frame,orient="vertical")
      myscrollbar.pack(side="right",fill="y")
      self.entitiyList = entityList
      self.rowList = []
      for i in entityList:
         self.rowList.append(SessionEntityRow.EntityRow(self.frame, i))
         self.rowList[-1].frame.pack(pady=0)


      self.frame.grid(row = 0, column = 0, rowspan = 5)

      self.openEntityButton = Button(win, text ="Open Entity", command = self.openEntityFile)
      self.aoeButton = Button(win, text ="Area Of Effect", command = self.aoe)
      self.updateButton = Button(win, text ="Update", command = self.update)
      self.openEntityButton.grid(row = 0, column = 1)
      self.aoeButton.grid(row = 1, column = 1)
      self.updateButton.grid(row = 2, column = 1)    

      win.mainloop()

   def openEntityFile(self):
      files = fd.askopenfilenames()
      for file in files:
         entity = entityV2.Entity.loadBin(file)
         self.rowList.append(SessionEntityRow.EntityRow(self.frame, entity))
         self.rowList[-1].frame.pack(pady=0)
         EntityStatsWindowGUI.CharSheetWindow(entity)

   def checkedList(self):
      rowList = []
      for row in self.rowList:
         if row.checked():
            rowList.append(row)
            
      
      return rowList



   def aoe(self):
      
      rowList = self.checkedList()
      entityList = map(lambda row: row.entity, rowList)
      damageWin = DamageWindow.DamageWindow(entityList, rowList)
      

   def update(self):
      for row in self.rowList:
         #print("ROW2")
         row.update()
         

   


list = []
char = entityV2.Entity(name="John", abilityList=[7, 13, 16, 12, 24, 20], proficiencyList=[False, True, False, True, False, True])
list.append(char)
char2 = entityV2.Entity(name="Rob", abilityList=[7, 7, 7, 72, 24, 20], proficiencyList=[False, True, False, True, False, True])
list.append(char2)

SessionGUI(list)