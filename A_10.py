import random

dice_number = [1, 2, 3, 4, 5, 6]


def dice():
    return random.choice(dice_number)


print(dice())


# print(random.choice(dice_number))
