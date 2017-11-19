#Simple script to normalzie the given train and test files
#Run with the command ./run.sh

python normalize.py pp5i_train.gr.csv train.txt;
mv train.txt pp5i_train.gr.csv;
python normalize.py pp5i_test.gr.csv test.txt;
mv test.txt pp5i_test.gr.csv;
