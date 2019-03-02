#import tkinter as tk

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
import Tkinter as tk
from itertools import *

root = tk.Tk()
notes = 0
cont = 1
rows = ['n','c','n','n']
data = [['note',1,'text'],['cont',5,'text'],['note',3,'text'],['note',10,'trext']]
print len(rows)
for x in range(4):
    for y in range(8):
        if(rows[x] == 'n'):
            temp = notes
            notes += 1
        else:
            temp = cont
            cont += 1
        for typeX in data:
            if(typeX[1] == temp and typeX[0][0] == rows[x]):
                labelText = typeX[2]
                break
            else:
                labelText = 'Unmapped'
        l = tk.Label(root, text=labelText,width=15)
        l.grid(row=x,column=y)

root.mainloop()

'''
TODO:
~ Find out how to parse XML data
~ Create the grid with naming


'''
