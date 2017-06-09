#!/usr/bin/python
# What is the total number of sales and the total sales value 
# from all the stores? Assume there is only one reducer.
import sys

salesTotal = 0
sumTotal = 0.0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue   
    currentKey = data_mapped[0]
    currentSale = float(data_mapped[1]) 
    salesTotal += 1
    sumTotal += currentSale
print "%s\t%s" % (str(salesTotal), str(sumTotal))
