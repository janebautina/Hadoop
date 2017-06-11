#!/usr/bin/python

# The number of hits for the file "/assets/js/the-associates.js"
# on the Web site
import sys

numHits = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue   
    currentKey = data_mapped[0]
    currentRequest = data_mapped[1] 
    if currentKey == "/assets/js/the-associates.js":
        numHits += 1
	print "%s\t%s" % (currentKey, currentRequest)
print "%s" % (str(numHits))
