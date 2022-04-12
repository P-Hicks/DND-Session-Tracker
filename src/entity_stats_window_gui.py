import math
import random
import dice
import entityV2
import pickle
from tkinter import *
from tkinter import filedialog
import datetime
import AbilitiesGUI

stuff = ['a']

def main(entity_thing):
    


    boollist = []








        

        
        
    
    
    global entity 
    entity = entity_thing
    entity_win = Tk()
    entity_win.title(entity.name)
    
    #FRAMES/SECTIONS


    #update_button = Button(entity_win, text = "Update Sheet", command = update_stuff).grid(row = 0, column = 4)

    """
    #TOP ROW
    top_row = LabelFrame(entity_win, text = 'Name & Such', padx = 10, pady = 10)
    top_row.grid(row = 0, column = 0, rowspan = 1, columnspan = 3, padx = 10, pady = 10)

    name_label = Label(top_row, text = 'Name:')
    name_entry = Entry(top_row)
    class_label = Label(top_row, text = 'Class:')
    class_entry = Entry(top_row)
    level_label = Label(top_row, text = 'Level:')
    level_entry = Entry(top_row)
    background_label = Label(top_row, text = 'Background:')
    background_entry = Entry(top_row)
    race_label = Label(top_row, text = 'Race:')
    race_entry = Entry(top_row)
    alignment_label = Label(top_row, text = 'Alignment:')
    alignment_entry = Entry(top_row)

    name_label.grid(row=0, column = 0)
    name_entry.grid(row=0, column = 1)
    name_entry.insert(0, entity.name)
    class_label.grid(row=1, column = 0)
    class_entry.grid(row=1, column = 1)
    class_entry.insert(0, entity.Class)
    level_label.grid(row=0, column = 2)
    level_entry.grid(row=0, column = 3)
    level_entry.insert(0, entity.level)
    background_label.grid(row=1, column = 2)
    background_entry.grid(row=1, column = 3)
    background_entry.insert(0, entity.background)
    race_label.grid(row=0, column = 4)
    race_entry.grid(row=0, column = 5)
    race_entry.insert(0, entity.race)
    alignment_label.grid(row=1, column = 4)
    alignment_entry.grid(row=1, column = 5)
    alignment_entry.insert(0, entity.alignment)




    #Proficiency Bonus Area
    prof_bon = LabelFrame(entity_win, text = 'Proficiency Bonus', padx = 10, pady = 10)
    prof_bon.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

    prof_bon_label = Label(prof_bon, text = 'Proficiency Bonus:')
    prof_bon_entry = Entry(prof_bon, width = 3)

    prof_bon_label.grid(row=0, column = 0)
    prof_bon_entry.grid(row=0, column = 1)
    prof_bon_entry.insert(0, entity.proficiency_bonus)

    """



    #Abilities Area
    abilities = AbilitiesGUI.AbilityFrame(entity=entity, window=entity_win)


    """
    #Saving Throws
    entity.update_saving_throws()

    saving_throws = LabelFrame(entity_win, text = 'Saving Throws', padx = 10, pady = 10)
    saving_throws.grid(row = 1, column = 1, rowspan = 2, columnspan = 1, padx = 10, pady = 10, sticky = 'n')


    # print(entity.saving_throws)
    strength_label = Label(saving_throws, text = "Strength: ({:+})".format(entity.saving_throws[0][2]))
    strength_label.grid(row=0, column = 1)
    strengthbool = BooleanVar()
    strength_save_checkbox = Checkbutton(saving_throws, variable = strengthbool, onvalue = True, offvalue = False)
    strength_save_checkbox.grid(row=0, column = 0)
    if entity.saving_throws[0][1] == True:
        strength_save_checkbox.select()
    
    dexterity_label = Label(saving_throws, text = "Dexterity: ({:+})".format(entity.saving_throws[1][2]))
    dexterity_label.grid(row = 1, column = 1)
    dexteritybool = BooleanVar()
    dexterity_save_checkbox = Checkbutton(saving_throws, variable = dexteritybool, onvalue = True, offvalue = False)
    dexterity_save_checkbox.grid(row=1, column = 0)
    if entity.saving_throws[1][1] == True:
        dexterity_save_checkbox.select()

    constitution_label = Label(saving_throws, text = "Constitution: ({:+})".format(entity.saving_throws[2][2]))
    constitution_label.grid(row=2, column = 1)
    constitutionbool = BooleanVar()
    constitution_save_checkbox = Checkbutton(saving_throws, variable = constitutionbool, onvalue = True, offvalue = False)
    constitution_save_checkbox.grid(row=2, column = 0)
    if entity.saving_throws[2][1] == True:
        constitution_save_checkbox.select()

    intelligence_label = Label(saving_throws, text = "Intelligence: ({:+})".format(entity.saving_throws[3][2]))
    intelligence_label.grid(row=3, column = 1)
    intelligencebool = BooleanVar()
    intelligence_save_checkbox = Checkbutton(saving_throws, variable = intelligencebool, onvalue = True, offvalue = False)
    intelligence_save_checkbox.grid(row=3, column = 0)
    if entity.saving_throws[3][1] == True:
        intelligence_save_checkbox.select()

    wisdom_label = Label(saving_throws, text = "Wisdom: ({:+})".format(entity.saving_throws[4][2]))
    wisdom_label.grid(row=4, column = 1)
    wisdombool = BooleanVar()
    wisdom_save_checkbox = Checkbutton(saving_throws, variable = wisdombool, onvalue = True, offvalue = False)
    wisdom_save_checkbox.grid(row=4, column = 0)
    if entity.saving_throws[4][1] == True:
        wisdom_save_checkbox.select()
    
    
    
    charisma_label = Label(saving_throws, text = "Charisma: ({:+})".format(entity.saving_throws[5][2]))
    charisma_label.grid(row=5, column = 1)
    charismabool = BooleanVar()
    charisma_save_checkbox = Checkbutton(saving_throws, variable = charismabool, onvalue = True, offvalue = False)
    charisma_save_checkbox.grid(row=5, column = 0)
    if entity.saving_throws[5][1] == True:
        charisma_save_checkbox.select()




    #Skills
    skills = LabelFrame(entity_win, text = 'Skills', padx = 10, pady = 10)
    skills.grid(row = 3, column = 1, rowspan = 1, columnspan = 1, padx = 10, pady = 10, stick = 'n')
    
    count = 0
    gui_skills_list = []
    #boollist = [] up higher
    for i in entity.skills_list:
        skill_label = Label(skills, text = "{}: ".format(i[0]))
        skill_entry = Entry(skills, width = 3)
        skill_entry.insert(0, "{:+}".format(i[1]))
        skill_label.grid(row=count, column = 1)
        boollist.append(BooleanVar())
        skill_save_checkbox = Checkbutton(skills, variable = boollist[count], onvalue = True, offvalue = False)
        skill_save_checkbox.grid(row=count, column = 0)
        skill_entry.grid(row=count, column=2)
        if i[2] == True:
            skill_save_checkbox.select()
        gui_skills_list.append([skill_save_checkbox, skill_label, boollist[count], skill_entry])
        count += 1

    

    #Healthdata window
    healthdata = LabelFrame(entity_win, padx = 10, pady = 10)
    healthdata.grid(row = 1, column = 2, rowspan = 4, columnspan = 1, padx = 10, pady = 10, sticky = 'n')

    # ac
    ac_frame = LabelFrame(healthdata, text = 'AC', padx = 10, pady = 10)
    ac_frame.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    ac_entry = Entry(ac_frame, width = 3)
    ac_entry.grid(row = 0, column = 0)

    # speed
    speed_frame = LabelFrame(healthdata, text = 'Speed', padx = 10, pady = 10)
    speed_frame.grid(row = 0, column = 1, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    speed_entry = Entry(speed_frame, width = 3)
    speed_entry.grid(row = 0, column = 0)

    # initiative
    init_frame = LabelFrame(healthdata, text = 'Init.', padx = 10, pady = 10)
    init_frame.grid(row = 0, column = 2, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
    init_entry = Entry(init_frame, width = 3)
    init_entry.grid(row = 0, column = 0)

    # Hit Points
    hp_frame = LabelFrame(healthdata, text = 'Health', padx = 10, pady = 10)
    hp_frame.grid(row = 1, column = 0, rowspan = 1, columnspan = 3, padx = 10, pady = 10)

    current_hit_points_label = Label(hp_frame, text = "Current HP")
    max_hit_points_label = Label(hp_frame, text = "Max HP")
    temp_hit_points_label = Label(hp_frame, text = "Temporary HP")
    current_hit_points_entry = Entry(hp_frame, width = 5)
    max_hit_points_entry = Entry(hp_frame, width = 5)
    temp_hit_points_entry = Entry(hp_frame, width = 5)

    current_hit_points_label.grid(row = 0, column = 0)
    max_hit_points_label.grid(row = 1, column = 0)
    temp_hit_points_label.grid(row = 2, column = 0)
    current_hit_points_entry.grid(row = 0, column = 1)
    max_hit_points_entry.grid(row = 1, column = 1)
    temp_hit_points_entry.grid(row = 2, column = 1)

    # hit dice
    hitdice_frame = LabelFrame(healthdata, text = 'Hit Dice', padx = 10, pady = 10)
    hitdice_frame.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, padx = 10, pady = 10)

    max_hit_dice_entry = Entry(hitdice_frame, width = 10)
    max_hit_dice_entry.insert(0, entity.hit_dice)
    max_hit_dice_entry.grid(row = 0, column = 0, columnspan = 2)
    hit_dice_label = Label(hitdice_frame, text = 'Used:')
    hit_dice_label.grid(row = 1, column = 0)
    used_hit_dice_entry = Entry(hitdice_frame, width = 2)
    used_hit_dice_entry.grid(row = 1, column = 1)

    # death saves fails
    deathsaves_frame = LabelFrame(healthdata, text = 'Death Saves', padx = 10, pady = 10)
    deathsaves_frame.grid(row = 2, column = 1, rowspan = 1, columnspan = 2, padx = 10, pady = 10)
    
    death_save_successes = Label(deathsaves_frame, text = "Successes:").grid(row=0,column=0)
    
    death_save_failures = Label(deathsaves_frame, text = "Failures:").grid(row=1,column=0)


    count = 0
    gui_deathsaves_list = []
    death_boollist = []
    for i in range(3):
        death_boollist.append(BooleanVar())
        death_save_checkbox = Checkbutton(deathsaves_frame, variable = death_boollist[count], onvalue = True, offvalue = False)
        death_save_checkbox.grid(row=0, column = count+1)
        gui_deathsaves_list.append([death_save_checkbox, death_boollist[count]])
        count += 1
    
    count = 0
    for i in range(3):
        death_boollist.append(BooleanVar())
        death_save_checkbox = Checkbutton(deathsaves_frame, variable = death_boollist[count+3], onvalue = True, offvalue = False)
        death_save_checkbox.grid(row=1, column = count+1)
        gui_deathsaves_list.append([death_save_checkbox, death_boollist[count+3]])
        count += 1

    """




    # sheet_1 = LabelFrame(entity_win, text = 'Sheet', padx = 10, pady = 10)
    # sheet_1.grid(row = 1, column = 2, rowspan = 5, columnspan = 1, padx = 10, pady = 10)

    # entity.save('printself')
    # file = open('printself.txt')
    # a = file.read()
    # label1 = Label(sheet_1, text = a)
    # label1.pack()
    
    entity_win.mainloop()
    
    






#a = CharacterSheetV1.Entity(False)
#a.saving_throws[0][1] = True
#a.saving_throws[3][1] = True
#a.saving_throws[4][1] = True
#a.update_ability_scores()
#a.update_skills()
#a.update_saving_throws()

#main(a)


# # main(a)


# # main(a)

char = entityV2.Entity(name="John")
main(char)


