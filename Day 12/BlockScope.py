
# There is no Block Scope in Python 

    # Example of this

game_level = 3

## Before: 

#enemies = ["Skeleton", "Zombie", "Alien"]
#if game_level < 5:
    #new_enemy = enemies[0]

#print(new_enemy)

## After: 

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

