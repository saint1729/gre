f = open("scriptOutput.txt", "r")
lines = f.readlines()
for line in lines:
    if len(line) > 7:
        print line[31:-1]
f.close()
