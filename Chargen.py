#!/bin/Python3
import math

def races():
    placeholder



def Skills():
    baseSkills = {}


def abilityModifier(abilityScore):
    # calculates ability mod based on the ability score given
    # ability mod formula is (A/2)-5 or (A-10)/2
    baseScore = math.trunc((abilityScore / 2) - 5)
    int(round(baseScore))
    return int(baseScore)


charAbilities = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
# abilityModifiers = {0:'N/A', 1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8}

print("What score to test?")
testScore = int(input())
testModifier = abilityModifier(testScore)

print(testScore + "selected at the test modifier. " + testModifier)

