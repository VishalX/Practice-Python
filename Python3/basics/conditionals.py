# Using Condition code in Python
# This is done using reserve word 'if'

# Define a variable : from user input
var = int(input('\nEnter an Integer : '))

# Use if to check certain conditions 
# Single way
print('\nSingle way Conditionals')
if var == 0:
    print('var : Equals to zero')

if var > 0:
    print('var : Greater than zero')

if var < 0:
    print('var : Less than zero')

if var != 0:
    print('var : Not equal to zero')

if var >= 0:
    print('var : Greater than OR equals to zero')

if var <= 0:
    print('var : Less than OR equals to zero')

# Two way 
print('\nTwo way Conditionals')
if var == 0:
    print('var : Equals to zero')
else:
    print('var : Not equal to zero')

# Multi way
print('\nMulti way Conditionals')
if var == 0:
    print('var : Equals to zero')
elif var > 0:
    print('var : Greater than zero')
else:
    print('var : Less than zero')

