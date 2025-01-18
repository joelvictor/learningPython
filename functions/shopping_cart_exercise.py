# Write a Python script that does the following:

# - Prints out a “banner” to welcome users to our shop
print(" Hello! Welcome to our shop")
# - Asks the user for the name of the item they are buying
item = input("What are you looking for today? ")
# - Asks the user for the price of that item
price = float(input("How much is it? "))
# - Asks the user for the quantity they are purchasing
qtd = int(input("How much itens do you want? "))
# - Prints out a message that includes their subtotal (quantity 𝚡 price)
total = price * qtd
print(f"Added {qtd} {item}(s) by the price {price} to shopping cart")

print(f"Subtotal: {total}")
# **Here’s an example of the script running (the green text is user input)**

# ```
# WELCOME TO OUR USELESS STORE!
# *****************************
# what item are you purchasing?  **taco**
# what is the price of taco?  **2.5**
# how many taco are you buying?  **5**
 
# Added 5 taco(s) to shopping cart
# Subtotal: $12.5
# ```

# **Here’s another example of the script running (the green text is user input)**

# ```
# WELCOME TO OUR USELESS STORE!
# *****************************
# what item are you purchasing?  **cotton candy** 
# what is the price of cotton candy?  **1.35**
# how many cotton candy are you buying?  **8**
 
# Added 8 cotton candy(s) to shopping cart
# Subtotal: $10.8
# ```

# **Gotchas:**

# - Make sure to convert user input to numbers when needed!
# - Use an f-strings when printing out the final total