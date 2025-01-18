# variables without type are defined by None which type is NoneType

first_name = None

print(type(first_name))

# strings can be defined by ' ' or " "
first_name = 'Jon'

last_name = " Macauley" 

#to concate strings use + sign
full_name = first_name +' '+  last_name

print(full_name)

str_multilines=""" multi
lines
"""

print(str_multilines)


str_multilines=f""" formated multi
lines {full_name}
"""

print(str_multilines)

# Escape Characters 
print('Escape Characters ')
# \n - new line 
print("Jump \n line \\n ")
# \t  - tab
print("hello\tworld - tab")
# \" - double quote
# \ - 'single' quote \'
print("\" double quote \' single quote")
# \b - backspace
print("\b backspace")
# \\ backslash
print("\\ backslash")