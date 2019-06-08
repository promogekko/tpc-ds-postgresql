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

  print("TRUNCATE table...",table)
  cmd= "psql test-tpc -q -c 'TRUNCATE {}'".format(table)
  os.system(cmd )

  print("Loading  data file...",f )
  cmd= """psql test-tpc -c "copy {} FROM '{}' CSV DELIMITER '|' "  """.format(table, f)
  os.system(cmd )


 #  #psql tpcds -q -c "TRUNCATE $table"
 #  #psql tpcds -c "\\copy $table FROM '$i' CSV DELIMITER '|'"

