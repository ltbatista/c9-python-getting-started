# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
# Test your function using named notation with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

def calculator(fnumber, snumber, op):
    if op == 'add':
        result = fnumber + snumber
    elif op == 'subtract':
        result =  fnumber - snumber
    elif op == 'divide':
        if snumber != 0:
            result =  fnumber / snumber
        else:
            result = 'ERROR: invalid valor, zero.'
    else:
        result = 'Incorrect operator'
    return result

a = int(input('Input the first number: '))
b = int(input('Input the second number: '))
op = input('Input the operator (add/subtract/divide): ')

print(calculator(a, b, op))