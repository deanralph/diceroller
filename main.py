# Dependancys

import random

# Functions

def printHeader():
    print("""
██████╗░██╗░█████╗░███████╗  ██████╗░░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░  ██████╗░
██╔══██╗██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗  ╚════██╗
██║░░██║██║██║░░╚═╝█████╗░░  ██████╔╝██║░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝  ░░███╔═╝
██║░░██║██║██║░░██╗██╔══╝░░  ██╔══██╗██║░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗  ██╔══╝░░
██████╔╝██║╚█████╔╝███████╗  ██║░░██║╚█████╔╝███████╗███████╗███████╗██║░░██║  ███████╗
╚═════╝░╚═╝░╚════╝░╚══════╝  ╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚══════╝

███████╗██╗░░░░░███████╗░█████╗░████████╗██████╗░██╗░█████╗░
██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║██╔══██╗
█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░██████╔╝██║██║░░╚═╝
██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░██╔══██╗██║██║░░██╗
███████╗███████╗███████╗╚█████╔╝░░░██║░░░██║░░██║██║╚█████╔╝
╚══════╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░

██████╗░░█████╗░░█████╗░░██████╗░░█████╗░██╗░░░░░░█████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██║░░░░░██╔══██╗██╔══██╗
██████╦╝██║░░██║██║░░██║██║░░██╗░███████║██║░░░░░██║░░██║██║░░██║
██╔══██╗██║░░██║██║░░██║██║░░╚██╗██╔══██║██║░░░░░██║░░██║██║░░██║
██████╦╝╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║███████╗╚█████╔╝╚█████╔╝
╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░""")

def buildWeaponProfile():
    weapon = {}
    print("Lets build the weapons profile")
    print()
    weapon["name"] = input("    What's the weapon called /(optional/): ")
    weapon["shots"] = input("    How many shots does this weapon have: ")
    weapon["strength"] = input("    What is The strength of the weapon: ")
    weapon["damaage"] = input("    What is the damage profile: ")
    weapon["ap"] = input("    What is the AP of the weapon: ")
    return weapon

def rollDice(noOfDice, successRoll):
    x = 0
    for dice in range(1, noOfDice):
        if random.randint(1, 6) >= int(successRoll):
            x += 1
    return x

def buildTargetProfile():
    target = {}
    print("Now lets build the target profile")
    print()
    target["name"] = input("    What's the target called /(optional/): ")
    target["toughness"] = input("    What is the taragets toughness: ")
    target["save"] = input("    What is the normal save: ")
    target["invun"] = input("    What is the tragets invun save: ")
    return target

def strengthToughness(stren ,tou):
    if stren == tou:
        return 4
    if stren >= (int(tou) * 2):
        return 2
    if stren <= (int(tou) / 2):
        return 6
    if stren > tou:
        return 3
    if stren < tou:
        return 5

def multipleDamage(damageProfile):
    if "+" in damageProfile:
        nod = damageProfile.split("+")
        nod2 = nod[0].split("d")
        return int(nod[1]) + int(random.randint(1, int(nod2[1])))
    if "d" in damageProfile:
        nod = damageProfile.split("d")
        return random.randint(1, int(nod[1]))
    else:
        return damageProfile

def adjustSave(normalSave, invulSave, AP):
    adjustedsave = 0

    if AP == "":
        adjustedsave = int(normalSave) + int(AP)

    elif int(invulSave) < int(normalSave):
        adjustedsave = invulSave
    
    elif int(invulSave) < (int(normalSave) + int(AP)):
        adjustedsave = invulSave

    else:
        adjustedsave = int(normalSave) + int(AP)

    return adjustedsave

def rerolls(result, toreroll):
    if result < toreroll:
        return random.randint(1, 6)
    else:
        return result
    
def specialRules():
    print("Are there any special rules?")
    print()
    print("    1: Re-roll 1s to hit")
    print("    2: Re-roll all failed hits")
    print("    3: Re-roll 1s to wound")
    print("    4: Re-roll all failed to wound rolls")
    print("    5: +1 to hit")
    print("    6: +1 to wound")
    print()
    return input("Please enter number of special rule /(Or leave blank for no rules/): ")

# Main Code:

# printHeader()
# print()
# wp = buildWeaponProfile()
# print()
# tg = buildTargetProfile()
# ws = wp["strength"]
# tt = tg["toughness"]
# print (f"needed to wound {strengthToughness(4, 8)}")
# print (multipleDamage("d6+4"))
# print(adjustSave(2, 5, 2))
# print(rerolls(4, 5))
print(specialRules())
