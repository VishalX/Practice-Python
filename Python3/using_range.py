# Range returns a list

# Create a numbered list
numlist = range(5) # By default starts from 0 and increments with 1
# Print
print("Total Numbers : ", len(numlist))
for num in numlist:
    print(num)

# range(start, stop, step)
numlist = range(10, -10, -1)
# Print
print("Total Numbers : ", len(numlist))
for num in numlist:
    print(num)
