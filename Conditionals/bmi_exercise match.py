# # BMI Exercise

# Create a simple script that calculates a user’s body mass index.  

# 1. Prompt a user to enter their height (in inches) and their weight (in pounds).  
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

# 2. Next, calculate their BMI using the formula: **(weight in pounds x 703) / (height in inches x height in inches)**
bmi = float((weight * 703) / (height **2))

bmi = round(bmi, 1) #THIS IS THE BONUS! Rounding the BMI to 1 decimal place
formated_bmi = "{:.2f}".format(bmi) #This is another way to round the BMI to 1 decimal place


# 3. Output a message including their BMI number and category according to the following table:
msg = f"Your BMI of  makes you {bmi} "
match bmi:
    case bmi if bmi < 16.0:
        print(msg + "Severely Underweight")
    case bmi if 16.0 <= bmi < 18.4:
        print(msg + "Underweight")
    case bmi if 18.5 <= bmi < 24.9:
        print(msg + "Normal")
    case bmi if 25.0 <= bmi < 29.9:
        print(msg + "Overweight")
    case bmi if 30.0 <= bmi < 34.9:
        print(msg + "Moderately Obese")
    case bmi if 35.0 <= bmi < 39.9:
        print(msg + "Severely Obese")
    case _:
        print(msg + "Morbidly Obese")
# > **< 16.0**    Severely Underweight 
# **16.0 - 18.4**   Underweight
# **18.5 - 24.9**   Normal
# **25.0 - 29.9**   Overweight
# **30.0 - 34.9**   Moderately Obese
# **35.0 - 39.9**   Severely Obese
# **> 39.9**   Morbidly Obese
# > 

# Here’s an example of the script running (user input is in green) : 

# ```
# enter your height in inches: **74**
# enter your weight in lbs: **130**
# Your BMI of 16.68918918918919 makes you Underweight
# ```

# Another example:

# ```
# enter your height in inches: **69**
# enter your weight in lbs: **140**
# Your BMI of 20.67212770426381 makes you Normal
# ```

# And one more example:

# ```
# enter your height in inches: **56**
# enter your weight in lbs: **240**
# Your BMI of 53.80102040816327 makes you Morbidly Obese
# ```

# ### **Bonus**

# The BMI numbers are often really long floats that are ugly to read.  Find a way to round the BMI number to a single decimal place like: `Your BMI of 53.80 makes you Morbidly Obese`