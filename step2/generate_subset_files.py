#
#Filename:
#       generate_subset_files.py
#
#Author:
#       Ian Goetting
#
#Description:
#       This file will create pp5i_train.topN.gr.csv files where N = 2,4,6,8,10,12,15,20,25,30.
#       pp5i_train.topN.gr.csv will contain the top N genes (sorted by T-value desc) found in the five class files for MED, EPD, MGL, RHB, and JPA.
#       Duplicate genes found in one or more of the class files will only be added ONCE to pp5i_train.topN.gr.csv.
#       If there are no duplicates in the top N genes in each of the class files, the total amount of genes in pp5i_train.topN.gr.csv will be 5 * N.
#
#Input:
#       This file takes 6 inputs: The input filename, the T-value MED filename, the T-value EPD filename, the T-value MGL filename, the T-value RHB filename, and the T-value JPA filename.
#       It is expected that the input filename is pp5i_train_removed.gr.csv. That is, the file generated from removed_fold_diff.py.
#       The expected inputs for the T-value filenames are the name of the files generated from compute_T_values.py.
#
#Precondition:
#       It is expected that the T-value files are SORTED in DESCENDING order.
#       That is to say, the gene with the largest T-value is at the top of the file and the gene with the smallest T-value is at the bottom of the file.
#       !!!IMPORTANT!!!: If the T-value files are not sorted prior to being passed to this program, each of the pp5i_train.topN.gr.csv files will contain inaccurate results.
#
#Output:
#       This program will generate 10 pp5i_train.topN.gr.csv files, where N = 2,4,6,8,10,12,15,20,25,30.
#       Each of the files will contain the top N genes (with no duplicates) found in the five given class files.
#       Each pp5i_train.topN.gr.csv file does NOT contain a sample number row as its first row, but it does contain the class labels as the last row.

import sys;
import string;

#Setup a list with the class_labels.
#Order of the list is determined by the file pp5i_train_class.txt
class_labels = [];
for i in range(0,39): class_labels.append("MED");
for i in range(0,7): class_labels.append("MGL");
for i in range(0,7): class_labels.append("RHB");
for i in range(0,10): class_labels.append("EPD");
for i in range(0,6): class_labels.append("JPA");

#Get the next gene from the T_value file
#If it's not in the subset_collection list already, append it as it is not a duplicate
def add_next_gene(class_file, subset_collection):
    line = class_file.readline();
    gene_name = string.split(line,',')[0];
    if gene_name not in subset_collection:
        subset_collection.append(gene_name);

#Function that will generate a pp5i_train.topN.gr.csv file containing the top N genes from each of the T-value files.
def generate_subset_file(input_filename,output_filename,N,MED_filename,EPD_filename,MGL_filename,RHB_filename,JPA_filename):
    input_file = open(input_filename,"r");
    output_file = open(output_filename,"w");
    MED_file = open(MED_filename,"r");
    EPD_file = open(EPD_filename,"r");
    MGL_file = open(MGL_filename,"r");
    RHB_file = open(RHB_filename,"r");
    JPA_file = open(JPA_filename,"r");
    #Skip over the header row in each T-value class file
    MED_file.readline();
    EPD_file.readline();
    MGL_file.readline();
    RHB_file.readline();
    JPA_file.readline();
    #List that will hold the genes that will be written to the output file
    subset_collection = [];
    for i in range(0,N):
        add_next_gene(MED_file,subset_collection);
        add_next_gene(EPD_file,subset_collection);
        add_next_gene(MGL_file,subset_collection);
        add_next_gene(RHB_file,subset_collection);
        add_next_gene(JPA_file,subset_collection);
    #Skip SNO line
    input_file.readline();
    line = input_file.readline();
    #Go through the input file, write genes that are in the subset_collection to the output file
    while line:
        gene_name = string.split(line,',')[0];
        #If the current gene is in the subset collection, write it to the output file
        if gene_name in subset_collection:
            output_file.write(line);
        line = input_file.readline();
    output_file.write("Class");
    for i in range(0,len(class_labels)):
        output_file.write("," + class_labels[i]);
    input_file.close();
    output_file.close();
    MED_file.close();
    EPD_file.close();
    MGL_file.close();
    RHB_file.close();
    JPA_file.close();

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print "ERROR: You must provide the input filename as well as the T_value filenames as command line args. \n e.g. python generate_subset_files.py pp5i_train_removed.gr.csv MED.txt EPD.txt MGL.txt RHB.txt JPA.txt"
        sys.exit(0);
    generate_subset_file(sys.argv[1],"pp5i_train.top2.gr.csv",2,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top4.gr.csv",4,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top6.gr.csv",6,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top8.gr.csv",8,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top10.gr.csv",10,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top12.gr.csv",12,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top15.gr.csv",15,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top20.gr.csv",20,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top25.gr.csv",25,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
    generate_subset_file(sys.argv[1],"pp5i_train.top30.gr.csv",30,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]);
