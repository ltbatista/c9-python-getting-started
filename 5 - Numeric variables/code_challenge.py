# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10


fnumber = input('\nEnter a number: ')
snumber = input('Enter a second number: ')

soma = int(fnumber) + int(snumber)

print('{} + {} = {}'.format(fnumber,snumber,soma))