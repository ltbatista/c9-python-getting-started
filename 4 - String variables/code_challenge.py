# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase

fname = input("\nInput your first name: ")
lname = input("Input your last name: ")

print("\nYour name: {}".format(fname.capitalize() +" "+
                                lname.capitalize()))



