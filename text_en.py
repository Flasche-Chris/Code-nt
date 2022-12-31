def print_mainscreen(points):
    print("Your points:", points, "\n(1) Start game\n(2) Introduction\n(3) Credits\n(4) Exit")

def print_level_select():
    print("(1) Easy    | 4-digit  code  | 3  seconds  time  | 0,5 points per code")
    print("(2) Medium  | 6-digit  code  | 5  seconds  time  | 1   points per code")
    print("(3) Hard    | 8-digit  code  | 7  seconds  time  | 1,5 points per code")
    print("(4) Legend  | 12-digit code  | 10 seconds  time  | 2   points per code")

def print_introduction():
    print("Hey, welcome to Code'nt!\nCode'nt is all about being fast and accurate!\n"
          "You will be shown a numeric code on the screen, you have to enter it within the given time and confirm it with Enter. "
          "That's it!\nThe length of the code, as well as the time and the points you get differ from the "
          "selected difficulty level!\nThe game ends immediately if the code is not correct or the time is up.\n"
          "(Little tip, the best way to play Code'nt is with a numpad)"
          "\nAnd now, have fun with Code'nt!\n")

def print_menu_advice():
    print("(Enter) Main menu")

def print_credits():
    print("Code'nt!\nVersion: 1.0\nCreated by: @Flasche_Chris\nProgramming language: Python 3.10\nLibrarys: Random, Sys and Time"
          "\nCreationdate: 25.12.2022\nDonation via PayPal: https://paypal.me/christianx2811\nLoading animation: @ParthChawla on replit"
          "\nGreetings to: RBBK Dortmund\n01000110010011110101001101001001001100010011000101100001\n"
          "Code'nt Copyright (C) 2023 Flasche-Chris\nThis program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n"
          "For more information, please read the LICENSE.md!")

def print_safemode_advice():
    print("Due to an error, the game was started in safemode...\n"
          "The codes only contains 0 and 1!")

def print_incorrect_input(code):
    print("Input incorrect... error:", code)

def print_wrong_code():
    print("The code is wrong! The game is over...")

def print_too_long():
    print("You was too slow! The game is over...")

def print_score(points, level):
    print("Your points:", points, "\nYour level:", level)