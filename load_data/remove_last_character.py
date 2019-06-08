#!/usr/bin/env python

import glob
import os
import re

path='/tmp'

files= [f for f in glob.glob(path+"**/*.dat")]

for f in files:
  m= re.search('(\/tmp\/)(.*)(....)', f)
  table=m.group(2)
  #print table

  m = re.search('(\/tmp\/)(.*)', f)
  data_file=m.group(2)
  #print data_file

  print " Removing last pipe character...{}".format(f)
  cmd="sed 's/.$//' {} | tee /tmp/newvalue.dat && mv /tmp/newvalue.dat {} ".format(f,f)
  os.system(cmd)


