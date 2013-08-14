#!/usr/bin/env python

# Produce nicer CSV files for the insult detection problem
# Usage: `./scriptname inputfilename outputfilename`

from __future__ import unicode_literals
from ftfy import fix_text
import sys
import csv

infile = open(sys.argv[1])

outfile = open(sys.argv[2], 'w')
writer = csv.writer(outfile)

for line in infile:
	#splits on commas
  splits = line.split(",")
  #make empty newline
  newline = []
  #add before the first comma and the second comma
  newline.append(splits[0])
  newline.append(splits[1])
  comment = ",".join(splits[2:])
  #make line that starts with common and adds after the second comma. strip the quotes
  #comment = ','.join(splits[2:]).strip().strip('"').strip()
  #replace double quote sequences with single quotes
  #comment = comment.replace('""','"')
  #get rid of all unicode
  try:
    comment = comment.decode("unicode-escape")
  except:
    pass
  try:
    comment = comment.decode("unicode-escape")
  except:
    pass
  try:
    comment = comment.decode("unicode-escape")
  except:
    pass
  #encode as utf8
  comment = fix_text(comment)
  comment = comment.encode("utf-8")
  newline.append(comment)
  writer.writerow(newline)

infile.close()
outfile.close()