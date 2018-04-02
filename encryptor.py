import sys
import util

fname = sys.argv[1]
stage = int(sys.argv[2])

####### IMPORTANT VARIABLES
factor1 = 7
factor2 = 11
prime = factor1*factor2
exponent = 3

if stage==1:
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    print(content)
