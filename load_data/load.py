#!/usr/bin/env python

import glob
import re

path='/tmp'

files= [f for f in glob.glob(path+"**/*.dat")]

for f in files:
  m= re.search('(\/tmp\/)(.*)(....)', f)
  table=m.group(2)
  print(table)

  m = re.search('(\/tmp\/)(.*)', f)
  data_file=m.group(2)
  print(data_file)

  print("TRUNCATE table...",table)
  cmd= "psql test-tpcds -q 'TRUNCATE {}'".format(table)
  os.system(cmd )

  print("Loading  data file...",table)
  cmd= "psql test-tpcds -c '\\copy {} FROM {} CVS DELIMITER "|"' ".format(table, data_file)
  os.system(cmd )


 #  #psql tpcds -q -c "TRUNCATE $table"
 #  #psql tpcds -c "\\copy $table FROM '$i' CSV DELIMITER '|'"

