import urllib2

contents = urllib2.urlopen("https://mnemonicdictionary.com/?word=abate").read()

print contents


