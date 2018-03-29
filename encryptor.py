import sys

fname = sys.argv[1]
stage = int(sys.argv[2])

if stage==1:
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = "".join(content)
    print(content)
