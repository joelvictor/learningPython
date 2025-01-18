# Toothpicks Exercise
# Implement a version of the “classic” matchsticks/toothpicks two player game.  We start with 13 toothpicks, and plays take turns removing 1, 2, or 3 toothpicks at a time.  The person who removes the last toothpick wins.
# Here’s an example of the gameplay:
# enter player 1's name: Colt
# enter player 2's name: Elton

# | | | | | | | | | | | | | 
# There are 13 toothpicks left
# How many do you take, Colt ? 
# 3

# | | | | | | | | | | 
# There are 10 toothpicks left
# How many do you take, Elton ? 
# 2

# | | | | | | | | 
# There are 8 toothpicks left
# How many do you take, Colt ? 
# 3

# | | | | | 
# There are 5 toothpicks left
# How many do you take, Elton ? 
# 1

# | | | | 
# There are 4 toothpicks left
# How many do you take, Colt ? 
# 3

# | 
# There are 1 toothpicks left
# How many do you take, Elton ? 
# 1

# Elton wins!!!
# GAME OVER!!
# ​
# BONUS: verify that players are only inputting valid numbers of 1, 2, or 3
player_1=input("Enter player 1's name: ")
player_2=input("Enter player 2's name: ")

toothpicks=13
next_turn_player = player_1

while toothpicks > 0:
    next_turn = f"""{'|' *toothpicks}
There are {toothpicks} toothpicks left 
How many do you take, {next_turn_player}? """
    remove_toothpicks=input(next_turn)
    while not remove_toothpicks.isdigit() or int(remove_toothpicks) < 1 or int(remove_toothpicks) > 3 or int(remove_toothpicks) > toothpicks:
        remove_toothpicks = input(next_turn)

    toothpicks-=int(remove_toothpicks)

    if toothpicks <= 0:
        print(f"""{next_turn_player} wins!!!
GAME OVER!!""")
        break

    if next_turn_player == player_1:
        next_turn_player = player_2
    else:
        next_turn_player = player_1
    
    