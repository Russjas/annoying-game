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
''' this is the searching function, called by pressing the search button, with dictionary of unique statements depending on conditions'''

search_results= {('tome', True): 'There is a bookshelf in the corner.\n You dont know how you missed it!\nYou select the weightiest tome there\nYou got the Tome!',
                 ('dagger', True): 'There is a cupboard, high on the wall.\nYou can just reach by standing on the tome!\nYou got the Dagger!',
                 ('dagger', False): 'There is a cupboard, high on the wall.\n You cant reach!' ,
                 ('key', True): 'You pry off a crooked wall panel with the dagger.\nBehind it is a key!\nYou got the Key!' ,
                 ('key', False): 'There is something behind a crooked wall panel, but you cant get it out!',
                 ('ruby', True): 'You found a locked chest, but your key fit!\nThe ruby was inside!\nYou Win!' ,
                 ('ruby', False): 'You found a locked chest but you dont have a key!',}

def searching():
    item_locs = []
    for l in items.keys():
        item_locs.append(items[l].location)
    if (coord['x'], coord['y']) in item_locs:
        for x in items.keys():
            if (coord['x'], coord['y']) == items[x].location:
                if items[x].req == None:
                    items[x].found = True
                    messagebox.showinfo(title='Search Result', message=(search_results[items[x].tres, items[x].found]))
                    clear_console()
                    roomfinder()
                else:                
                    for r in items.keys():
                        if items[r].tres == items[x].req:
                            if items[r].found == False:
                                messagebox.showinfo(title='Search Result', message=(search_results[items[x].tres, items[r].found]))
                                clear_console()
                                roomfinder()
                            else:
                                items[x].found = True
                                messagebox.showinfo(title='Search Result', message=(search_results[items[x].tres, items[r].found]))
                                clear_console()
                                if items[x].tres == 'ruby':
                                    startroom()
                                else:
                                    roomfinder()
    else:
       messagebox.showinfo(title='Search Result', message='nothing to see here!')
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
    room_locs = []
    for r in rooms.keys():
        room_locs.append(rooms[r].location)
    if (coord['x'], coord['y']) in room_locs:
        roomfinder()
    else:
        messagebox.showinfo(title='Search Result', message='You have fallen to your doom! There was no room here!')
        startroom()
        


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