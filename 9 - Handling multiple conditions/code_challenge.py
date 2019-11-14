# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

name = input('Input your first name: ')

flname = name[0:1]

if flname.upper() == 'A' or flname.upper() == 'B':
    print('Please, go to AB room.')
elif flname.upper() == 'C':
    print('Please, go to CD room.') 
else: 
    lname = input('Please, input your last name: ')
    if lname[0:1].upper() == 'Z':
        print('Please, go to Z room.')
    else:
        print('Please, go to the OTHER room.') 
