import random

def roll():
    return random.randint(1,6)

dice = []
answer = int(input("How many dice do you want to roll: "))
for i in range(answer):
    dice.append(roll())
dice_drawing = {
        1: (
            " ---------",
            "|    1    |",
            "|    o    |",
            "|         |",
            " ---------",
        ),
        2: (
            " ---------",
            "| o       |",
            "|    2    |",
            "|       o |",
            " ---------",
        ),
        3: (
            " ---------",
            "| o  3    |",
            "|    o    |",
            "|       o |",
            " ---------",
        ),
        4: (
            " ---------",
            "| o     o |",
            "|    4    |",
            "| o     o |",
            " ---------",
        ),
        5: (
            " ---------",
            "| o  5  o |",
            "|    o    |",
            "| o     o |",
            " ---------",
        ),
        6: (
            " ---------",
            "| o     o |",
            "| o  6  o |",
            "| o     o |",
            " ---------",
        ),

    }

for i in range(len(dice)):
    print(f"dice rolled {dice[i]}  ")
    print("\n".join(dice_drawing[dice[i]]))