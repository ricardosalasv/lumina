from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import math
import os


root = Tk()
root.title('Lumina 1.0')

d = os.getcwd()
d1 = os.path.join(d, "gray_light_icon.ico")

root.iconbitmap(d1)

# Main Variables

# Lux Requirement List
luxes = []
for i in range(50, 1050, 50):
    luxes.append(i)

for i in range(1500, 4500, 500):
    luxes.append(i)


# Fixtures' Lumen Specification List
lumens = [i for i in range(200, 8200, 200)]

# Architectural elements' colors
ceilingIndexes = {
    'White or very light': 0.7,
    'Light': 0.5,
    'Gray': 0.3
}

wallsIndexes = {
    'Light': 0.5,
    'Gray': 0.3,
    'Dark': 0.1
}

# K Collection
KCollection = [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]

# Frames
mainFrame1 = LabelFrame(root, width = 560, height = 160, padx=5, pady=5)
mainFrame1.grid(column=0, row=2, padx=10, pady=10, columnspan=3, sticky=W)
mainFrame1.grid_propagate(0)

mainFrame2 = LabelFrame(root, width = 560, height = 160, padx=5, pady=5)
mainFrame2.grid(column=0, row=2, padx=10, pady=10, columnspan=3, sticky=W)
mainFrame2.grid_propagate(0)

# Dimensions Frames
roomDFrame = LabelFrame(mainFrame1, text='Room Information', width = 200, height = 120, padx=5, pady=5)
roomDFrame.grid(column=0, row=0, padx=10, pady=10, columnspan=2, sticky=W)
roomDFrame.grid_propagate(0)

roomAFrame = LabelFrame(mainFrame2, text='Room Information', width = 200, height = 120, padx=5, pady=5)
roomAFrame.grid(column=0, row=0, padx=10, pady=10, columnspan=2, sticky=W)
roomAFrame.grid_propagate(0)

#Lighting and material properties Frames
lmDFrame = LabelFrame(mainFrame1, text='Lighting and Material Properties', width = 300, height = 120, padx=5, pady=5)
lmDFrame.grid(column=2, row=0, padx=10, pady=10, columnspan=2, sticky=W)
lmDFrame.grid_propagate(0)

lmAFrame = LabelFrame(mainFrame2, text='Lighting and Material Properties', width = 300, height = 120, padx=5, pady=5)
lmAFrame.grid(column=2, row=0, padx=10, pady=10, columnspan=2, sticky=W)
lmAFrame.grid_propagate(0)

# Calculate Frame
finalFrame = LabelFrame(root)
finalFrame.grid(column=0, row=3, columnspan=3, sticky=W+E, padx=10, pady=5)

# Number of fixtures Frame
fixturesNmbFrame = LabelFrame(finalFrame, text='Amount of fixtures needed')
fixturesNmbFrame.grid(column=1, row=0)


# Buttons

# Calculate Button and function

