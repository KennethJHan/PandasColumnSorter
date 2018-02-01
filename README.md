# PandasColumnSorter
###### csv, tsv, space delimited column sorter using pandas


## HOW TO USE THIS SCRIPT


####  0) REQUIREMENT
######    - PYTHON
######    - PANDAS LIBRARY

####  1) THIS IS AN EXAMPLE FILE DELIMITED BY TAB.
######    $ cat test1_tab.txt
######    Name    Sample1 Sample2 Sample3
######    1:12345 G/G     G/G     T/G
######    1:67890 C/C     G/C     C/C
######    2:12345 G/T     T/T     T/T
######    3:12345 C/A     A/A     A/A
######    4:12345 A/C     C/C     A/C

####  2) THIS IS A GROUP FILE. WE WILL SORT COLUMNS BY THIS ORDER.
######    $ cat groupfile1.txt
######    Name
######    Sample3
######    Sample2

####  3) RUN COMMAND.
######    - Options:    -f <file>          # File, data file
######                  -H [true/false]    # Header
######                  -S [csv/tsv/space] # Separator
######                  -G <file>          # [Optional] Group File, containing group column information
######    $ PandasColumnSorter.py -f test1_tab.txt -H true -S tsv -G groupfile1.txt
######    Name      Sample3   Sample2
######    1:12345   T/G       G/G
######    1:67890   C/C       G/C
######    2:12345   T/T       T/T
######    3:12345   A/A       A/A
######    4:12345   A/C       C/C

######YOU CAN SORT AND SELECT COLUMNS!
######HAVE FUN :)
