# Step 1
# In this workshop, you will practice how to use booleans and conditional statements in Python by building a movie ticket booking calculator.

# Begin by declaring variables that store information about the user and the movie show.

# Create a variable named base_price to store the base price of the movie ticket and set its value to 15. Create another variable named age to store the user's age and set its value to 21.
#
base_price = 15
age = 21

# Step 2
# Now you need to store some string values about the movie ticket.

# Create a variable named seat_type to store the type of seat the user has selected and set its value to the string Gold. Create another variable named show_time to store the show time of the movie and set its value to the string Evening.
seat_type = "Gold"
show_time = "Evening"

# Step 3
# As you learned in previous lessons, in Python, an if statement can be used to run code depending on if a condition is true.

# An if statement consists of the if keyword, followed by a condition and a colon. The code to run when the condition is true, which must be indented, is called the body of the if statement.

# Example Code
# if condition:
    # Code to execute if condition is True
# A condition is often a comparison between two values. The greater than operator, >, evaluates to True when the left value is greater than the right value, and False otherwise:

# Example Code
# score = 85
# print(score > 70) # True
# print(score > 90) # False
# Because a comparison returns a True or False value, you can use it directly as the condition of an if statement:

# Example Code
# if score > 70:
    # print('You passed')
# In this step, you will check if the user is eligible to book a movie ticket based on their age.

# Create an if statement to check if age is greater than 17. Inside the body of the if statement, print User is eligible to book a ticket. This will print the message only when the user's age is greater than 17.

# Remember to indent the body of the if statement and surround the message with single or double quotes inside the print() call.
if age > 17:
    print("User is eligible to book a ticket")

# Step 4
# The greater than or equal operator (>=) checks whether the value on its left is greater than or equal to the value on its right. Unlike the greater than operator (>), >= also evaluates to True when the two values are equal:

# Example Code
# score = 50
# print(score > 50) # False
# print(score >= 50) # True
# Now you will check whether the user is allowed to book an evening show based on their age.

# Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print User is eligible for Evening shows.
if age >= 21:
    print("User is eligible for Evening shows")

# Step 5
# In the previous step, you checked a condition using an if statement. The else clause is used to handle the case when the condition is false. Here's the syntax of an if...else statement:

# Example Code
# if condition:
    # Code to execute if condition is True
# else:
    # Code to execute if condition is False
# Now, add an else clause to your if statement and print User is not eligible for Evening shows inside the else body. This will print only when the condition in the if statement is false.
else:
    print("User is not eligible for Evening shows")
