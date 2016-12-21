from netaddr import *
import sys

if(len(sys.argv) != 2 ):
    print "Usage: python remove_duplicate_cidrs.py input_CIDR_file.txt"
else:
    s = open(sys.argv[1],"r").readlines()
    iplist = []
    for i in s :
        iplist.append(i.split("\n")[0])

    for j in cidr_merge(iplist):
        print j
