#
#Filename:
#       extract_test_data.py
#
#Author:
#       Ian Goetting
#
#Description:
#       This program will extract N genes from a test csv file that match the genes present in a topN csv file.
#       The extracted genes will then be written to an output file.
#       The output file will also have a Class row written to it, where the first element is "Class" and the remaining 
#       values are "?" which represent missing class values for each of the test samples.
#
#Input:
#       This program takes 3 command line args: the topN filename, the test_filename, and the output_filename.
#       The output_filename must be different than the topN filename and the test_filename.
#       The expected inputs for this program are pp5i_train.topN.gr.csv, pp5i_test.gr.csv, and out.txt
#
#Output:
#       This program will output a file containing the extracted genes from the test file along with a row containing the 
#       Class label and missing values "?". 


import sys;
import string;

#Function that will extract N genes from the test_file that match the genes present in the topN_file.
#The extracted genes will be written to the output_file.
#The output_file will get an additional row at the end that contains the Class label 
#as well as missing values (?) for each sample in the test data.
def extract_data(topN_filename, test_filename, output_filename):
    topN_file = open(topN_filename, "r");
    test_file = open(test_filename, "r");
    output_file = open(output_filename, "w");
    #Get the gene labels from the first line of the topN file
    topN_gene_labels = string.split(topN_file.readline(),",");
    topN_file.close();
    #Skip the SNO line in the test file
    SNO_line = test_file.readline();
    #Get the number of columns in the test file
    num_cols = len(string.split(SNO_line,","));
    line = test_file.readline();
    while line:
        line_list = string.split(line,",");
        #If the gene name in the test file matches a topN gene name, 
        #write the test file contents for that gene to the output file.
        if line_list[0] in topN_gene_labels:
            output_file.write(line);
        line = test_file.readline();
    test_file.close();
    #Write the Class row, use missing values (?) as the class values for the samples.
    output_file.write("Class");
    for i in range(0,num_cols-1):
        output_file.write(",?");
    output_file.close();


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "ERROR: You must provide the topN filename, the test filename, and the output filename \n e.g. python extract_test_data.py pp5i_train.top15.gr.csv pp5i_test.csv out.txt";
        sys.exit(0);
    elif (sys.argv[1] == sys.argv[3]) or (sys.argv[2] == sys.argv[3]):
        print "ERROR: The output filename cannot be the same as the topN filename or the test filename";
        sys.exit(0);
    else:
        extract_data(sys.argv[1],sys.argv[2],sys.argv[3]);
