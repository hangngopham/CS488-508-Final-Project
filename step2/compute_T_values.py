import sys;
import math;
import string;
#Setup a list with the class_labels.
#Order of the list is determined by the file pp5i_train_class.txt
class_labels = [];
for i in range(0,39): class_labels.append("MED");
for i in range(0,7): class_labels.append("MGL");
for i in range(0,7): class_labels.append("RHB");
for i in range(0,10): class_labels.append("EPD");
for i in range(0,6): class_labels.append("JPA");

#Average computed as: Sum_val/N
def average(Sum_val,N):
    Sum_val = float(Sum_val); N = float(N);
    return Sum_val/N;

#Standard Deviation computed as: sqrt((N*Sum_sq - Sum_val*Sum_val)/(N*(N-1)))
def standard_deviation(N,Sum_val,Sum_sq):
    N = float(N); Sum_val = float(Sum_val); Sum_sq = float(Sum_sq);
    return math.sqrt((N*Sum_sq - Sum_val*Sum_val)/(N*(N-1)));        

#T_value computed as: (Avg1 - Avg2) / sqrt(Stdev1 * Stdev1/N1 + Stdev2*Stdev2/N2)
#Absolute value is applied to the computed T_value for the final result
def T_value(Avg1,Avg2,Stdev1,Stdev2,N1,N2):
    Avg1 = float(Avg1); Avg2 = float(Avg2); Stdev1 = float(Stdev1); Stdev2 = float(Stdev2); N1 = float(N1); N2 = float(N2);
    return abs((Avg1 - Avg2) / math.sqrt(Stdev1 * Stdev1/N1 + Stdev2 * Stdev2/N2));

def compute_T_values(input_filename, output_filename, target_class):
    input_file = open(input_filename, "r");
    output_file = open(output_filename, "w");
    #Write the header to the output file
    output_file.write("Gene,T-Value for Class " + target_class + "\n");
    #Skip the SNO line
    input_file.readline();
    line = input_file.readline();
    #Compute the T values for each line for the given target_class
    while line:
        line = string.split(line,',');
        gene_name = line[0];
        Sum_val_1 = 0.0;
        Sum_sq_1 = 0.0;
        Sum_val_2 = 0.0;
        Sum_sq_2 = 0.0;
        N1 = 0.0;
        N2 = 0.0;
        #Go through the sample values. Starts from 1 to ignore the gene_name.
        for i in range(1,70):
            #If the current sample is of the target class, increment Sum_val_1, Sum_sq_1, and N1.
            if class_labels[i - 1] == target_class:
                Sum_val_1 += float(line[i]);
                Sum_sq_1 += float(line[i]) * float(line[i]);
                N1 += 1.0;
            #Otherwise increment Sum_val_2, Sum_sq_2, and N2 for the other remaining classes.
            else:
                Sum_val_2 += float(line[i]);
                Sum_sq_2 += float(line[i]) * float(line[i]);
                N2 += 1.0;
        #Compute the statistics
        Avg1 = average(Sum_val_1,N1);
        Avg2 = average(Sum_val_2,N2);
        Stdev1 = standard_deviation(N1,Sum_val_1,Sum_sq_1);
        Stdev2 = standard_deviation(N2,Sum_val_2,Sum_sq_2);
        T_value_target = T_value(Avg1,Avg2,Stdev1,Stdev2,N1,N2);
        #Write the gene name and the T value to the output file
        output_file.write(gene_name + "," + str(T_value_target) + "\n");
        line = input_file.readline();
    input_file.close();
    output_file.close();

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "ERROR: You must provide an input filename as a command line arg. e.g. python compute_T_values.py pp5i_train_removed.gr.csv"
        sys.exit(0);
    compute_T_values(sys.argv[1],"T_values_MED.txt","MED");
    compute_T_values(sys.argv[1],"T_values_MGL.txt","MGL");
    compute_T_values(sys.argv[1],"T_values_RHB.txt","RHB");
    compute_T_values(sys.argv[1],"T_values_EPD.txt","EPD");
    compute_T_values(sys.argv[1],"T_values_JPA.txt","JPA");
