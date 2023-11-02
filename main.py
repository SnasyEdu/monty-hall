import tkinter as tk
from tkinter import ttk

import random

#Wie oft wurde der Button gedrückt?
count = 0

#Wieviele Runden hast du spielt/gewonnen?
played_rounds = 0
winned_rounds = 0

#Welche Tür wurde als erstes angeklickt?
player_door1 = 0

#Welche Tür wurde als zweites angeklickt?
player_door2 = 0

#Welche Tür wird vom Moderator geöffnet?
mod_door = 0

#Welche Tür gewinnt
win_door = 0

def gen_win_door():
    global win_door
    win_door = random.randint(1, 3)

#Welche Tür wird vom Moderator geöffnet
def gen_mod_door():
    global mod_door
    while mod_door == player_door1 or mod_door == win_door or mod_door == 0:
        mod_door = random.randint(1, 3)

#Welchen Befehl soll der Button ausführen
def button_cmd(door):
    global count, player_door1, player_door2, win_door, root, played_rounds, winned_rounds
    count += 1

    if count == 1:
        player_door1 = door
        gen_win_door()
        gen_mod_door()
        mod_label.set(f"Die Tür {mod_door} ist eine Ziege | Gewonne Spiele: {winned_rounds}/{played_rounds}")

    elif count == 2:
        player_door2 = door
        if player_door2 == win_door:
            played_rounds += 1
            winned_rounds += 1
            mod_label.set(f"Du hast gewonnen! | Klicke nochmal auf eine Tür zum neustart | Gewonne Spiele: {winned_rounds}/{played_rounds}")

        else:
            played_rounds += 1
            mod_label.set(f"Du hast verloren! | Die richtige Tür wäre {win_door} gewesen | Klicke nochmal auf eine Tür zum neustart | Gewonne Spiele: {winned_rounds}/{played_rounds}")
    
    else:
        count = 0
        mod_label.set(f"Klicke auf einen Button! | Gewonne Spiele: {winned_rounds}/{played_rounds}")

#3 Funktionen, die man braucht, weil man Button-Commandw nicht mit Paramentern verwenden kann
def door1_cmd():
    button_cmd(1)

def door2_cmd():
    button_cmd(2)

def door3_cmd():
    button_cmd(3)


#Erstelle das Fenster und bearbeite es
root = tk.Tk() #Erstellt das Fenster namens "root"
root.title('Monty-Hall') #Modifiziert den Titel des Hauptfensters
root.resizable(width=False, height=False) #Stellt ein, ob man die Breite/Höhe modifizieren kann


#Erstelle eine Tkinter-Variable namens mod_label
mod_label = tk.StringVar()
mod_label.set("Klicke auf einen Button!")

#Erstelle ein Widget 
mod_widget = ttk.Label(root, textvariable=mod_label)
mod_widget.grid(row=0, column=4, padx=0, pady=10, sticky="w")


#Erstelle die Türen
door1 = ttk.Button(root, text="Tür 1", padding=10, command=door1_cmd)
door2 = ttk.Button(root, text="Tür 2", padding=10, command=door2_cmd)
door3 = ttk.Button(root, text="Tür 3", padding=10, command=door3_cmd)

#Platziere die Türen
door1.grid(row=0, column=1, padx=0, pady=10, sticky="w")
door2.grid(row=0, column=2, padx=0, pady=10, sticky="w")
door3.grid(row=0, column=3, padx=0, pady=10, sticky="w")


#Führe das Programm aus
root.mainloop()
