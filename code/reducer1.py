#!/usr/bin/python
# Find the monetary value for the highest individual
# sale for each separate store
import sys

salesMax = 0.0
prevKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    currentKey = data_mapped[0]
    currentSale = float(data_mapped[1]) 
    if prevKey == None:
	   salesMax = currentSale
	   prevKey = currentKey
    else:
    	if prevKey == currentKey:
            if salesMax < currentSale:
    		    salesMax = currentSale
    	else:
    	    print "%s\t%s" % (prevKey, str(salesMax))
            salesMax = float(currentSale)
    	    prevKey = currentKey    
if prevKey != None:
    print "%s\t%s" % (prevKey, str(salesMax))