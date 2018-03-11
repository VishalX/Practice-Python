# Convert a line to a list of words
# Words in line must be sepated by whitespaces

def line2Words(line):
    # Check line length
    if len(line) < 1:
        return None
    # Split line into words
    words = line.split()
    return words
    # End of function