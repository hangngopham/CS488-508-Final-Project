#
#Filename:
#       transpose.py
#
#Author:
#       Ian Goetting
#
#Description:
#       This program transposes a comma-separated matrix given in an input file, 
#       and writes the result to an output file.
#
#Input:
#       This program takes two inputs: The filename of the input file and the filename of the output file.
#       Both inputs are provided via command line args.
#       The input filename must be different than the output file, and it is expected the output file does not exist already.
#

import sys;
import string;

#Function that transposes the comma-separated matrix that is given in the input file 
#and writes the transposed matrix to the output file.
def transpose(input_filename, output_filename):
    input_file = open(input_filename, "r");
    output_file = open(output_filename, "w");
    #Get the number of columns in the file
    num_cols = len(string.split(input_file.readline(),","));
    #Go through each column,
    for current_col in range(0,num_cols):
        #Set the current line of the input_file back to the beginning of the file
        input_file.seek(0);
        transposed_row = "";
        line = input_file.readline();
        #Go through each row of the file 
        #Concatenate the elements that make up the row to form the transposed row
        while line:
            line = string.split(line, ",");
            #Get the element in the current column at the current row
            element = line[current_col];
            #If element ends with newline, remove the newline
            if element.endswith('\n'):
                element = element[:-1];
            #If element ends with carriage return, remove the carriage return
            if element.endswith('\r'):
                element = element[:-1];
            #Append the element to the row with a comma
            transposed_row += element + ",";
            line = input_file.readline();
        #Remove the ending comma, replace it with a newline
        transposed_row = transposed_row[:-1];
        transposed_row += '\n';
        output_file.write(transposed_row);

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "ERROR: You must provide an input filename and an output filename via command line args. \n e.g. python transpose.py input.txt output.txt"
        sys.exit(0);
    elif sys.argv[1] == sys.argv[2]:
        print "ERROR: The input filename cannot be the same as the output filename."
        sys.exit(0);
    else:
        transpose(sys.argv[1],sys.argv[2])
