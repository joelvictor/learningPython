first_name = input("First Name: ")
last_name = input("Last Name: ")

full_name = first_name + last_name

name_formated = f"{first_name} {last_name} with {len(full_name)} characters is "  
if (len(full_name) > 12):
    print(name_formated + "greater Average american name")
elif (len(full_name) == 12):
    print(name_formated + "average american name")
else:
    print(name_formated + "not an average american name")