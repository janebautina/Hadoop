#!/usr/bin/python
# Display the number of hits for each different
# file on the Web site.
import sys

numRequests = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue   
    currentKey = data_mapped[0]
    currentRequest = data_mapped[1] 
    if currentKey == "10.99.99.186":
        numRequests += 1
	print "%s\t%s" % (currentKey, currentRequest)
print "%s" % (str(numRequests))
