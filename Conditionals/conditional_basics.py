# Example of using conditionals with if, elif, and else

# Example 1: Checking if a number is positive, negative, or zero
number = 10

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Example 2: Grading system
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Example 3: Checking age group
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")