# Looping using for
print('\nLooping using for')

# Loop over some statement using `for` : Definite loops
print('\nInitializing Launch Sequence ...')
for iseq in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
    print(iseq)
print('* BOOM * Liftoff !\n')

del iseq

print('\nInitializing Launch Sequence ...')
for iseq in range(10, 0, -1): # 10 to 1 (not 0), with step -1
    print(iseq)
print('* BOOM * Liftoff !\n')



