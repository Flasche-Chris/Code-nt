import random
import time
import sys
from logo import *
from animation import *




def print_line():
    print("--------------------------------------------")
def print_clear():
    clear = 50
    while clear > 0:
        print()
        time.sleep(0.01)
        clear -= 1

while True:
    print_line()
    print("Please select your language/Bitte wähle deine Sprache aus...")
    print("(1) English\n(2) Deutsch")
    print_line()
    lang = input("#bash: ")

    if lang == "1":
        from text_en import *
        break
    elif lang == "2":
        from text_de import *
        break
    else:
        print_line()
        print("Input incorrect/Eingabe ungültig...")

random_code = "1"
mode = 0
seconds = 0
user_code = 0
random_code_choice = 0
user_score = 0
set_mode = 0
difficulty = 0
false_difficulty = 0
num_mode = "1234567890"

animation(0.2)
print("\nProgramm started!")

while True:
    # main screen
    while True:
        false_difficulty = 0
        print_line()
        print_logo()
        print("Code'nt Copyright (C) 2023 Flasche-Chris")
        print_line()
        print_mainscreen()
        setting_select = input("#bash: ").capitalize()
        # select difficulty
        if setting_select == "1":
            print_line()
            print("Level:")
            print_level_select()
            difficulty = input("#bash: ")
            animation(0.2)
            print_clear()
            break
        # Print the manual
        elif setting_select == "2":
            print_line()
            print_introduction()
            print_menu_advice()
            input()
        # Print the credits
        elif setting_select == "3":
            print_line()
            print_credits()
            print_menu_advice()
            input()
        elif setting_select == "4":
            exit()
        elif setting_select == "Besenkammer":
            print_line()
            print("Besenkammer forever!!!")
            input()
        elif setting_select == random_code:
            print_clear()
            print_line()
            print("Error! Game can't run properly...\nRestart in progress")
            print_line()
            animation(0.5)
            num_mode = "01"
            print("\nProgramm started!")
            time.sleep(3)
            print_line()
            print_safemode_advice()
        elif setting_select == 'Run -fuck_mode':
            difficulty = "500"
            print_clear()
            break
        elif setting_select == 'Test -animation':
            animation(0.5)
        else:
            error_code = 4
            random_code = ""
            while error_code > 0:
                random_code_choice = random.choice(num_mode)
                random_code = random_code + random_code_choice
                error_code -= 1
            print_line()
            print_incorrect_input(random_code)


    if difficulty == "1":
        false_difficulty = 0
        set_mode = 4
        set_time = 3
        set_points = 0.5
    elif difficulty == "2":
        false_difficulty = 0
        set_mode = 6
        set_time = 5
        set_points = 1
    elif difficulty == "3":
        false_difficulty = 0
        set_mode = 8
        set_time = 7
        set_points = 1.5
    elif difficulty == "4":
        false_difficulty = 0
        set_mode = 12
        set_time = 10
        set_points = 2
    elif difficulty == "500":
        false_difficulty = 0
        set_mode = 50
        set_time = 5
        set_points = 500
    else:
        false_difficulty = 1
        error_code = 4
        random_code = ""
        while error_code > 0:
            random_code_choice = random.choice(num_mode)
            random_code = random_code + random_code_choice
            error_code -= 1
        print_line()
        print_incorrect_input(random_code)
        print_line()



    if false_difficulty < 1:
        print("Ready...")
        time.sleep(1)
        print("Set...")
        time.sleep(1)
        print("Zapp!")
        time.sleep(0.5)
        print_clear()
        user_score = 0
        while True:
            random_code_temp = 0
            random_code_temp = random.sample(num_mode,mode)
            random_code = "".join(random_code_temp)
            print(random_code)
            print("---------")
            t_end = time.time() + set_time
            user_code = input()
            if time.time() < t_end:
                if user_code == random_code:
                    print("passed...")
                    user_score += set_points
                else:
                    print_line()
                    print_wrong_code()
                    print_line()
                    print_score(user_score, difficulty)
                    print_line()
                    print_menu_advice()
                    input()
                    print_clear()
                    break
            else:
                print_line()
                print_too_long()
                print_line()
                print_score(user_score, difficulty)
                print_line()
                print_menu_advice()
                input()
                print_clear()
                break









