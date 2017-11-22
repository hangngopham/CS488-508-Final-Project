#Remove genes that have fold difference <2
python remove_fold_diff.py pp5i_train.gr.csv out.txt;
mv out.txt pp5i_train.gr.csv;
#Create files holding each class's T-values for each gene
python compute_T_values.py pp5i_train.gr.csv;
#Sort the created files
./sort.sh;

