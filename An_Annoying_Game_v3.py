# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:14:21 2022

@author: russj
"""
import csv
import tkinter as tk
from tkinter import messagebox
from pandas import *

#%% coordinates, functions and startroom
''' keeps track of current location coordinates and defines frequently used functions'''
coord = {'x': -2, 'y': -2}


def clear_console():
    Console.delete("1.0","end")
def clear_console_lower():    
    Console_lower.delete("1.0","end")
def write(text):
    Console.insert('1.0', text)
def write_lower(text):
    Console_lower.insert('1.0', text)
def startroom():
    for i in items.keys():
        items[i].found = False
    startbutton.grid_forget()
    button_search.grid(row=2, column=2, sticky=tk.W+tk.E)
    clear_console()
    clear_console_lower()    
    (coord['x'], coord['y']) = (1, 0) 
    write('The room is panelled in dark wood, with dirt in the corners and mysterious stains on the walls. The room has 4 doors, one for each cardinal point. Which one do you want to take? (n, s, e, w) \n' )
    write('You awaken in a mysterious room, lit by flickering candlelight.\nIn your right hand is a compass, in your left is a list of 4 items "tome, key, ruby, dagger"\n \n')  

#%% room class and room room generators
'''room class, functions and dictionaries'''

class room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.searched = 0
    
    @staticmethod
    def room_list():
        room_locs = []
        for r in rooms.keys():
            room_locs.append(rooms[r].location)
        return room_locs
        
    def prompt(self):
        write('Another, identical, wood-panelled, four-doored room. What now?')
            
    def __eq__(self, other):
        return self.location == other
    
# reading CSV file
room_file = read_csv("rooms2_grid.csv")
 
# converting column data to list
x_r2 = room_file['x'].tolist()
y_r2 = room_file['y'].tolist()

coords =list(zip(x_r2, y_r2))


rooms = {1: room(0, 0), 2: room(1, 0,), 3: room(2, 0), 4: room(0, 1), 5: room(1, 1), 6: room(2, 1)} 
rooms2 = {i: room(x, y) for i, (x, y) in enumerate(coords)
          }
rooms2list =[]
for r in rooms2.keys():
    rooms2list.append(rooms2[r].location)

#%% treasures
''' this generates treasures, for now treasures are stored in dictionary below. next step is to produce treasure for the expanded rooms'''  

class treasure:
    def __init__(self, treasure, x, y, requisite=None):
        self.x = x
        self.y = y
        self.tres = treasure
        self.location = (self.x, self.y)
        self.found = False
        self.req = requisite
    
    @staticmethod
    def tres_list():
        item_locs = []
        for l in items.keys():
            item_locs.append(items[l].location)
        return item_locs
        
            
    
items = {1: treasure('key', 1, 1, 'dagger'), 2: treasure('dagger', 2, 0, 'tome'), 3: treasure('tome', 2, 1), 4: treasure('ruby', 1, 0, 'key')}

# reading CSV file
treasure_file = read_csv("treasures.csv")
 
# converting column data to list
f_tres = treasure_file['treasure'].tolist()
f_x = treasure_file['x'].tolist()
f_y = treasure_file['y'].tolist()
f_req = treasure_file['req'].tolist()
fix_req = ['' if (x == 'remove') else x for x in f_req]

zip_tresausre =list(zip(f_tres, f_x, f_y, fix_req))
items2 = {i: treasure(t, x, y, r) for i, (t, x, y, r) in enumerate(zip_tresausre)
          }




#%% searching
''' this is the searching function, called by pressing the search button, with dictionary of unique statements depending on conditions'''



# Old method, replaced by one for expanded game - hopefully
#                # (self.item, self.req_found, words)
#search_results= {('', None): 'There is nothing to see here!',
#                 ('tome', None): 'There is a bookshelf in the corner.\nYou dont know how you missed it!\nYou select the weightiest tome there',
#                 ('dagger', True): 'There is a cupboard, high on the wall.\nYou can just reach by standing on the tome!',
#                 ('dagger', False): 'There is a cupboard, high on the wall.\nYou cant reach!' ,
#                 ('key', True): 'You pry off a crooked wall panel with the dagger.\nBehind it is a key!' ,
#                 ('key', False): 'There is something behind a crooked wall panel, but you cant get it out!',
#                 ('ruby', True): 'You found a locked chest, but your key fit!\n' ,
#                 ('ruby', False): 'You found a locked chest but you dont have a key!',}
#

# reading CSV file
data = read_csv("search_results.csv")
 
# converting column data to list
tres_res = data['treasure'].tolist()
reqf_res = data['req_found'].tolist()
reqf_prompt = data['prompt'].tolist()

def string_to_bool(s):
    if s == 'TRUE':
        return True
    elif s == 'FALSE':
        return False
    else:
        pass
    
sr_keys =list(zip(tres_res, reqf_res))
zip_keys = [(i, string_to_bool(v)) for (i, v) in sr_keys]
search_results = {zip_keys[i]: reqf_prompt[i] for i in range(len(zip_keys))}
extras = {('', ''): 'Nothing to see here', (None, None): 'Nothing to see here'}
search_results.update(extras)



def search():
    clear_console_lower()
    x = search_instance(coord['x'], coord['y'])
    try:
        write_lower(search_results[x.out])
        
    except KeyError:
        pass
    if x.req_found == True or x.req_found == None:
        try:
            items[x.index].found = True
            messagebox.showinfo(title='Search Result', message=f'You got a {items[x.index].tres}.')
            unlock_check()
        except:
            return ''
    


class search_instance:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.loc = (self.x, self.y)
        self.index = self.get_index()
        self.item = self.get_item()
        self.req = self.get_req()
        self.req_found = self.get_req_found()
        self.out = (self.item, self.req_found)
        
    def get_index(self):
        if self.loc in treasure.tres_list():
            for x in items.keys():
                if (self.loc) == items[x].location:
                    return x
        else:
             return None
    def get_item(self):
        if self.loc in treasure.tres_list():
            for x in items.keys():
                if self.index == x:
                    return items[x].tres
        else:
            return ''
    def get_req(self):
        if self.loc in treasure.tres_list():
            for x in items.keys():
                if self.index == x:
                   return items[x].req
        else:
            return ''    
    def get_req_found(self):
        if self.loc in treasure.tres_list():
            for r in items.keys():
                if items[r].tres == self.req:                       #find the index of the room that has the requisite
                    return items[r].found
        else:
            return ''
                    
                    
        


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
    if (coord['x'], coord['y']) in room.room_list():
        roomfinder()
    else:
        messagebox.showinfo(title='DEATH!', message='You have fallen to your doom! There was no room here!')
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
'''unlock new levels/win the game''' 
def unlock_check():
    found_tot =sum([1 for x in items.keys() if items[x].found == True]) 
    if found_tot == len(treasure.tres_list()):
        if len(treasure.tres_list()) < 5:
            messagebox.showinfo(title='WINNER', message='Unlocked new rooms!')
            rooms.update(rooms2)
            items.update(items2)
            startroom()
        else:
            messagebox.showinfo(title='WINNER?', message='I guess you won....\nWas it worth it?')
            startroom()
#%%
''' game window'''

root1 = tk.Tk() # name of the main window in the GUI
root1.geometry("500x500")
root1.title('An Annoying Game')

label = tk.Label(root1, text='An Annoying Game', font=('Arial', 18)) # first argument is root1 to associate it with root1 window.
label.pack() #.pack puts it into the window

Console = tk.Text(root1, height=10, padx=5, pady=5, wrap=tk.WORD)
Console.pack(fill=tk.X)

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

button_search = tk.Button(frame, text='Search?', command=search)


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