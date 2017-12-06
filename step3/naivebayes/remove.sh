#!/bin/bash
#
#Script to remove the pp5i_test.bestN.csv file and pp5i_train.bestN.csv file
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
        echo "No argument for N was supplied! Use the command \"./remove.sh N\" where N is the N from your topN train file."
        exit 1
fi

N=$1
rm -f pp5i_train.best"$N".csv pp5i_test.best"$N".csv;
