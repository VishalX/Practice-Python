# Stop execution of a loop using `break`
print '\nStopping execution of a loop using "Break"'

# Break infinite loop when the condition is met
while True:
    # Define variable : Read for user input
    itvar = int(raw_input('Enter an integer : '))
    if itvar <= 0: # Break when the input is zero or negative
        print '\n* Breaking Bad *\n'
        break
    print 'Running loop again'





