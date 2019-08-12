#!/bin/Python3
import math

def CalcModifier(abilityScore):
    # calculates ability mod based on the ability score given
    # ability mod formula is (A/2)-5 or (A-10)/2
    abilityModifier = math.trunc((abilityScore / 2) - 5)
    int(round(abilityModifier))
    if abilityScore == 1:
        abilityModifier = -5
    return int(abilityModifier)

def CharacterDefault():
    # initializing potential variables to try and keep track of what's used and what needs to change
    playerName = "Unnamed Player"
    charName = "Unnamed Character"
    charRace = "Default Race"
    charTheme = "Default Theme"
    charClass = "Default Class"
    charAbilitieScores = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
    charSkills = {"Acrobatics":0, "Athletics":0, "Bluff":0, "Computers":0,
        "Culture":0, "Diplomacy":0, "Disguise":0, "Engineering":0, "Intimidate":0,
        "Life Science":0, "Medicine":0, "Mysticism":0, "Perception":0,
        "Physical Science":0, "Piloting":0, "Sense Motive":0, "Sleight of Hand":0,
        "Stealth":0, "Survival":0, "Profession 1":0, "Profession 2":0}
    charAlignment = "This is useless"
    charArmorClass = 8
    charBaseAttackBonus = 0
    CharCarryCapacity = 0
    CharDiety = "Default Diety"
    charHomeWorld = "Default World"
    charInitiative = 0 # Dex mod + other Misc bonuses
    charLanguages = ["Default Languages"]
    charResolveMax = 0
    charResolveCurrent = 0
    charSavingThrows = {"Fortitude": 0, "Reflex": 0, "Will": 0}
    charSize = "Default Size"
    charSpeed = 30
    charHPMax = 1
    charHPCurrent = 1
    charHPTemporary = 0
    charStamMax = 1
    charStamCurrent = 1
    charLevels = {"Single Class": 0}
    charExpTotal = 0
    charCredits = 0

def RaceSelection():
    racePlanned = input("Have you already decided on a race?\n (Y)es (N)o\n")
    if racePlanned == "y":
        chosenRace = input("What race have you decided to be: ")
    else:


CharacterDefault()

print("~~~Welcome to Hunara's Starfinder Character Creator~~~\nVersion: \"pre-release\"\nRelease Date: August 09, 2019\n\n")
playerName = input("What is the name of the Player for this character: ")
charName = input("What will this character be named: ")

RaceSelection()

print("Player: " + playerName + "\nCharacter: " + charName)