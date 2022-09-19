# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:40:45 2022

@author: russj
"""
import tkinter as tk
from tkinter import messagebox


key = 0
dagger = 0
tome = 0
ruby = 0
user_input = ''

def clear_console():
    Console.delete("1.0","end")
def clear_entry():
    entrybox.delete(0, 'end')
def write(text):
    Console.insert('1.0', text)
    
def startroom():
    global key, ruby, tome, dagger, place
    place = 'startroom'
    key = 0
    dagger = 0
    tome = 0
    ruby = 0
    write('The room is panelled in dark wood, with dirt in the corners and mysterious stains on the walls. The room has 4 doors, one for each cardinal point. Which one do you want to take? (n, s, e, w) \n' )
    write('You awaken in a mysterious room, lit by flickering candlelight.\nIn your right hand is a compass, in your left is a list of 4 items "tome, key, ruby, dagger"\n \n')  
    print(place)
        
def room1():
    global place
    place = 'one'
    write('Another, identical, wood-panelled, four-doored room. What now?')
    print(place)
def room2():
    global place
    place = 'two'
    write('Another, identical, wood-panelled, four-doored room. What now?')
    print(place)
def room3():
    global place
    place = 'three'
    write('Another, identical, wood-panelled, four-doored room. What now?')
    print(place)
def room4():
    global place
    place = 'four'
    write('Another, identical, wood-panelled, four-doored room. What now?')
    print(place)
def room5():
    global place
    place = 'five'
    write('Another, identical, wood-panelled, four-doored room. What now?')
    print(place)
def room6():
    global place
    place = 'six'
    write('Another, identical, wood-panelled, four-doored room. What now?')   
    print(place)      
        
def searching():
    global ruby, dagger, tome, key
    if place == 'startroom':
        messagebox.showinfo(title='Search Result', message='You have played before I see.\n But you must play properly! \n \n')
        clear_console()
        startroom()
    if place == 'one':
        messagebox.showinfo(title='Search Result', message='Nothing to see here \n \n')
        clear_console()
        room1()
    if place == 'two':
        if ruby == 0 and key == 0:
            clear_console()
            write('You found a locked chest but you dont have a key!')
            room2()  
        elif ruby == 0 and key == 1:
            messagebox.showinfo(title='Search Result', message='You found a locked chest, but your key fit! \nThe ruby was inside!')
            messagebox.showinfo(title='Search Result', message='YOU WON!\n but was there more to see? \n \n')
            clear_console()
            startroom()  
        else:
            messagebox.showinfo(title='Search Result', message='You already got the ruby here! \n \n')
            clear_console()
            room2()
    if place == 'three':
        if tome == 0 and dagger == 0:
            messagebox.showinfo(title='Search Result', message='There is a cupboard, high on the wall.\n You cant reach!')
            clear_console()
            room3()
        elif tome == 1 and dagger == 0:
            messagebox.showinfo(title='Search Result', message='There is a cupboard, high on the wall.\n You can just reach by standing on the tome!')
            messagebox.showinfo(title='Search Result', message='You got the Dagger')
            dagger = 1
            clear_console()
            room3()
        elif dagger == 1:
            messagebox.showinfo(title='Search Result', message='You already got the Dagger here')
            clear_console()
            room3()
    if place == 'four':
        messagebox.showinfo(title='Search Result', message='Nothing to see here \n \n')
        clear_console()
        room4()
    if place == 'five':
        if dagger == 0 and key == 0:
            messagebox.showinfo(title='Search Result', message='There is something behind a wall panel, but you cant get it out!')
        elif dagger == 1 and key == 0:
            messagebox.showinfo(title='Search Result', message='You pry off a crooked wall panel with the dagger.\n Behind it is a key!')
            messagebox.showinfo(title='Search Result', message='You got the key')
            key = 1
            clear_console()
            room5()
        elif key == 1:
            messagebox.showinfo(title='Search Result', message='You already got the key here')
            clear_console()
            room3()
    if place == 'six':
        if tome == 0:
            messagebox.showinfo(title='Search Result', message='There is a bookshelf in the corner.\n You dont know how you missed it!\n You select the weightiest tome there')
            messagebox.showinfo(title='Search Result', message='You got the Tome!')
            tome = 1
            clear_console()
            room6()
    
def roomfinder():
    global place
    if place == 'start':
        if user_input == 'start':
            startroom()
        else:
            write('Please enter a valid response')
    elif place == 'startroom':
        if user_input.lower() == 'n':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 's':
            clear_console()
            room5()
        elif user_input.lower() == 'e':
            clear_console()
            room3()
        elif user_input.lower() == 'w':
            room1()
        #elif user_input.lower() == 'search':
          #   messagebox.showinfo(title='Search Result', message='You have played before I see.\n But you must play properly! \n \n')
        #    clear_console()
        #    startroom()
        else:
            write('Please enter a valid response')
        
    elif place == 'one':
        if user_input.lower() == 'n':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 's':
            clear_console()
            room4()
        elif user_input.lower() == 'e':
            clear_console()
            room2()
        elif user_input.lower() == 'w':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        #elif user_input.lower() == 'search':
        #    messagebox.showinfo(title='Search Result', message='Nothing to see here \n \n')
        #    clear_console()
        #    room1()
        else:
            write('Please enter a valid response')
            
    elif place == 'two':
        if user_input.lower() == 'n':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 's':
            clear_console()
            room5()
        elif user_input.lower() == 'e':
            clear_console()
            room3()
        elif user_input.lower() == 'w':
            clear_console()
            room1()
        elif user_input.lower() == 'search':
            pass
        else:
            write('Please enter a valid response')
            
    elif place == 'three':
        if user_input.lower() == 'n':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 's':
            clear_console()
            room6()
        elif user_input.lower() == 'e':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'w':
            clear_console()
            room2()
        elif user_input.lower() == 'search':
            pass
        else:
            write('Please enter a valid response')
            
    elif place == 'four':
        if user_input.lower() == 'n':
            clear_console()
            room1()
        elif user_input.lower() == 's':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'e':
            clear_console()
            room2()
        elif user_input.lower() == 'w':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'search':
            messagebox.showinfo(title='Search Result', message='Nothing to see here \n \n')
            clear_console()
            room4()
        else:
            write('Please enter a valid response')
    elif place == 'five':
        if user_input.lower() == 'n':
            clear_console()
            room2()
        elif user_input.lower() == 's':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'e':
            clear_console()
            room6()
        elif user_input.lower() == 'w':
            clear_console()
            room4()
        elif user_input.lower() == 'search':
            pass
        else:
            write('Please enter a valid response')
    elif place == 'six':
        if user_input.lower() == 'n':
            clear_console()
            room3()
        elif user_input.lower() == 's':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'e':
            messagebox.showinfo(title='Game Over', message='You fall to your doom. There was no room here! \n \n')
            clear_console()
            startroom()
        elif user_input.lower() == 'w':
            clear_console()
            room5()
        elif user_input.lower() == 'search':
            pass
        else:
            write('Please enter a valid response')
        
  
def shortcut(event):
    if event.keysym == 'Return':
        global user_input
        user_input = entrybox.get()
        clear_console()
        clear_entry()
        roomfinder()

def searchbtn():
    searching()

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

write('Are you sure you want to continue? \nType start to begin. \nIf it all gets too much, quit at any time with Q')
place = 'start'
root1.mainloop() 

