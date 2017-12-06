##########################################
CS488/508 Data Mining Final Project Files
##########################################

Progress:
    Finished Step 1
    Finished Step 2, final files are in the step2_result_files folder
    Finished Step 3, bestN.csv files can be generated using ./run.sh 15 in the step3 folder.
    Finished Step 4, predictions found in step4/predictions.csv. These predictions are for top12 on IBk where K = 4.

Notes:

    Each of the step folders has a run file that will automate the commands.
    Use these for each step, although keep in mind the requirements listed in the comments inside the scripts.

    The normalized train file generated via normalize.py from step 1,
    is used with the python code and scripts found in step2. 
    In this project's current form, the generated files from step 1 must be
    manually moved over to the step 2 folder (e.g. use mv). Additionally, the final csv files
    generated from step2 must be manually converted to arff using weka.
    This has already been done and the results have been placed into the 
    step2_result_files folder, however recreation of the files should keep these
    notes in mind.

    Based on the data calculated for step3.b, the best gene set is N=12 w/ model IBk where K = 4.
    No optimizations were made to the model (may want to work with this).

    Update: Absolute value has been removed from the calculation of the T value.
    This has changed the best gene set. Previously it was N = 15 w/ model IBk where K = 4.

    Update: Added naivebayes predictions in step4/naivebayes/predictions.csv
    The top25 genes were chosen as the gene set. 
    In comparison to the predictions made for IBk (k = 4) on top12,
    the following gene predictions differed (listed by prediction numbers 1-23): 1,10,17,21,23.

    Added j48 predictions in step4/j48/predictions.csv
    The top8 genes were chosen as the gene set.
    Surprisingly, setting reducedErrorPruning = True and binarySplits = False gave error rate 18.8406%, worse than original.
    Setting reducedErrorPruning = True, binarySplits = True gave error rate 18.8406%
    Setting reducedErrorPruning = False, binarySplits = True gave error rate 11.5942%, same as the original.
    Therefore, default settings were used for generating the predictions
    In comparison to the predictions made for IBk (k = 4) on top12,
    the following gene predictions differed (listed by prediction numbers 1-23): 5,17,23.
