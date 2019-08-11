import sys

clArgs = sys.argv

if len(clArgs) > 1:
    wordListFilePath = clArgs[1]
    wordListFilePathTokens = wordListFilePath.split("/")
    wordListFileFolder = "/".join(wordListFilePathTokens[:-1])
    wordListFileName = wordListFilePathTokens[-1]
    fr = open(wordListFileFolder + "/"+wordListFileName, "r")
    fw = open(wordListFileFolder + "/missedWords.txt", "w")
    lines = fr.readlines()
    for line in lines:
        if len(line) > 7:
            fw.write(line[31:-1]+"\n")
    fr.close()
    fw.close()
else:
    print "enter wordlist filename as second argument"

