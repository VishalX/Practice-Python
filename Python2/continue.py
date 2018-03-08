# Skip next instruction in a loop using `continue`
print '\nSkip instructions of a loop iteration using "continue"'

while True:
    # Define variable : Read for user input
    val = int(raw_input('Enter an integer : '))
    if val > 10:
        print 'Not printing value'
        continue # Go back to "while True:"
    elif val <= 0:
        break    # Break loop
    else:
        val = val + 1 # Increment val
    print val         # Print val
