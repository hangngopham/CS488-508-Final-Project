#
#Filename:
#       normalize.py
#
#Author:
#       Ian Goetting 
#
#Description:
#       This program will normalize a comma delimited input file by thresholding all values to be >=20 and <=16000.
#       Any value <20 will be replaced by 20 and any value >16000 will be replaced by 16000.
#       This program assumes that the first line of the input file contains ID labels that are not part of the actual data.
#       Thus, the first line of the file will NOT be normalized.
#Input:
#       This program takes command line arguments. 
#       The first argument is the input filename, the second argument is the output filename.
#       An example command to run this program would be: python normalize.py input.txt output.txt
#       Precondition: It is assumed that the input file already exists, otherwise an error will be generated.
#       The intended input files for this program is pp5i_train.gr.csv and pp5i_test.gr.csv from the final_project_data folder.
#

import sys;
import string;

#Function that will normalize the data in the file given by the input_filename parameter.
#The results of the normalization will be written to the file given by the output_filename parameter.
def normalize(input_filename, output_filename):
    input_file = open(input_filename, "r");
    output_file = open(output_filename, "w");
    #Skip the SNO line.
    SNO_line = input_file.readline();
    output_file.write(SNO_line);
    #Get the first actual line
    line = input_file.readline();
    #Normalize each line in the file
    while line:
        line_elements = string.split(line,',');
        skip_attribute_name = 1;
        #If the next line only has the attribute, or is empty (i.e. only carriage return and newline), skip it
        if len(line_elements) == 1:
            output_file.write(line_elements[0]);
        #Otherwise loop through the elements that make up the line
        else:
            for element in line_elements:
                #Skip the first line in the file since it only contains IDs.
                if skip_attribute_name:
                    skip_attribute_name = 0;
                    output_file.write(element + ",");
                else:
                    new_element = float(element);
                    #Perform normalization; change new_element if it's <20 or >16000
                    if new_element < 20:
                        new_element = 20;
                    elif new_element > 16000:
                        new_element = 16000;
                    #Append carriage return + newline if new_element is the last element in the line
                    #Otherwise append a comma to it.
                    if element.endswith('\r\n'):
                        output_file.write(str(new_element) + "\r\n");
                    else:
                        output_file.write(str(new_element) + ","); 
        line = input_file.readline();
    input_file.close();
    output_file.close();


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "ERROR: An input filename and output filename must be given. e.g. python normalize.py input.txt output.txt";
        sys.exit(0);
    elif sys.argv[1] == sys.argv[2]:
        print "ERROR: The input filename cannot be the same as the output filename!";
        sys.exit(0);
    normalize(sys.argv[1],sys.argv[2]);
