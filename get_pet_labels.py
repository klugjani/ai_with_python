#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Janis Leonard Klug
# DATE CREATED: 07.05.2022                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Creating list of files in directory
    in_files = listdir(image_dir)
    
    # Processing each file to create a pet label dictionary with the key being 
    # the filenamevand the value being the image label
    results_dic = dict()
    
    # Processing through each file in the director and extracting only the 
    # words of the file containing the pet image label
    for idx in range(0, len(in_files), 1):
        
        # File that starts with "." being skipped, since these are no pet 
        # image files
        if in_files[idx][0] != ".":
            
            # Splitting lower case strings into words separated by 
            # whitespaces
            pet_image = in_files[idx].lower().split("_")
            
            # Creating a temporary label variable for the extracted pet 
            # label name
            pet_label = ""
            
            # For loop, checking if the word in pet_image consists of 
            # alphabetic character and adding blank space at the end.
            for word in pet_image:
                if word.isalpha():
                    pet_label += word + " "
            
            # Striping whitespace characters
            pet_label = pet_label.strip()
            
            
            # Adding filename and pet label to the dictionary. Printing 
            # an error message if already existant.
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
                
            else:
                print("Error: Duplicate file existant in directory.", 
                      in_files[idx])
           
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
