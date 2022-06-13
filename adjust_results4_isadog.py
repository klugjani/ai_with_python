#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Janis Leonard Klug
# DATE CREATED: 08.05.2022                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    
    # Creating a dognames dictionary for matching with result_dic labels
    # from real answer & classifier's answer.
    dognames_dic = dict()
    
    # Reading in dognames from file; one name / line and automatically closing file.
    with open(dogfile, "r") as infile:
        # Reading in dognames from the first line
        line = infile.readline()
        
        # While loop, each line of the file is processed until the end of 
        # the file (EOF); dognames are added to dognames_dic. 
        while line != "":
            
            # Stripping newline from line
            line = line.strip()
            
            # Adding line (dogname) to the dictionary (dognames_dic) if not
            # yet existant in the dictionary.
            if line not in dognames_dic:
                dognames_dic[line] = 1
            else:
                print("Warning, duplicate dognames", line)
                
            # Reading in next line in file (if this is not empty). 
            line = infile.readline()
            
     
    # For loop iterating through results_dic: 
    # If label is found in dognames_dic, then the label "is a dog" (index 3/4 = 1).
    # Otherwise (index3/4 = 0), the  label "is not a dog".
    for key in results_dic:
        
        # Pet image label is a dog:
        if results_dic[key][0] in dognames_dic:
            
            # Appending (1,1), when both labels are dogs, that means the classifier 
            # label can be found e.g. in dognames_dic. 
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
            # Appending (1,0), when only the pet label is a dog and the classifier 
            # label is not a dog image (can e.g. not be found in dognames_dic).
            else:
                results_dic[key].extend((1,0))
        
        # Pet image is not a dog:
        else:
            
            # Appending(0,1), when only the classifier label is a dog image 
            # (found e.g. in dognames_dic).
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
            
            # Appending(0,0), when the classifier label is not a dog image 
            # (e.g. not found in dognames_dic), which means both labels are not dogs.
            else:
                results_dic[key].extend((0,0))
            
        
            
            
        
        
        
