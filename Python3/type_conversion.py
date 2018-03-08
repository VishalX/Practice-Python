# Convert Basic types of python
print('Basic Type Conversion : No exception handling, don\'t blow up')

# Integer to float and string
var1 = 10
var2 = float(var1)
var3 = str(var1)

var1_type = type(var1)
var2_type = type(var2)
var3_type = type(var3)

print('var1 :', var1, '\t', var1_type)
print('var2 :', var2, '\t', var2_type)
print('var3 :', var3, '\t', var3_type)

# Float to integer and string
var1 = 10.5
var2 = int(var1)
var3 = str(var1)

var1_type = type(var1)
var2_type = type(var2)
var3_type = type(var3)

print('var1 :', var1, '\t', var1_type)
print('var2 :', var2, '\t', var2_type)
print('var3 :', var3, '\t', var3_type)

# String to integer and float
var1 = '10'
var2 = int(var1)    # Can convert without decimal point only 
var1 = '10.5'       # Change value to a string with decimal point
var3 = float(var1)  # Can convert with decimal points

var1_type = type(var1)
var2_type = type(var2)
var3_type = type(var3)

print('var1 :', var1, '\t', var1_type)
print('var2 :', var2, '\t', var2_type)
print('var3 :', var3, '\t', var3_type)

# If needed, numbers in a strings with decimal points, can be converted into float and then to integer
var2 = int(float(var1))
print('var2 :', var2, '\t', var2_type)