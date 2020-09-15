import random
def coin():
    r = random.randint(1,2)
    return "heads" if r == 2 else "tails"

def dice():
    r = random.randint(1,6)
    return r

x = input("flip a coin or roll a dice: ")
counter = False
# while not isinstance(x, str) and x == None:
#    x = input("Please enter coin or dice: ")

while counter == False:
    if x.lower() == "c" or x.lower() == "coin":
        print(coin())
        counter = True

    elif x.lower() == "d" or x.lower() == "dice":
        print(dice())
        counter = True
    else:
        x = input("Please enter coin or dice: ")
