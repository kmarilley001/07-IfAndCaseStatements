###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def color_picker(): 
    user_color = input("Enter the name of a color: ")
    if user_color.lower() == "red":
        print("Success! You picked red.")
    elif user_color.lower() == "blue": 
        print("Success! You picked blue!") 
    elif user_color.lower() == "green":
        print("Success! You picked green.")
    elif user_color.lower() == "yellow":
        print("Success! You picked yellow.")
    elif user_color.lower() == "purple":
        print("Success! You picked purple.")
    else:
         print("Unknown Color!")
color_picker()

###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def calculate_grade(percentage):
    if 0.9 <= percentage <= 1.0: 
        return "A" 
    elif 0.8 <= percentage <0.9: 
        return "B" 
    elif 0.7 <= percentage < 0.8: 
        return "C"
    elif 0.6 <= percentage < 0.7: 
        return "D"
    elif 0 <= percentage < 0.6: 
        return "F" 
    else: 
        return "Invalid Score!"
    
def grade(): 
    user_percentage = float(input("Enter your percentage (as a decimal): fe"))
    result = calculate_grade(user_percentage)
    print("Your received a(n)" + result + ".")

grade()
                            
    
