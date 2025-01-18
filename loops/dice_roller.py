# Create a script that rolls dice for a user.  When the script runs, it should ask a user how many dice they want to roll and how many sides each die will have.  Then it randomly rolls those dice and prints the result.  Every time a user hits Enter, the dice are rolled again.  If a user every enter “q”, then the script quits and stops running!

# **Hints:**

# - use `randint()` to generate the dice rolls. Remember, you need to import it from `random`
# - start by rolling a single die before rolling multiple
# - you’ll need to use nested loops!

# Here’s an example of the script in action where the user wanted three 6-sided dice:

# ```
# How many dice are we rolling? **3**
# How many sides on each die? **6**
# |5|1|4|
# Roll again? ('q' to quit) 
# |5|3|1|
# Roll again? ('q' to quit) 
# |2|4|1|
# Roll again? ('q' to quit) **q**
# ```

# The following example rolls two 20-sided die:

# ```
# How many dice are we rolling? **2**
# How many sides on each die? **20**
# |19|20|
# Roll again? ('q' to quit) 
# |6|1|
# Roll again? ('q' to quit) 
# |6|11|
# Roll again? ('q' to quit) 
# |2|13|
# Roll again? ('q' to quit) **q**
# ```

# **Bonus: Ensure that a user enters a valid integer between 1 and 20 and keep prompting a user until they do!**

from random import randint

def get_value_question(question):
    qtd_dice = input(question)
    while not qtd_dice.isdigit() or int(qtd_dice) < 1 or int(qtd_dice) > 20:
        qtd_dice = input(question)

    return int(qtd_dice)


def roll_dice(qtd_dice, side_dice):
    dice_results = "|"
    for _ in range(qtd_dice):
        dice_results += f"{randint(1, side_dice)}|"
    print(dice_results)
    
    return input("Roll again? ('q' to quit) ")

qtd_dice = get_value_question("How many dice are we rolling between 1 and 20? ")
side_dice = get_value_question("How many sides on each die between 1 and 20? ")

quit = roll_dice(qtd_dice, side_dice)

while quit != 'q':
    quit = roll_dice(qtd_dice, side_dice)