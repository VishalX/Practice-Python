# Exception Handling with 'try' & 'except'
print('\nUsing "try" and "except" to handle exceptions')
# Read user input and convert it to floating point value
inp = input('\nEnter a number : ')
# Convert it to float
inp_real = None
# User input comes as string. If string can't be converted to float, program stops execution
# Use try block to check these kind of cases and 
# Use except to Handle these errors without breaking program execution.
try:
    inp_real = float(inp) 
except:
    print('Error: Invalid Input')
    quit()

print("New Number :", inp_real * 2)