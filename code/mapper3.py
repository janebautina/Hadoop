#!/usr/bin/python

import sys
import re

# 10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/img/dummy/primary-news-2.jpg HTTP/1.1" 304 -

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
	ip = data[0]
 	used_id = data[1]
	user_name = data[2]
    time = data[3]+ " " + data[4]
    request = data[5] + " " + data[6] + " " + data[7]
    page = data[6]
    status = data[8]
	data_size = data[9]
    print "{0}\t{1}".format(page, ip)
