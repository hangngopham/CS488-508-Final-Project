#!/bin/bash
#
#Description: 
#       Script that performs the selection of top genes for step 2 of the project.
#
#IMPORTANT: 
#       This script requires the pp5i_train_removed.gr.csv file generated from step1 of the project.
#       That file can be found in the step1 folder after running the run.sh script found in that folder.

#Remove genes that have fold difference <2
python remove_fold_diff.py pp5i_train.gr.csv out.txt;
mv out.txt pp5i_train_removed.gr.csv;
#Create files holding each class's T-values for each gene
python compute_T_values.py pp5i_train_removed.gr.csv;
#Sort the created files
(head -n 1 T_values_EPD.txt && tail -n +2 T_values_EPD.txt | sort -t , -k 2 -g -r) > EPD_sort.txt;
mv EPD_sort.txt T_values_EPD.txt;
(head -n 1 T_values_JPA.txt && tail -n +2 T_values_JPA.txt | sort -t , -k 2 -g -r) > JPA_sort.txt;
mv JPA_sort.txt T_values_JPA.txt;
(head -n 1 T_values_MED.txt && tail -n +2 T_values_MED.txt | sort -t , -k 2 -g -r) > MED_sort.txt;
mv MED_sort.txt T_values_MED.txt;
(head -n 1 T_values_MGL.txt && tail -n +2 T_values_MGL.txt | sort -t , -k 2 -g -r) > MGL_sort.txt;
mv MGL_sort.txt T_values_MGL.txt;
(head -n 1 T_values_RHB.txt && tail -n +2 T_values_RHB.txt | sort -t , -k 2 -g -r) > RHB_sort.txt;
mv RHB_sort.txt T_values_RHB.txt;
#Generate the pp5i_train.topN.gr.csv files
python generate_subset_files.py pp5i_train_removed.gr.csv T_values_MED.txt T_values_EPD.txt T_values_MGL.txt T_values_RHB.txt T_values_JPA.txt;
#Transpose the pp5i_train.topN.gr.csv files
python transpose.py pp5i_train.top2.gr.csv out.txt;
mv out.txt pp5i_train.top2.gr.csv;
python transpose.py pp5i_train.top4.gr.csv out.txt;
mv out.txt pp5i_train.top4.gr.csv;
python transpose.py pp5i_train.top6.gr.csv out.txt;
mv out.txt pp5i_train.top6.gr.csv;
python transpose.py pp5i_train.top8.gr.csv out.txt;
mv out.txt pp5i_train.top8.gr.csv;
python transpose.py pp5i_train.top10.gr.csv out.txt;
mv out.txt pp5i_train.top10.gr.csv;
python transpose.py pp5i_train.top12.gr.csv out.txt;
mv out.txt pp5i_train.top12.gr.csv;
python transpose.py pp5i_train.top15.gr.csv out.txt;
mv out.txt pp5i_train.top15.gr.csv;
python transpose.py pp5i_train.top20.gr.csv out.txt;
mv out.txt pp5i_train.top20.gr.csv;
python transpose.py pp5i_train.top25.gr.csv out.txt;
mv out.txt pp5i_train.top25.gr.csv;
python transpose.py pp5i_train.top30.gr.csv out.txt;
mv out.txt pp5i_train.top30.gr.csv;

