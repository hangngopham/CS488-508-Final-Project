#!/bin/bash
#
#Script to create the pp5i_test.bestN.csv file and pp5i_train.bestN.csv file
#
#IMPORTANT: 
#       This script requires a pp5i_train.topN.gr.csv file generated from step2.
#       These can be found in the step2 folder after running the run.sh script found there. 
#       This script also requires the pp5i_test.gr.csv file generated from step1.
#       That can be found in the step1 folder after running the run.sh script found there.
#
#INPUT: 
#       This script requires you to provide the N value as a command line arg. 
#       This value should be the same as the one in listed in the filename of the topN filename you chose.
#       e.g. if your filename is pp5i_train.top15.gr.csv, then use the command ./run.sh 15. 

#Check an argument was given
if [ $# -eq 0 ]
    then
        echo "No argument for N was supplied! Use the command \"./run.sh N\" where N is the N from your topN train file."
        exit 1
fi

N=$1

#Extract the test data
python extract_test_data.py pp5i_train.top"$N".gr.csv pp5i_test.gr.csv out_test.txt
#Transpose the test data
python ../../step2/transpose.py out_test.txt pp5i_test.best"$N".csv
#Remove the intermediate out_test.txt file
rm -f out_test.txt
#Copy the train topN file to the bestN file
cp pp5i_train.top"$N".gr.csv pp5i_train.best"$N".csv
