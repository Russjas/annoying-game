# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:58:25 2022

@author: russj
"""
print('Welcome to an Annoying Game')

key = 0
tome = 0
ruby = 0
dagger = 0

def startroom():
    global key
    global ruby
    global tome
    global dagger 
    key = 0
    dagger = 0
    tome = 0
    ruby = 0
    print('You awaken in a mysterious room, lit by flickering candlelight.\n in your right hand is a compass, in your left is a list of 4 items "tome, key, ruby, dagger"')
    di = input('The room is panelled in dark wood, with dirt in the corners and mysterious stains on the walls. The room has 4 doors, one for each cardinal point. Which one do you want to take? (N, S, E, W) ' ).lower()
    if di == 'q':
        pass
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 's':
        room5()
    elif di == 'e':
        room3()
    elif di == 'w':
        room1()
    elif di == 'search':
        print('You have played before! But you have to do it properly!')
        startroom()
        

def room1():
    global key
    global ruby
    global tome
    global dagger
    di = input('Another, identical, wood-panelled, four-doored room. What now? '  ).lower()
    if di == 'q':
        pass    
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
        
    elif di == 's':
        room4()
    elif di == 'e':
        room2()
    elif di == 'w':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'search':
        print('nothing to see here')
        room1rep()
def room1rep():
    global key
    global ruby
    global tome
    global dagger
    di = input('What now? '  ).lower()
    if di == 'q':
        pass    
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()        
    elif di == 's':
        room4()
    elif di == 'e':
        room2()
    elif di == 'w':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'search':
        print('nothing to see here')
        room1rep()
def room2():
    global key
    global ruby
    global tome
    global dagger    
    di = input('Another, identical, wood-panelled, four-doored room. What now? ' ).lower()
    if di == 'q':
        pass
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 's':
        room5()
    elif di == 'e':
        room3()
    elif di == 'w':
        room1()
    elif di == 'search':
        if ruby == 1:
            print('You already found the ruby!')
        else:
            chest = input('You found a chest! unlock the chest? (y/n)? ').lower()
            if chest == 'y':
                if key == 1:
                    ruby += 1
                    print ('You got the ruby!!')
                    if key + tome + dagger + key == 4:
                        print('YOU HAVE WON!!')
                else:
                    print('You dont have a key')
                    room2rep()
            else:
                room2rep()
def room2rep():
    global key
    global ruby
    global tome
    global dagger    
    di = input('What now? ').lower()
    if di == 'q':
        pass
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 's':
        room5()
    elif di == 'e':
        room3()
    elif di == 'w':
        room1()
    elif di == 'search':
        if ruby == 1:
            print('You already found the ruby!')
        else:
            chest = input('You found a chest! unlock the chest? (y/n)? ').lower()
            if chest == 'y':
                if key == 1:
                    ruby += 1
                    print ('You got the ruby!!')
                else:
                    room2rep()
            else:
                room2rep()
def room3():
    global key
    global ruby
    global tome
    global dagger
    di = input('Another, identical, wood-panelled, four-doored room. What now? ').lower()      
    if di == 'q':
        pass
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()        
    elif di == 's':
        room6()
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
        room2()
    elif di == 'search':
        if dagger == 1:
            print('You already found the dagger here!')
        else:
            cupboard = input('There is a cupboard, high up on one wall. Would you like to try and reach it? (y/n) ')
            if cupboard == 'y':
                if tome == 1:
                    print('You place the tome on the floor, it allows you to just reach!')
                    print('You got the dagger!')
                    dagger += 1
                    room3rep()
                else:
                    print('You cant reach!')
                    room3rep()
            else:
                room3rep()
            
def room3rep():
    global key
    global ruby
    global tome
    global dagger
    di = input('What now? ').lower()      
    if di == 'q':
        pass
    elif di == 'n':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()        
    elif di == 's':
        room6()
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
        room2()
    elif di == 'search':
        if dagger == 1:
            print('You already found the dagger here!')
        else:
            cupboard = input('There is a cupboard, high up on one wall. Would you like to try and reach it? (y/n) ')
            if cupboard == 'y':
                if tome == 1:
                    print('You place the tome on the floor, it allows you to just reach!')
                    print('You got the dagger!')
                    dagger += 1
                    room3rep()
                else:
                    print('You cant reach!')
                    room3rep()
            else:
                room3rep()
def room4():
    global key
    global ruby
    global tome
    global dagger
    di = input('Another, identical, wood-panelled, four-doored room. What now? ' ).lower()  
    if di == 'q':
        pass
    elif di == 'n':
        room1()        
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
        room5()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'search':
        print('nothing to see here')
        room4rep()

def room4rep():
    global key
    global ruby
    global tome
    global dagger
    di = input('What now? ' ).lower()  
    if di == 'q':
        pass
    elif di == 'n':
        room1()        
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
        room5()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'search':
        print('nothing to see here')
        room4rep()

def room5():
    global key
    global ruby
    global tome
    global dagger
    di = input('another 4 doored room! Search or direction? ').lower()
    if di == 'q':
        pass
    elif di == 'search':
        if key == 1:
            print('You already found the key here!')
            room5rep()
        else:            
            panel = input('One of the wall panels is slightly crooked! Is there something behind there? Would you like to dig it out? ')
            if panel == 'y':
                if dagger == 1:
                    print('You used the dagger to pry the panel out and found a key behind!')
                    key += 1
                    room5rep()
                else:
                    print('you dont have anything to pry the panel off!')
                    room5rep()
            else:
                room5rep()        
    elif di == 'n':
         room2()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'e':
         room6()
    elif di == 'w':
         room4()
    
def room5rep():
    global key
    global ruby
    global tome
    global dagger
    di = input('what now? ').lower()
    if di == 'q':
        pass
    elif di == 'search':
        if key == 1:
            print('You already found the key here!')
            room5rep()
        else:            
            panel = input('One of the wall panels is slightly crooked! Is there something behind there? Would you like to dig it out? ')
            if panel == 'y':
                if dagger == 1:
                    print('You used the dagger to pry the panel out and found a key behind!')
                    key += 1
                    room5rep()
                else:
                    print('you dont have anything to pry the panel off!')
                    room5rep()
            else:
                room5rep()   
    elif di == 'n':
         room2()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'e':
         room6()
    elif di == 'w':
         room4()  

def room6():
    global key
    global ruby
    global tome
    global dagger    
    di = input('Another, identical, wood-panelled, four-doored room. What now? ' ).lower()  
    if di == 'q':
        pass
    elif di == 'search':
        if tome == 1:
            print('You already found the tome here! \n \n ')
            room6rep()
        else:
            shelves = input('You see a bookshelf, you dont know how you missed it before! It has 4 shelves which would you like to search? (1-4) ').lower()
            if shelves == '1':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '2':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '3':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '4':
                print('Only 1 book on this shelf, it is very very heavy! You definitely consider it a tome')
                tome += 1
                room6rep()
    elif di == 'n':
         room3()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
         room5()
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()

def room6rep():
    global key
    global ruby
    global tome
    global dagger    
    di = input('what now? ').lower()  
    if di == 'q':
        pass
    elif di == 'search':
        if tome == 1:
            print('You already found the tome here! \n \n ')
            room6rep()
        else:
            shelves = input('You see a bookshelf, you dont know how you missed it before! It has 4 shelves which would you like to search? (1-4) ').lower()
            if shelves == '1':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '2':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '3':
                print('Some interesting titles here, but nothing weighty enough that you would consider it a tome')
                room6rep()
            elif shelves == '4':
                print('Only 1 book on this shelf, it is very very heavy! You definitely consider it a tome')
                tome += 1
                room6rep()
    elif di == 'n':
         room3()
    elif di == 's':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()
    elif di == 'w':
         room5()
    elif di == 'e':
        print('You fall to your doom. There was no room here! \n \n')
        startroom()


play = input('Are you sure you want to continue? (y/n). If it all gets too much, quit at any time with Q ' )
if play != 'y':
    quit()
else:
    startroom()