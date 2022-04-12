# Implementation of Collapsible Pane container
 
# importing tkinter and ttk modules
import tkinter as tk
from tkinter import ttk
import SessionGUI.SessionEntityRow as SessionEntityRow

class SessionGroup:
    def __init__(self, window, entityList = [], name = "", session = None, index = -1):
        self.session = session
        self.name = name
        self.index = index
        self.entityList = entityList
        self.overWindow =window
        self.session = session

    def createGUI(self):
        self.window = SessionGroupGUI(self.session.frame, group = self, entityList = self.entityList, name = self.name, session = self.session, index = -1)
        return self.window
    
    def addEntity(self, entity):
        self.entityList.append(entity)



class SessionGroupGUI:

    def __init__(self, window, entityList = [], name = "", session = None, index = -1, group = None):
        self.session = session
        self.name = name
        self.index = index
        self.entityList = entityList
        self.window = CollapsiblePane(window, "Collapse", "Expand")
        self.frame = self.window.frame
        self.group = group
        

        self.nameEntry = ttk.Entry(self.window.sideFrame, width=10)
        self.nameEntry.insert(0, self.name)
        self.nameEntry.bind("<Return>", self.changeName) 
        self.nameEntry.grid(row = 0, column = 0, padx = 10)


        self.deleteButton = ttk.Button(self.window.sideFrame, text= "Remove", command = self.deleteFromList)
        self.deleteButton.grid(row = 0, column = 1, padx = 10)

        self.checkButton = ttk.Button(self.window.sideFrame, text= "Check All", command = self.toggleCheck)
        self.checkButton.grid(row = 0, column = 2, padx = 10)

        self.addButton = ttk.Button(self.window.sideFrame, text= "Add To List", command = self.addToList)
        self.addButton.grid(row = 0, column = 3, padx = 10)

        #REMOVE GROUP
        #NAME GROUP


        self.rowList = []
        self.rebuild()
        self.isExpanded = self.window._variable

    def changeName(self, args):
        self.name = self.nameEntry.get()
        self.group.name = self.nameEntry.get()



    def toggleCheck(self):
        if len(self.checkedList()) < len(self.rowList):
            for row in self.rowList:
                if not row.checked():
                    row.checkbuttonToggle()
        else:
            for row in self.rowList:
                row.checkbuttonToggle()


    def checkedList(self):
        rowList = []
        for row in self.rowList:
            if row.checked():
                rowList.append(row)
            
        return rowList

    def rebuild(self):
        for i in self.rowList:
            i.frame.destroy()

        self.rowList = []
        row = 0
        for i in range(len(self.entityList)):
            self.rowList.append(SessionEntityRow.EntityRow(self.frame, self.entityList[i]))
            self.rowList[-1].frame.grid(row = i, column = 0, pady=0)
            row += 1

   
    def update(self):
        for row in self.rowList:
            #print("ROW2")
            row.update()
        self.changeName()
    
    def addToList(self):
        #self.session.addToGroup(self.index)
        entityList = list(self.session.deleteFromList())
        for entity in entityList:
            self.entityList.append(entity)
        self.session.rebuild()
        
            
    
    def deleteFromList(self):
        rowList = self.checkedList()
        entityList = map(lambda a : a.entity, rowList)
        for entity in entityList:
            self.entityList.remove(entity)
            if self.session:
                self.session.entityList.append(entity)
        self.session.rebuild()
        #self.rebuild()



class CollapsiblePane(ttk.Frame):
    """
     -----USAGE-----
    collapsiblePane = CollapsiblePane(parent,
                          expanded_text =[string],
                          collapsed_text =[string])
 
    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    """
 
    def __init__(self, parent, expanded_text ="Collapse <<",
                               collapsed_text ="Expand >>"):
 
        ttk.Frame.__init__(self, parent)
 
        # These are the class variable
        # see a underscore in expanded_text and _collapsed_text
        # this means these are private to class
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text
 
        # Here weight implies that it can grow it's
        # size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)
 
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()
 
        # Checkbutton is created but will behave as Button
        # cause in style, Button is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        self._button = ttk.Checkbutton(self, variable = self._variable,
                            command = self._activate, style ="TButton")
        self._button.grid(row = 0, column = 0)
 
        # This wil create a separator
        # A separator is a line, we can also set thickness
        self.sideFrame = ttk.Frame(self)
        self.sideFrame.grid(row = 0, column = 1, sticky ="we")
 
        self.frame = ttk.Frame(self)
 
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if not self._variable.get():
 
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.frame.grid_forget()
 
            # This will change the text of the checkbutton
            self._button.configure(text = self._collapsed_text)
 
        elif self._variable.get():
            # increasing the frame area so new widgets
            # could reside in this container
            self.frame.grid(row = 1, column = 0, columnspan = 2)
            self._button.configure(text = self._expanded_text)
 
    def toggle(self):
        """Switches the label frame to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()