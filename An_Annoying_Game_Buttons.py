# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:14:21 2022

@author: russj
"""

import tkinter as tk
from tkinter import messagebox
user_input = ''

#%%

coord = {'x': -2, 'y': -2}


def clear_console():
    Console.delete("1.0","end")
def clear_console_lower():    
    Console_lower.delete("1.0","end")
#def clear_entry():
#    entrybox.delete(0, 'end')
def write(text):
    Console.insert('1.0', text)
def write_lower(text):
    Console_lower.insert('1.0', text)


   
#%%  

''' this generates rooms, for now rooms are stored in dictionary below'''     
class room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.searched = 0
        
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
    startbutton.grid_forget()
    clear_console()
    clear_console_lower()    
    (coord['x'], coord['y']) = (1, 0) 
    write('The room is panelled in dark wood, with dirt in the corners and mysterious stains on the walls. The room has 4 doors, one for each cardinal point. Which one do you want to take? (n, s, e, w) \n' )
    write('You awaken in a mysterious room, lit by flickering candlelight.\nIn your right hand is a compass, in your left is a list of 4 items "tome, key, ruby, dagger"\n \n')  


#%%
''' this is the searching function, called by pressing the search button, with dictionary of unique statements depending on conditions'''

search_results= {('tome', True): 'There is a bookshelf in the corner.\n You dont know how you missed it!\nYou select the weightiest tome there',
                 ('dagger', True): 'There is a cupboard, high on the wall.\nYou can just reach by standing on the tome!',
                 ('dagger', False): 'There is a cupboard, high on the wall.\n You cant reach!' ,
                 ('key', True): 'You pry off a crooked wall panel with the dagger.\nBehind it is a key!' ,
                 ('key', False): 'There is something behind a crooked wall panel, but you cant get it out!',
                 ('ruby', True): 'You found a locked chest, but your key fit!\n' ,
                 ('ruby', False): 'You found a locked chest but you dont have a key!',}





def searching():
    clear_console_lower()
    item_locs = []
    for l in items.keys():
        item_locs.append(items[l].location)
    for s in rooms.keys():
        rooms[s].searched += 1
    if (coord['x'], coord['y']) in item_locs:
        for x in items.keys():
            if (coord['x'], coord['y']) == items[x].location:
                if items[x].req == None:
                    items[x].found = True
                    write_lower(search_results[items[x].tres, items[x].found])
                    messagebox.showinfo(title='Search Result', message=f'You got {items[x].tres}')
                    clear_console()
                    roomfinder()
                else:                
                    for r in items.keys():
                        if items[r].tres == items[x].req:
                            if items[r].found == False:
                                write_lower(search_results[items[x].tres, items[r].found])
                                clear_console()
                                roomfinder()
                            else:
                                items[x].found = True
                                write_lower(search_results[items[x].tres, items[r].found])
                                messagebox.showinfo(title='Search Result', message=f'You got {items[x].tres}')
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
''' moves from room to room depending on input and checks if you are dead'''

def doom():
    room_locs = []
    for r in rooms.keys():
        room_locs.append(rooms[r].location)
    if (coord['x'], coord['y']) in room_locs:
        roomfinder()
    else:
        messagebox.showinfo(title='Search Result', message='You have fallen to your doom! There was no room here!')
        startroom()




class btnMove:
    def __init__(self):
        pass
    
    @staticmethod
    def north_move():
        (coord['x'], coord['y']) =(coord['x'], coord['y'] - 1)
        clear_console()
        doom()
    @staticmethod 
    def south_move():
        (coord['x'], coord['y']) = (coord['x'], coord['y'] + 1)
        clear_console()
        doom()
    @staticmethod
    def east_move():
        (coord['x'], coord['y']) = (coord['x'] + 1, coord['y'])
        clear_console()
        doom()
    @staticmethod
    def west_move():
        (coord['x'], coord['y']) = (coord['x'] - 1, coord['y'])
        clear_console()
        doom()
    

#%%
''' game window'''

root1 = tk.Tk() # name of the main window in the GUI
root1.geometry("500x500")
root1.title('An Annoying Game')

label = tk.Label(root1, text='An Annoying Game', font=('Arial', 18)) # first argument is root1 to associate it with root1 window.
label.pack() #.pack puts it into the window

Console = tk.Text(root1, height=10, padx=5, pady=5, wrap=tk.WORD)
Console.pack(fill=tk.X)


#entrybox = tk.Entry(root1)
#entrybox.pack()
#entrybox.bind("<KeyPress>", shortcut)

frame = tk.Frame(root1, width=400, height=200,background='black')
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

button_n = tk.Button(frame, text='N', command=btnMove.north_move)
button_n.grid(row=1, column=2, sticky=tk.W+tk.E)

button_w = tk.Button(frame, text='W', command=btnMove.west_move)
button_w.grid(row=2, column=1, sticky=tk.W+tk.E)

button_search = tk.Button(frame, text='Search?', command=searching)
button_search.grid(row=2, column=2, sticky=tk.W+tk.E)

button_e = tk.Button(frame, text='E', command=btnMove.east_move)
button_e.grid(row=2, column=3, sticky=tk.W+tk.E)

button_s = tk.Button(frame, text='S', command=btnMove.south_move)
button_s.grid(row=3, column=2, sticky=tk.W+tk.E)

startbutton = tk.Button(frame, text='start', command=startroom)
startbutton.grid(row=4, column=1, columnspan=3, sticky=tk.W+tk.E)

frame.pack(fill= tk.X)

Console_lower = tk.Text(root1, height=10, padx=5, pady=5, wrap=tk.WORD)
Console_lower.pack(fill=tk.X)

write('Are you sure you ready to play?')

root1.mainloop() 