# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:14:21 2022

@author: russj
"""

import tkinter as tk
from tkinter import messagebox
user_input = ''
coord = {'x': -2, 'y': -2}


def clear_console():
    Console.delete("1.0","end")
def clear_entry():
    entrybox.delete(0, 'end')
def write(text):
    Console.insert('1.0', text)


   
#%%  

''' this generates rooms, for now rooms are stored in dictionary below'''     
class room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        
        
    def prompt(self):
        write('Another, identical, wood-panelled, four-doored room. What now?')
            
    def __eq__(self, other):
        return self.location == other
    

rooms = {1: room(0, 0), 2: room(1, 0,), 3: room(2, 0), 4: room(0, 1), 5: room(1, 1), 6: room(2, 1)} 

#%%
''' this generates treasures, for now treasures are stored in dictionary below'''  

class treasure:
    def __init__(self, treasure, x, y, requisite=None):
        self.x = x
        self.y = y
        self.tres = treasure
        self.location = (self.x, self.y)
        self.found = False
        self.req = requisite
        
            
    
items = {1: treasure('key', 1, 1, 'dagger'), 2: treasure('dagger', 2, 0, 'tome'), 3: treasure('tome', 2, 1), 4: treasure('ruby', 1, 0, 'key')}


''' unique room, not in room class, first room of game'''
def startroom():
    for i in items.keys():
        items[i].found = False
    (coord['x'], coord['y']) = (1, 0) 
    write('The room is panelled in dark wood, with dirt in the corners and mysterious stains on the walls. The room has 4 doors, one for each cardinal point. Which one do you want to take? (n, s, e, w) \n' )
    write('You awaken in a mysterious room, lit by flickering candlelight.\nIn your right hand is a compass, in your left is a list of 4 items "tome, key, ruby, dagger"\n \n')  


#%%
''' this is the searching function, called by pressing the search button'''

def searching():
    for x in items.keys():
        if (coord['x'], coord['y']) == items[x].location:
            messagebox.showinfo(title='Search Result', message=f'you have found a {items[x].tres} in this room!')
            if items[x].req == None:
                items[x].found = True
                messagebox.showinfo(title='Search Result', message=f'you got a {items[x].tres} ')
                roomfinder()
            else:                
                for r in items.keys():
                    if items[r].tres == items[x].req:
                        if items[r].found == False:
                            messagebox.showinfo(title='Search Result', message=f'but you need a {items[r].tres} to get to it')
                            roomfinder()
                        else:
                            items[x].found = True
                            messagebox.showinfo(title='Search Result', message=f'you used a {items[r].tres} and got {items[x].tres} ')
                            if items[x].tres == 'ruby':
                                messagebox.showinfo(title='Search Result', message='YOU WON THE GAME!! ')
                                startroom()
                            else:    
                                roomfinder()


   
#%%
''' function called by pressing enter on the entrybox, finds out where you are and creates the prompt'''
def roomfinder():
    if (coord['x'], coord['y']) == (-2, -2):
        startroom()
    else:
        for key in rooms:
            if (coord['x'], coord['y']) == rooms[key].location:
                clear_console()
                rooms[key].prompt()
            
            
#%%
''' moves from room to room depending on input'''
def move():
    global user_input
    xshift, yshift = 0, 0
    if user_input.lower() == 'quit':
        root1.destroy()
    else:
        if (coord['x'], coord['y']) == (-2, -2):
            startroom()
        else:
            if user_input == 'n':    # Move to room North of current room.
                yshift = -1
            elif user_input == 's':  # Move to room South of current room.
                yshift = 1
            elif user_input == 'w':  # Move to room West of current room.
                xshift = -1
            elif user_input == 'e':  # Move to room East of current room.
                xshift = 1
            else:
                write('Please enter a valid response')
            (coord['x'], coord['y']) = (coord['x'] + xshift, coord['y'] + yshift)
            if coord['x'] < 0 or coord['x'] > 2 or coord['y'] < 0 or coord['y'] > 1:
                messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
                clear_console()
                startroom()
            else:
                roomfinder()


#%%
''' captures the data input, records it in a variable and calls the room finder'''  
def shortcut(event):
    if event.keysym == 'Return':
        global user_input
        user_input = entrybox.get()
        clear_console()
        clear_entry()
        move()

''' game window'''

root1 = tk.Tk() # name of the main window in the GUI
root1.geometry("500x500")
root1.title('An Annoying Game')

label = tk.Label(root1, text='An Annoying Game', font=('Arial', 18)) # first argument is root1 to associate it with root1 window.
label.pack(padx=50, pady=50) #.pack puts it into the window

Console = tk.Text(root1, height=10, padx=5, pady=5, wrap=tk.WORD)
Console.pack()


entrybox = tk.Entry(root1)
entrybox.pack()
entrybox.bind("<KeyPress>", shortcut)

button = tk.Button(root1, text='Search?', command=searching)
button.pack(padx=50, pady=50)

write('Are you sure you want to continue? \nType start to begin. type quit to quit')

root1.mainloop() 