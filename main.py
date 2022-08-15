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
    weapon["name"] = input("    What's the weapon called (optional): ")
    weapon["bs"] = input("    Whats  the Balistics Skill: ")
    weapon["shots"] = input("    How many shots does this weapon have: ")
    weapon["strength"] = input("    What is The strength of the weapon: ")
    weapon["damage"] = input("    What is the damage profile: ")
    weapon["ap"] = input("    What is the AP of the weapon: ")
    return weapon

def buildWeaponProfileForTesting():
    weapon = {}
    print("Lets build the weapons profile")
    print()
    weapon["name"] = "Test Cannon"
    weapon["bs"] = 4
    weapon["shots"] = 3
    weapon["strength"] = 14
    weapon["damage"] = "d6+4"
    weapon["ap"] = 4
    return weapon

def rollDice(noOfDice, successRoll):
    x = 0
    for dice in range(0, noOfDice):
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

def buildTargetProfileForTesting():
    target = {}
    print("Now lets build the target profile")
    print()
    target["name"] = "Test Target"
    target["toughness"] = 8
    target["save"] = 3
    target["invun"] = 5
    return target

def strengthToughness(stren ,tou):
    if stren == tou:
        return 4
    if int(stren) >= (int(tou) * 2):
        return 2
    if int(stren) <= (int(tou) / 2):
        return 6
    if int(stren) > int(tou):
        return 3
    if int(stren) < int(tou):
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

printHeader()
print()
# wp = buildWeaponProfile()
# print()
# tg = buildTargetProfile()
wp = buildWeaponProfileForTesting()
print()
tg = buildTargetProfileForTesting()
ws = wp["strength"]
tt = tg["toughness"]
toWound = strengthToughness(ws, tt)
actualSave = adjustSave(tg["save"], tg["invun"], wp["ap"])
damage = 0
y = 1
ave = []
for _ in range(1,1000):
    y = 1
    while damage < 24:
    # for _ in range(1,20):
        hits = rollDice(int(wp["shots"]), int(wp["bs"]))
        wounds = rollDice(hits, toWound)
        saves = rollDice(wounds, actualSave)
        fails = wounds - saves

        if fails >= 1:
            for x in range (1, fails):
                damage += multipleDamage(wp["damage"])
        y += 1

        print(f"{hits} hits, {wounds} wounds, {saves} saves & {damage} damage")
        print()
    print(f"It took {y} attemts to kill " + tg["name"])

    ave.append(y)

print("On average, a " + wp["name"] + " will one shot a " + tg["name"] + f" every 1 in {sum(ave) / len(ave)} times")




#print(specialRules())
