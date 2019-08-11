import urllib2
import sys
from timeit import timeit

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def getMnemonics(fw, line):
    word = line[:-1]
    word_length = len(word)
    if word_length > 1:
        #print word
        contents = urllib2.urlopen("https://mnemonicdictionary.com/?word=" + word).read()
        parsed_html = BeautifulSoup(contents, "html.parser")
        body = parsed_html.body
        meaning = body.find('div', attrs={'style':'padding-bottom:0px;'})
        if meaning is not None:
            meaning = meaning.text
        mnemonic = body.find('div', attrs={'class':'card-text'})
        if mnemonic is not None:
            mnemonic = mnemonic.text
        if meaning is not None and mnemonic is not None:
            card_content = meaning + mnemonic
            modified_card_content = card_content.replace("Definition ", "")
            #print modified_card_content.encode('ascii', 'ignore')
            fw.write(word + "\n")
            fw.write(modified_card_content.encode('ascii', 'ignore'))
            fw.write("$@#")
        else:
            print "manually add mnemonic for word " + word


clArgs = sys.argv

if len(clArgs) > 1:
    wordListFilePath = clArgs[1]
    wordListFilePathTokens = wordListFilePath.split("/")
    wordListFileFolder = "/".join(wordListFilePathTokens[:-1])
    wordListFileName = wordListFilePathTokens[-1]
    try:
        fr = open(wordListFileFolder + "/"+wordListFileName, "r")
        fw = open(wordListFileFolder + "/worlist_mnemonics.txt", "w")
        fw2 = open(wordListFileFolder + "/wordlist_timings.txt", "w")
        lines = fr.readlines()
        i = 0
        for line in lines:
            fw2.write(line[:-1] + "\t-\t")
            try:
                fw2.write(str(timeit(lambda: getMnemonics(fw, line), number=1)) + "\n")
            except Error:
                print line
            i += 1
            print i
        fr.close()
        fw.close()
        fw2.close()
    except IOError:
        print "File not found"
else:
    print "enter wordlist filename as second argument"

