"""This script converts a WIG format file into 
   a data frame that R can import and plot with
   Bin He
   2020-07-03
"""

# import libraries
import sys
import re

# parse arguments
if len(sys.argv) != 2: # the first element is the program name
    print("python3 wig2rdata.py <WIG>")
    sys.exit()

IN = sys.argv[1] # input file name
OUT = re.sub("\.wig",".faa", IN)

# open the file
f = open(IN, "r")

chr = "chr1" # variable used to store the state of the chromosome number

for line in f: # read data line by line
    x = line.split()
    if x[0].isnumeric():   # first word is a number
        print(chr, x[0], x[1], sep = "\t") # print
    elif x[0] == "variableStep": # definition line
        chr = x[1].split("=")[1] # update chromosome number
    elif x[0] == "track":        # we can ignore lines starting with "track"
        next

f.close()

