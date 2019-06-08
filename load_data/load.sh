#!/usr/bin/sh
for i in `ls /tmp/*.dat`; do
  table=${i/.dat/}
  f=""
  file=""
  tab=""
  echo "Loading $table..."
  sed 's/|$//' $i > $f
  sed 's/...//' $f > $file
  sed 's/...//' $table > $tab
  echo "Truncate $tab"
  echo "file ...  $file"
  #psql tpcds -q -c "TRUNCATE $table"
  #psql tpcds -c "\\copy $table FROM '$i' CSV DELIMITER '|'"
done
