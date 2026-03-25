#File Name: Spider-Man: Saving Gwen Stacy
#Spider-Man game. I'll give a full plot description later
#File Author: Sahaj Ranadey
#last Edited: 23/03/2026

#imports (Libraries)

import random
import time

#Global Variables

spider_man_health = 100
print_delay = 0.3


#Functions

def main_menu():
    global player_name
    print("---------------------------")
    print("Spider-Man: Saving Gwen Stacy")
    print("---------------------------")
    print()
    print("How to play:")
    print("As you encounter the battle functions, they will start to explain themselves. to access areas, use:")
    print("'1' for Empire State University,")
    print("'2' for Times Square,")
    print("'3' for Wall Street, ")
    print("'4' for Central Park,")
    print("'5' for Home in Queens,")
    print("and '6' when you're ready for the final fight.")
    print("If at any point you wish to quit? Just input 'I'm done being Spider-Man' exactly and the game will restart.")
    print()

    while True:
        try:
            print("Which Spider-Man would you like to be?")
            print("Type 1 for Peter Parker, 2 for Peter Parker, or 3 for Peter Parker: ")
            player_choice = int(input())
            if player_choice == 1 or player_choice == 2 or player_choice == 3:
                player_name = "Peter Parker"
                break
            else:
                print("Try again and pick 1, 2, or 3. Because you have to be Peter Parker.")
        except ValueError:
            print("Invalid input.")

    while True:
            try:
                print(f"Hi {player_name} press 1 to start your journey, or 2 to quit.")
                user_input = int(input())
                if user_input == 1:
                        print("Empire State University")
                        print("The haunting sound of an explosion rumbles through the campus of Empire State University.")
                        print("Teenagers sprint in panic, professors hide, and through it all? You slip away from the crowd.")
                        print("Subtly, you slip out of your civilian clothes to reveal the suit underneath.")
                        print("Red and blue spandex. Shimmering in the gleaming sun. An odd suit, but one that the citizens of the city now love.")
                        print()
                        print("Why?")
                        print()
                        print("Simple.")
                        print()
                        print("You're a hero.")
                        print()
                        print("In fact? You're THE Hero.")
                        print()
                        print("You")
                        print()
                        print()
                        print("Are")
                        print()
                        print()
                        print("Spider-Man")
                        area_01()
                elif user_input == 2:
                    print("Fine. Don't play. Bye. Nerd.")
                    exit()
                else:
                    print("Invalid Option.")
            except ValueError:
                print("Invalid input.")
def battle():
    print("Rhino")

def riddle_fight():
    print("Mysterio")

def pattern_recognition():
    print("Chameleon")

def dodge_timing():
#function for area 1
    print("Here are the instructions as to how you will play this area of the game.")
    print("When the word 'DODGE' pops up on your screen? You have 1 second to input the letter 'D'.")
    print("If you're too late? You die and you lose the game.")
    print("After dodging 3 times? You can press 'A' to Attack and you defeat this level.")

def round_repeating():
    print("Doctor Octopus")

def final_boss():
    print("Green Goblin")

#these are all the specialized battle functions for each of the fights in the game.

#---------------------------------------------------------------------------

def area_01():
    print("Empire State University")
def area_02():
    print("Times Square")

def area_03():
    print("Rhino in Wall Street")

def area_04():
    print("The Scorpion in Central Park")

def area_05():
    print("Aunt May's home in Queens")

def final_area():
    print("Brooklyn Bridge")

#these are all the settings for each fight. All the locations. 

#---------------------------------------------------------------------------

#main routine

main_menu()
