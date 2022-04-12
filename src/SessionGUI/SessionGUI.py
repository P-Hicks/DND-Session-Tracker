#modules = dir()
#print("Session : " + str(modules))

#Import the required library
#from .DamageWindow import DamageWindow
import SessionGUI.DamageWindow.DamageWindow as DamageWindow
import Entity.entityV2 as Entity
from tkinter import *
import tkinter
from tkinter import filedialog as fd
import SessionGUI.SessionEntityRow as SessionEntityRow
import CharacterSheetGUI.EntityStatsWindowGUI as EntityStatsWindowGUI
import SessionGUI.SessionGroup as SessionGroup


class SessionGUI:
   def __init__(self, entityList = []):
      #Create an instance of tkinter frame or window
      self.win = Tk()
      #Define the geometry
      self.win.geometry("1000x400")
      #Create a Frame
      self.frame= LabelFrame(self.win, height=30, text = 'Entities', padx = 20, pady = 10)
      self.frame.grid(row = 0, column = 0, rowspan = 5)
      
      self.entityList = entityList
      
      self.rowList = []
      self.groupList = []
      self.rebuild()
      
      self.controlFrame= LabelFrame(self.win, height=30, text = 'Controls', padx = 20, pady = 10)
      self.controlFrame.grid(row = 0, column = 1, rowspan = 2)

      self.openEntityButton = Button(self.controlFrame, text ="Open Entity", command = self.openEntityFile)
      self.aoeButton = Button(self.controlFrame, text ="Area Of Effect", command = self.aoe)
      self.updateButton = Button(self.controlFrame, text ="Update", command = self.update)
      self.newCharButton = Button(self.controlFrame, text ="New Character", command = self.addNew)
      self.removeCharButton = Button(self.controlFrame, text ="Remove Entities", command = self.deleteCommand)
      self.createGroupButton = Button(self.controlFrame, text ="Create Group", command = self.createGroup)
      self.openEntityButton.grid(row = 0, column = 0)
      self.aoeButton.grid(row = 1, column = 0)
      self.updateButton.grid(row = 2, column = 0)
      self.newCharButton.grid(row = 3, column = 0)
      self.removeCharButton.grid(row = 4, column = 0)
      self.createGroupButton.grid(row = 5, column = 0)
              

      self.win.mainloop()

   def openEntityFile(self):
      files = fd.askopenfilenames()
      for file in files:
         entity = Entity.Entity.loadBin(file)
         self.entityList.append(entity)
      self.rebuild()
   


   def openEntityFileMultiple(self, amount):
      files = fd.askopenfilenames()
      for file in files:
         entity = Entity.Entity.loadBin(file)
         for i in range(amount):
            self.entityList.append(entity)
      self.rebuild()


   def clearChecked(self):
      if len(self.checkedListTop()) < len(self.rowList):
         for row in self.rowList:
            if not row.checked():
               row.checkbuttonToggle()
      else:
         for row in self.rowList:
            row.checkbuttonToggle()

   def checkedListTop(self):
      rowList = []
      for row in self.rowList:
         if isinstance(row, SessionEntityRow.EntityRow):
            if row.checked():
               rowList.append(row)
      return rowList
   
   def addToGroup(self, index):
      entityList = list(self.deleteFromList())
      #print(entityList)
      for object in entityList:
         self.groupList[index].addEntity(object)
      self.rebuild()

   def deleteFromList(self):
      print("delete")
      rowList = self.checkedListTop()
      #print(rowList)
      deleteEntityList = list(map(lambda a : a.entity, rowList))
      for entity in deleteEntityList:
         self.entityList.remove(entity)
         
      #self.rebuild()
      #print(deleteEntityList)
      return deleteEntityList
   
   def deleteCommand(self):
      self.deleteFromList()
      self.rebuild()

   def checkedList(self):
      rowList = []
      for row in self.rowList:
         if isinstance(row, SessionEntityRow.EntityRow):
            if row.checked():
               rowList.append(row)
         elif isinstance(row, SessionGroup.SessionGroupGUI):
            for innerRow in row.checkedList():
               rowList.append(innerRow)
            
      return rowList

   def aoe(self):
      
      rowList = self.checkedList()
      entityList = map(lambda row: row.entity, rowList)
      damageWin = DamageWindow.DamageWindow(entityList, rowList)
   
   def rebuild(self):
      #for i in self.rowList:
      #   i.frame.destroy()
      self.frame.destroy()
      self.frame= LabelFrame(self.win, height=30, text = 'Entities', padx = 10, pady = 10)
      self.frame.grid(row = 0, column = 0, rowspan = 5)
      
      #print(self.entityList)
      self.rowList = []
      row = 0
      for i in range(len(self.entityList)):
         self.rowList.append(SessionEntityRow.EntityRow(self.frame, self.entityList[i]))
         self.rowList[-1].frame.grid(row = i, column = 0, pady=0)
         row += 1
      #print(self.groupList)
      for i in range(len(self.groupList)):
         self.rowList.append(self.groupList[i].createGUI())
         self.rowList[-1].window.grid(row = row+i, column = 0, pady=0)

   def createGroup(self):
      entityList = list(self.deleteFromList())
      self.groupList.append(SessionGroup.SessionGroup(self.frame, entityList, name = "GROUP", session=self))
      self.rebuild()

   def update(self):
      for row in self.rowList:
         #print("ROW2")
         row.update()
   
   def addNew(self):
      self.entityList.append(Entity.Entity.new_character())
      self.rebuild()

         

def main():
   list = []
   char = Entity.Entity(name="John", abilityList=[7, 13, 16, 12, 24, 20], proficiencyList=[False, True, False, True, False, True])
   list.append(char)
   char2 = Entity.Entity(name="Rob", abilityList=[7, 7, 7, 72, 24, 20], proficiencyList=[False, True, False, True, False, True])
   list.append(char2)
   list.append(Entity.Entity.new_character())

   SessionGUI(list)