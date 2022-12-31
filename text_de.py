def print_mainscreen(points):
    print("Deine Punkte:", points, "\n(1) Spiel starten\n(2) Anleitung\n(3) Credits\n(4) Beenden")

def print_level_select():
    print("(1) Einfach | 4-Stelliger  Code  | 3  Sekunden  Zeit  | 0,5 Punkt  pro Code")
    print("(2) Mittel  | 6-Stelliger  Code  | 5  Sekunden  Zeit  | 1   Punkt  pro Code")
    print("(3) Schwer  | 8-Stelliger  Code  | 7  Sekunden  Zeit  | 1,5 Punkte pro Code")
    print("(4) Legende | 12-Stelliger Code  | 10 Sekunden  Zeit  | 2   Punkte pro Code")

def print_introduction():
    print("Hey, willkommen bei Code'nt!\n\nBei Code'nt geht es darum schnell und genau zu sein!\n"
          "Dir wird am Bildschirm ein Numerischercode angezeigt, diesen musst du innerhalb der vorgegeben Zeit eingeben und mit Enter "
          "bestätigen. Das war's!\nLänge des Codes, sowie die Zeit und die Punkte die du bekommst unterscheiden sich vom"
          "ausgewählten Schwierigkeitsgrad her!\nDas Spiel endet sofort, wenn der Code nicht korrekt oder die Zeit abgelaufen ist.\n"
          "(Kleiner Tipp, am besten spielt sich Code'nt mit einem Numpad)"
          "\n\nUnd nun, viel Spaß bei Code'nt!\n")

def print_menu_advice():
    print("(Enter) Hauptmenü")

def print_credits():
    print("Code'nt!\nErstellt von: @Flasche_Chris\nProgrammiersprache: Python 3.10\nBibliotheken: Random, Sys und Time"
          "\nErstelldatum: 25.12.2022\nDonation via PayPal: https://paypal.me/christianx2811\nLoading animation: @ParthChawla on replit"
          "\nDankeschön an: RBBK Dortmund\n01000110010011110101001101001001001100010011000101100001\n"
          "Code'nt Copyright (C) 2023 Flasche-Chris\nThis program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n"
          "For more information, please read the LICENSE.md!")

def print_safemode_advice():
    print("Aufgrund eines Fehlers, wurde das Spiel im Safemode gestartet...\n"
          "Die Codes bestehen nur aus 0 und 1!")

def print_incorrect_input(code):
    print("Input ungültig... incorrect:", code)

def print_wrong_code():
    print("Der Code ist falsch! Das Spiel ist vorbei...")

def print_too_long():
    print("Du warst zu langsam! Das Spiel ist vorbei...")

def print_score(points, level):
    print("Deine Punkte:", points, "\nDein Level:", level)