import os
from tkinter import filedialog
import json

#steamLoc = ["C:\Program Files (x86)\Steam\steamapps\common","D:\Windows\Steam\steamapps\common"]
steamLoc = []
steamGames = []
#battleNetLoc = ["D:\Windows\BattleNet"]
battleNetLoc = []
battleNet = []
originLoc = []
origin = []
uplayLoc = []
uplay = []

def export():
    locations = {}
    locations["battleNet"] = battleNetLoc
    locations["steam"] = steamLoc
    locations["origin"] = originLoc
    locations["uplay"] = uplayLoc
    with open('libraries.json', 'w') as json_file:
        json.dump(locations, json_file)

def steamAdd():
    steamLoc.append(filedialog.askdirectory())

def battleAdd():
    battleNetLoc.append(filedialog.askdirectory())

def originAdd():
    originLoc.append(filedialog.askdirectory())

def uplayAdd():
    uplayLoc.append(filedialog.askdirectory())

def location():
    ans = "blah"
    while ans != "finish":
        print("Game Library Input, please select an option:")
        print("Steam")
        print("Origin")
        print("BattleNet")
        print("Uplay")
        print("JSON")
        print("Export")
        print("finish")
        ans = input("")
        if ans == "Steam":
            steamAdd()
        if ans == "BattleNet":
            battleAdd()
        if ans == "Origin":
            originAdd()
        if ans == "Uplay":
            uplayAdd()
        if ans == "Export":
            export()

def find():
    for i in steamLoc:
        found = os.listdir(i)
        for j in found:
            steamGames.append(j)
    for i in battleNetLoc:
        found = os.listdir(i)
        for j in found:
            battleNet.append(j)
    for i in originLoc:
        found = os.listdir(i)
        for j in found:
            origin.append(j)
    for i in uplayLoc:
        found = os.listdir(i)
        for j in found:
            uplay.append(j)

    print("Steam Games Found across all Drives:\n")
    for i in steamGames:
        print(i)
    print("\nBattle.Net Games Found across all Drives:\n")
    for i in battleNet:
        print(i)
    print("\nUplay Games Found across all Drives:\n")
    for i in uplay:
        print(i)
    print("\nOrigin Games Found across all Drives:\n")
    for i in origin:
        print(i)

def main():
    location()
    find()

main()
