# capitalize() - Converts the first character to upper case
print("hello".capitalize())  # Output: Hello

# casefold() - Converts string into lower case
print("HELLO".casefold())  # Output: hello

# center() - Returns a centered string
print("hello".center(10))  # Output: '  hello   '

# count() - Returns the number of times a specified value occurs in a string
print("hello".count('l'))  # Output: 2

# encode() - Returns an encoded version of the string
print("hello".encode())  # Output: b'hello'

# endswith() - Returns true if the string ends with the specified value
print("hello".endswith('o'))  # Output: True

# expandtabs() - Sets the tab size of the string
print("h\te\tl\tl\to".expandtabs(2))  # Output: 'h e l l o'

# find() - Searches the string for a specified value and returns the position of where it was found
print("hello".find('e'))  # Output: 1

# format() - Formats specified values in a string
print("Hello {}!".format("World"))  # Output: Hello World!

# index() - Searches the string for a specified value and returns the position of where it was found
print("hello".index('e'))  # Output: 1

# isalnum() - Returns True if all characters in the string are alphanumeric
print("hello123".isalnum())  # Output: True

# isalpha() - Returns True if all characters in the string are in the alphabet
print("hello".isalpha())  # Output: True

# isdecimal() - Returns True if all characters in the string are decimals
print("123".isdecimal())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
print("123".isdigit())  # Output: True

# isidentifier() - Returns True if the string is an identifier
print("hello".isidentifier())  # Output: True

# islower() - Returns True if all characters in the string are lower case
print("hello".islower())  # Output: True

# isnumeric() - Returns True if all characters in the string are numeric
print("123".isnumeric())  # Output: True

# isprintable() - Returns True if all characters in the string are printable
print("hello".isprintable())  # Output: True

# isspace() - Returns True if all characters in the string are whitespaces
print("   ".isspace())  # Output: True

# istitle() - Returns True if the string follows the rules of a title
print("Hello World".istitle())  # Output: True

# isupper() - Returns True if all characters in the string are upper case
print("HELLO".isupper())  # Output: True

# join() - Joins the elements of an iterable to the end of the string
print(",".join(["hello", "world"]))  # Output: hello,world

# ljust() - Returns a left justified version of the string
print("hello".ljust(10))  # Output: 'hello     '

# lower() - Converts a string into lower case
print("HELLO".lower())  # Output: hello

# lstrip() - Returns a left trim version of the string
print("   hello".lstrip())  # Output: 'hello'

# maketrans() - Returns a translation table to be used in translations
table = str.maketrans("h", "y")
print("hello".translate(table))  # Output: yello

# partition() - Returns a tuple where the string is parted into three parts
print("hello world".partition(" "))  # Output: ('hello', ' ', 'world')

# replace() - Returns a string where a specified value is replaced with a specified value
print("hello world".replace("world", "there"))  # Output: hello there

# rfind() - Searches the string for a specified value and returns the last position of where it was found
print("hello".rfind('l'))  # Output: 3

# rindex() - Searches the string for a specified value and returns the last position of where it was found
print("hello".rindex('l'))  # Output: 3

# rjust() - Returns a right justified version of the string
print("hello".rjust(10))  # Output: '     hello'

# rpartition() - Returns a tuple where the string is parted into three parts
print("hello world".rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit() - Splits the string at the specified separator, and returns a list
print("hello world".rsplit())  # Output: ['hello', 'world']

# rstrip() - Returns a right trim version of the string
print("hello   ".rstrip())  # Output: 'hello'

# split() - Splits the string at the specified separator, and returns a list
print("hello world".split())  # Output: ['hello', 'world']

# splitlines() - Splits the string at line breaks and returns a list
print("hello\nworld".splitlines())  # Output: ['hello', 'world']

# startswith() - Returns true if the string starts with the specified value
print("hello".startswith('h'))  # Output: True

# strip() - Returns a trimmed version of the string
print("   hello   ".strip())  # Output: 'hello'

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("Hello World".swapcase())  # Output: hELLO wORLD

# title() - Converts the first character of each word to upper case
print("hello world".title())  # Output: Hello World

# translate() - Returns a translated string
table = str.maketrans("h", "y")
print("hello".translate(table))  # Output: yello

# upper() - Converts a string into upper case
print("hello".upper())  # Output: HELLO

# zfill() - Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5))  # Output: 00042