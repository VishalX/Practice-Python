# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0
# Read Lines
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cpos = line.find(':')
    cstr = line[cpos+1:]
    nstr = cstr.strip()
    
    if len(nstr) < 1: continue
    try:
        num = float(nstr)
    except:
        continue
    
    total = total + num
    count = count + 1
    
average = total / count
print("Average spam confidence:", average)
