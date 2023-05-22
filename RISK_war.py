import random

def roll_dice(offense, defense):
    red_roll = []
    for i in range(min(offense, 3)):
        red_roll.append(random.randrange(1, 7))

    red_max = max(red_roll)

    blue_roll = []
    for i in range(min(defense, 2)):
        blue_roll.append(random.randrange(1, 7))

    blue_max = max(blue_roll)
    
    return (red_max, blue_max)

def find_winner(offense, defense):
    red, blue = roll_dice(offense, defense)

    if red > blue:
        return 'offense'
    return 'defense'

def war(offense, defense):
    '''war(offense, defense) -> None
    prints the troops left after a war in RISK in formatted as
    (offense, defense).'''
    while offense > 0 and defense > 0:
        winner = find_winner(offense, defense)
        if winner == 'offense':
            defense = defense - 1
        else:
            offense = offense - 1

    print(offense, defense)