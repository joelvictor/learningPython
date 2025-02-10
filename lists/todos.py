# Todo List Exercise
# Create an interactive, text-based todo list that has the following features:
# A user can add todos by entering them into the prompt
# A user can complete todos by entering the todo’s corresponding number
# A user can view a help screen by typing ‘h’ or ‘help’
# A user can quit by typing ‘q’ or ‘quit
# When a user first runs the script, there are no todos in the list.  They can add one by simply entering it into the prompt as seen below (user input is in green)
#   _____         _           
#  |_   _|__   __| | ___  ___ 
#    | |/ _ \ / _` |/ _ \/ __|
#    | | (_) | (_| | (_) \__ \
#    |_|\___/ \__,_|\___/|___/


header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos = []
completed = []
while True:
    if todos:
        for i in range(len(todos)):
            print(f"{i+1}) {todos[i]}")

    command = input("Enter a command. Type 'h' for help: ")
    if command == 'q':
        break
    if command == 'h':
        help = """# To add a todo to the list, type it and hit enter
# To complete a todo enter its number """
        command = input(help)
        if command.isnumeric():
            index = int(command) -1
            if index < len(todos):
                completed.append(todos[index])
                todos.pop(index)
                if not todos:
                    print(f"# Today you completed {len(completed)} todos: ")
                    for i in range(len(completed)):
                        print(f"{i+1}) {completed[i]}")
                    break
                continue
    todos.append(command)
        
                            

# ***********************************
# Enter a command. Type 'h' for help: 
# > walk dog
# 1) walk dog
# ***********************************
# Enter a command. Type 'h' for help: 
# > wash dog
# 1) walk dog
# 2) wash dog
# ***********************************
# Enter a command. Type 'h' for help: 
# > edit video 
# 1) walk dog
# 2) wash dog
# 3) edit video
# ***********************************
# Enter a command. Type 'h' for help: 
# >
# ​
# As you can see, each todo in the list is displayed to the user along with a corresponding number.  A user can enter that number to complete a specific todo:
# 1) walk dog
# 2) wash dog
# 3) edit video
# ***********************************
# Enter a command. Type 'h' for help: 
# > 2
# 1) walk dog
# 2) edit video
# ***********************************
# ​
# A user can type ‘h’ or ‘help’ to view a help menu:
# Enter a command. Type 'h' for help: 
# > h
# TODO LIST HELP
# Type 'q' to quit
# To add a todo to the list, type it and hit enter
# To complete a todo enter its number
# ​
# A user can type ‘q’ or ‘quit’ to quit the app.  The script should display any completed todos in a summary after a user quits:
# Enter a command. Type 'h' for help: 
# > q
# Today you completed 5 todos: 
# * wash dog
# * walk dog
# * walk fish
# * edit video
# * cook dinner