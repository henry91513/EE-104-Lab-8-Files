#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:26:33 2022

@author: pinyiyeh
"""

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

#Define Game window
WIDTH = 800 
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

#List for the dance moves
move_list = []
display_list = []

#Valuable needed in the game
score_Player1 = 0
score_Player2 = 0
current_move = 0
count = 17
dance_length = 4
rounds = 0

#Flag that can track what happen in the game
say_dance = False
show_countdown = True
moves_complete = False
game_over = False

#This state that when the game start the dancer will start in the starting position
dancer = Actor("dancer-start") 
dancer.pos = CENTER_X - 10, CENTER_Y - 40

#This code will arrange the colored squares in a cross shape below the dancer.
#For player one
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170 
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

#Draw Actors
def draw():
    
    #State which global we are using in this function
    global game_over, say_dance,score_Player1, score_Player2
    global count, show_countdown, rounds
    
    #If the game isn't over this function will keep runnig
    if not game_over:
        screen.clear() #Clear the line 
        screen.blit("stage", (0, 0)) #Add background in the game window
        #Draw Actor in their current location
        dancer.draw() 
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        
        screen.draw.text("Player 1 Score: " +
                         str(score_Player1), color="black", 
                         topleft=(10, 10)) #Print the score in the top-left corner for player one
        screen.draw.text("Player 2 Score: " +
                         str(score_Player2), color="black", 
                         topleft=(400, 10)) #Print the score in the top-left corner for player two
        
        if say_dance:
            screen.draw.text("Dance!", color="black",
                             topleft=(CENTER_X - 65, 150), fontsize=60)#Draw dance on the screen
            
            
        if show_countdown:
            screen.draw.text(str(count), color="black",
                             topleft=(CENTER_X - 8, 150), fontsize=60)##Draw count on the screen
            
            if (rounds % 2 == 0):      #player 1 has color orange
                screen.draw.text("Be ready, Player 1", color="orange",
                             topleft=(CENTER_X - 160, 170), fontsize=60)
            else:                      #player 2 has color blue
                screen.draw.text("Be ready, Player 2", color="blue",
                             topleft=(CENTER_X - 160, 170), fontsize=60)
    else:
        screen.clear()
        screen.blit("stage", (0, 0)) 
        
        screen.draw.text("Score for player1: " +   #display the final score for player1
                         str(score_Player1), color="orange",
                         topleft=(10, 10))
        screen.draw.text("Score for player2: " +   #diaplay the final score for player2
                         str(score_Player2), color="blue",
                         topleft=(400, 10))
        screen.draw.text("GAME OVER!", color="black",  #Display Game over
                         topleft=(CENTER_X - 130, 220), fontsize=60)
        screen.draw.text("Music: PPAP by Pikotaro", color="red",
                         topleft=(CENTER_X - 130, 300), fontsize=30)#display music credit
        if (score_Player1 > score_Player2):  #if player1 score is greater than player2
            screen.draw.text("Player1 won", color="orange",    
                             topleft=(CENTER_X - 130, 100), fontsize=60)
        elif (score_Player1 < score_Player2): #if player 2 sccore is greater than player1
            screen.draw.text("Player2 won", color="blue",
                             topleft=(CENTER_X - 130, 100), fontsize=60)
        elif (score_Player1 == score_Player2):
            screen.draw.text("Even, play again", color="black",
                             topleft=(CENTER_X - 130, 100), fontsize=60)
        
    return

#Reset Actor position
def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start" 
        up.image = "up"
        right.image = "right" 
        down.image = "down" 
        left.image = "left"
    return

#Update Actors to show the dance move
def update_dancer(move):
    global game_over#Global value 
    
    if not game_over:
        if move == 0:  #Up
            up.image = "up-lit" #Call yellow outline
            dancer.image = "dancer-up" #Change the image of the dancer
            clock.schedule(reset_dancer, 0.5)
        elif move == 1: #Right
            right.image = "right-lit" 
            dancer.image = "dancer-right" 
            clock.schedule(reset_dancer, 0.5)
        elif move == 2: #Down
            down.image = "down-lit" 
            dancer.image = "dancer-down" 
            clock.schedule(reset_dancer, 0.5)
        else:           #Left
            left.image = "left-lit" 
            dancer.image = "dancer-left" 
            clock.schedule(reset_dancer, 0.5)
            
    return

#Display the latest sequence of moves generated by the program.
def display_moves():
    global move_list, display_list, dance_length 
    global say_dance, show_countdown, current_move 
    
    if display_list:
        this_move = display_list[0] 
        display_list = display_list[1:] 
        
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1) 
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1) 
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1) 
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1) 
    else:
        say_dance = True
        show_countdown = False
        
    return

#Generate a list of dance move
def generate_moves():
    global move_list, dance_length, count 
    global show_countdown, say_dance 
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        rand_move = randint(0, 4) 
        move_list.append(rand_move) 
        display_list.append(rand_move)
    show_countdown = True
    countdown()
    
    return

#Display countdown before each sequence of moves
def countdown():
    global count, game_over, show_countdown 
    
    if count > 1:
        count = count - 1 #Upadate the count value
        clock.schedule(countdown, 1) #Call countdown function
    else:
        show_countdown = False #remove the countdown 
        display_moves()
        
    return

#Go to the next move in the list
def next_move():
    global dance_length, current_move, moves_complete 
    
    if current_move < dance_length - 1:
        current_move = current_move + 1 
        
    else:
     moves_complete = True
    return

#Make the program react when pressing the key
def on_key_up(key):
    global game_over, move_list, current_move, rounds, score_Player1, score_Player2
    if (rounds % 2 == 0): #key for player 1 which is up down left right
        if key == keys.UP:
            update_dancer(0)    #key.up is correspond to 0
            if move_list[current_move] == 0:
                if (rounds % 2 == 0):
                    score_Player1 = score_Player1 + 1
                    next_move()
                else:
                    score_Player2 = score_Player2 + 1
                    next_move()
            else:
                game_over = True
        elif key == keys.RIGHT:#key.right is cooresond to 1
            update_dancer(1)
            if move_list[current_move] == 1:
                if (rounds % 2 == 0):
                    score_Player1 = score_Player1 + 1
                    next_move()
                else:
                    score_Player2 = score_Player2 + 1
                    next_move()
            else:
                game_over = True
        elif key == keys.DOWN:#key.down is coorspond to 2
            update_dancer(2)
            if move_list[current_move] == 2:
                    if (rounds % 2 == 0):
                        score_Player1 = score_Player1 + 1
                        next_move()
                    else:
                        score_Player2 = score_Player2 + 1
                        next_move()
            else:
                game_over = True
        elif key == keys.LEFT:#key.left is coorspond to 3
            update_dancer(3)
            if move_list[current_move] == 3:
                    if (rounds % 2 == 0):
                        score_Player1 = score_Player1 + 1
                        next_move()
                    else:
                        score_Player2 = score_Player2 + 1
                        next_move()
            else:
                game_over = True
        return
    
    else: #key for player 2 which is WASD
        if key == keys.W:
            update_dancer(0)    #key.up is correspond to 0
            if move_list[current_move] == 0:
                if (rounds % 2 == 0):
                    score_Player1 = score_Player1 + 1
                    next_move()
                else:
                    score_Player2 = score_Player2 + 1
                    next_move()
            else:
                game_over = True
        elif key == keys.D:#key.right is cooresond to 1
            update_dancer(1)
            if move_list[current_move] == 1:
                if (rounds % 2 == 0):
                    score_Player1 = score_Player1 + 1
                    next_move()
                else:
                    score_Player2 = score_Player2 + 1
                    next_move()
            else:
                game_over = True
        elif key == keys.S:#key.down is coorspond to 2
            update_dancer(2)
            if move_list[current_move] == 2:
                    if (rounds % 2 == 0):
                        score_Player1 = score_Player1 + 1
                        next_move()
                    else:
                        score_Player2 = score_Player2 + 1
                        next_move()
            else:
                game_over = True
        elif key == keys.A:#key.left is coorspond to 3
            update_dancer(3)
            if move_list[current_move] == 3:
                    if (rounds % 2 == 0):
                        score_Player1 = score_Player1 + 1
                        next_move()
                    else:
                        score_Player2 = score_Player2 + 1
                        next_move()
            else:
                game_over = True
        return

generate_moves()
music.play("ppap")

#Builtin Pygame function
def update():
    global game_over, current_move, moves_complete
    global rounds, dance_length
    
    if not game_over:
        if moves_complete: #if moves_complete
            rounds = rounds + 1   #rounds + 1
            if (rounds % 2 == 0):   #dance_length +1 for every 2 trials
                dance_length = dance_length + 1
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
            music.stop()
            

pgzrun.go()