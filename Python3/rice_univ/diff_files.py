""" Functions to check first occurennce of difference in every line """

# Define value for identical lines
IDENTICAL = -1

def line_diff(line1, line2):
    """
    Checks and returns the first occurence of the differences
    """
    len1 = len(line1)
    len2 = len(line2)
    if len1 < len2:
        short_line = line1
    else:
        short_line = line2
    
    first_diff_pos = IDENTICAL
    for idx in range(len(short_line)):
        if line1[idx] != line2[idx]:
            first_diff_pos = idx
            return first_diff_pos

    if (len1 == len2):
        return IDENTICAL
    else:
        return len(short_line)

def print_line_diff(line1, line2, pos):
    """
    Prints a formatted string showing the first occurence of difference
    """
    if pos == IDENTICAL: return None
    # Print 
    print("")
    print(line1.rstrip())
    print('{:=>{spaces}}'.format("^", spaces=pos+1))
    print(line2.rstrip())
    print("")

# Caller function
if __name__ == "__main__":
    fname1 = "G:\\GitHub\\Data\\file6.txt"
    fname2 = "G:\\GitHub\\Data\\file10.txt"

    fhand1 = open(fname1)
    fhand2 = open(fname2)

    lines1 = fhand1.readlines()
    lines2 = fhand2.readlines()

    print(lines1)
    print(lines2)

    # Check Line difference
    for idx in range(50):#len(lines1)):
        try:
            line1 = lines1[idx]
        except:
            line1 = ""
        try:
            line2 = lines2[idx]
        except:
            line2 = ""
        print("Line", idx+1, ":")

        firstpos = line_diff(line1, line2)
        if firstpos == IDENTICAL:
            print("--- IDENTICAL ---")
        else:
            print_line_diff(line1, line2, firstpos)