# Math logic
def calc():

    def fixturesH():
    
        if roomHeight <= 2.4:
            fixturesHeight = 2.4
        elif roomHeight > 2.4:
            fixturesHeight = math.ceil((4/5)*(roomHeight-0.85))

        if fixturesHeight < 2.4:
            fixturesHeight = 2.4

        return fixturesHeight


    if choosed.get() == 'Rectangular':
        
        roomLen = float(Da.get())
        roomWidth = float(Db.get())
        roomArea = roomLen * roomWidth
        roomHeight = float(Dh.get())
        
        fixturesHeight = fixturesH()

        firstK = ((roomArea)/(fixturesHeight*(roomLen+roomWidth)))
        
    
    elif choosed.get() == 'Irregular':
        
        roomArea = float(AArea.get())
        roomHeight = float(Ah.get())
        
        fixturesHeight = fixturesH()

        firstK = ((roomArea)/(fixturesHeight*(2*(math.sqrt(roomArea)))))

    
    def chooseClosestK():
        minDif = []
        for i in KCollection:
            minDif.append(abs(i-firstK))
        Dif = min(minDif)
        return minDif.index(Dif)

    K = chooseClosestK()
    
   
    # Determine Utilization Factor

    option1 = choosedDCeiling.get()
    search1 = list(ceilingIndexes.keys()).index(option1)
    listIter1 = gList[search1]

    option2 = choosedDwalls.get()
    search2 = list(wallsIndexes.keys()).index(option2)
    listIter2 = listIter1[search2]

    uFactor = listIter2[K]
    
    print(uFactor)

  
    reqFixtures = math.ceil(((roomArea*lux.get()/uFactor)/(choosedDLumen.get())

    fixtNmbOutput(reqFixtures)

calcBtn = Button(finalFrame, text='Calculate', font=('helvetica', '14'), command=calc).grid(column=0, row=0, sticky=W, padx=10, pady=10)

# Base inputs

# Rectangular Inputs

Da = Entry(roomDFrame, borderwidth=2)
Da.grid(column=1, row=0, padx=5, pady=5)
DaTex = Label(roomDFrame, text='Lenght').grid(column=0, row=0, padx=5, pady=5, sticky=W)

Db = Entry(roomDFrame, borderwidth=2)
Db.grid(column=1, row=1, padx=5, pady=5)
DbTex = Label(roomDFrame, text='Width').grid(column=0, row=1, padx=5, pady=5, sticky=W)

Dh = Entry(roomDFrame, borderwidth=2)
Dh.grid(column=1, row=2, padx=5, pady=5)
DhTex = Label(roomDFrame, text='Height').grid(column=0, row=2, padx=5, pady=5, sticky=W)

# Lumen Specification Selection

lumenDMenuTex = Label(lmDFrame, text="Fixtures' Luminous Flux").grid(column=0, row=0, sticky=W)
choosedDLumen = IntVar()
choosedDLumen.set(800)
lumenDMenu = ttk.Combobox(lmDFrame, textvar=choosedDLumen)
lumenDMenu.grid(column=1, row=0, padx=5, pady=5, sticky=E)
lumenDMenu['values'] = lumens

# Material Reflection Selection

# Ceiling Reflection Selection

ceilingDMenuTex = Label(lmDFrame, text="Ceiling Color").grid(column=0, row=1, sticky=W)
choosedDCeiling = StringVar()
# choosedDCeiling.set(str(ceilingIndexes)[0])
ceilingDMenu = ttk.Combobox(lmDFrame, textvar=choosedDCeiling)
ceilingDMenu.grid(column=1, row=1, padx=5, pady=5, sticky=E)
ceilingDMenu['values'] = list(ceilingIndexes.keys())
ceilingDMenu.current(0)

            # Wall Reflection Selection

wallsDMenuTex = Label(lmDFrame, text="Walls Color").grid(column=0, row=2, sticky=W)
choosedDwalls = StringVar()
# choosedDwalls.set(str(wallsIndexes)[0])
wallsDMenu = ttk.Combobox(lmDFrame, textvar=choosedDwalls)
wallsDMenu.grid(column=1, row=2, padx=5, pady=5, sticky=E)
wallsDMenu['values'] = list(wallsIndexes.keys())
wallsDMenu.current(0)

# Irregular Inputs

AArea = Entry(roomAFrame, borderwidth=2)
AArea.grid(column=1, row=0, padx=5, pady=5)
AAreaTex = Label(roomAFrame, text='Area').grid(column=0, row=0, padx=5, pady=5, sticky=W)


Ah = Entry(roomAFrame, borderwidth=2)
Ah.grid(column=1, row=1, padx=5, pady=5)
AhTex = Label(roomAFrame, text='Height').grid(column=0, row=1, padx=5, pady=5, sticky=W)

# Lumen Specification Selection

lumenAMenuTex = Label(lmAFrame, text="Fixtures' Luminous Flux").grid(column=0, row=0, sticky=W)
choosedALumen = IntVar()
choosedALumen.set(800)
lumenAMenu = ttk.Combobox(lmAFrame, textvar=choosedALumen)
lumenAMenu.grid(column=1, row=0, padx=5, pady=5, sticky=E)
lumenAMenu['values'] = lumens

# Material Reflection Selection

# Ceiling Reflection Selection

ceilingAMenuTex = Label(lmAFrame, text="Ceiling Color").grid(column=0, row=1, sticky=W)
choosedACeiling = StringVar()
ceilingAMenu = ttk.Combobox(lmAFrame, textvar=choosedACeiling)
ceilingAMenu.grid(column=1, row=1, padx=5, pady=5, sticky=E)
ceilingAMenu['values'] = list(ceilingIndexes.keys())
ceilingAMenu.current(0)

# Wall Reflection Selection

wallsAMenuTex = Label(lmAFrame, text="Walls Color").grid(column=0, row=2, sticky=W)
choosedAwalls = StringVar()
wallsAMenu = ttk.Combobox(lmAFrame, textvar=choosedAwalls)
wallsAMenu.grid(column=1, row=2, padx=5, pady=5, sticky=E)
wallsAMenu['values'] = list(wallsIndexes.keys())
wallsAMenu.current(0)

# Choose between regular and irregular shaped floorplan

choosed = StringVar()
dropShapeText = Label(root, text="Floorplan's Shape").grid(column=0, row=0, padx=10, sticky=W)
dropShape = ttk.Combobox(root, textvar=choosed)
dropShape.grid(column=1, row=0, sticky=W+E, padx=10, pady=5)
dropShape['values'] = ['Rectangular', 'Irregular']
dropShape.current(0)


# Specify Lux requirement
luxReqTex = Label(root, text='Illuminance Requirement (Lux)', padx=10).grid(column=0, row=1, sticky=W)
lux = IntVar()
luxMenu = ttk.Combobox(root, textvar=lux)
luxMenu.grid(column=1, row=1, sticky=W+E, padx=10, pady=5)
luxMenu['values'] = luxes
luxMenu.current(0)

# Outputs

# Number of fixtures needed

def blankOutput(*args):

    fixtures = Label(fixturesNmbFrame, text=40*' ')
    fixtures.grid(column=0, row=0)

def fixtNmbOutput(value):

    blankOutput()
    
    fixtures = Label(fixturesNmbFrame, text=value)
    fixtures.grid(column=0, row=0, sticky=W)

blankOutput()  

# Event Driven Functions

if choosed.get() == 'Rectangular':
    mainFrame1.tkraise()

def printValue(*args):
    if choosed.get() == 'Rectangular':
        print(choosed.get())
    elif choosed.get() == 'Irregular':
        print(choosed.get())

def frameRaise(*args):
    if choosed.get() == 'Rectangular':
        mainFrame1.tkraise()
    elif choosed.get() == 'Irregular':
        mainFrame2.tkraise()

def clearEntries(*args):
    Da.delete(0, END)
    Db.delete(0, END)
    Dh.delete(0, END)

    AArea.delete(0, END)
    Ah.delete(0, END)

    fixtures = Label(fixturesNmbFrame, text=20*' ')
    fixtures.grid(column=0, row=0)

choosed.trace('w', frameRaise)
choosed.trace('w', clearEntries)
choosed.trace('w', blankOutput)

# Lists for ceiling reflection of 0.7

# List for wall reflection of 0.5
list1_1 = [0.28, 0.31, 0.39, 0.45, 0.52, 0.54, 0.61, 0.63, 0.68, 0.71, 0.72]

# List for wall reflection of 0.3
list1_2 = [0.22, 0.27, 0.33, 0.40, 0.46, 0.50, 0.56, 0.60, 0.63, 0.67, 0.70]

# List for wall reflection of 0.1
list1_3 = [0.16, 0.20, 0.26, 0.35, 0.41, 0.45, 0.52, 0.56, 0.60, 0.64, 0.67]


# Lists for ceiling reflection of 0.5

# List for wall reflection of 0.5
list2_1 = [0.25, 0.30, 0.36, 0.44, 0.49, 0.53, 0.59, 0.63, 0.66, 0.69, 0.71]

# List for wall reflection of 0.3
list2_2 = [0.22, 0.27, 0.33, 0.40, 0.46, 0.50, 0.56, 0.60, 0.63, 0.67, 0.70]

# List for wall reflection of 0.1
list2_3 = [0.16, 0.20, 0.26, 0.35, 0.41, 0.45, 0.52, 0.56, 0.60, 0.64, 0.67]


# Lists for ceiling reflection of 0.3

# List for wall reflection of 0.5
list3_1 = [0.26, 0.30, 0.36, 0.44, 0.49, 0.53, 0.59, 0.62, 0.65, 0.68, 0.71]

# List for wall reflection of 0.3
list3_2 = [0.22, 0.27, 0.33, 0.40, 0.46, 0.50, 0.56, 0.60, 0.63, 0.67, 0.70]

# List for wall reflection of 0.1
list3_3 = [0.16, 0.20, 0.26, 0.35, 0.41, 0.45, 0.52, 0.56, 0.60, 0.64, 0.67]


# Lists for ceiling reflections

ceil_list7 = [list1_1, list1_2, list1_3]
ceil_list5 = [list2_1, list2_2, list2_3]
ceil_list3 = [list3_1, list3_2, list3_3]

# General list

gList = [ceil_list7, ceil_list5, ceil_list3]


root.mainloop()