#!/bin/bash
#
#Description:
#       Simple script to normalize the given train and test files
#       Run with the command ./run.sh
#
#IMPORTANT:
#       This script depends on the pp5i_train.gr.csv and pp5i_test.gr.csv files provided in the final_project.zip
#       Those files should be placed in this folder before running this script.

python normalize.py pp5i_train.gr.csv train.txt;
mv train.txt pp5i_train.gr.csv;
python normalize.py pp5i_test.gr.csv test.txt;
mv test.txt pp5i_test.gr.csv;
