# Import libraries
import os
import glob 
import sys 
import argparse 
import cv2
import pandas as pd
import numpy as np

# Define the main function
def main(targetpath, filepath):
    # Creating some empty lists, which we later will append, respectively: the filenames and the distance from the target image.
    filenames = []
    distance_to_target_image = []

    # Creating histogram of the target image
    target_image = cv2.imread(targetpath)
    target_hist = cv2.calcHist([target_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    target_hist = cv2.normalize(target_hist, target_hist, 0,255, cv2.NORM_MINMAX)
    
    # For every other file, we get the filename and calculate the distance to the target
    for file in glob.glob(filepath):
        # Get filename
        filename = os.path.split(file)[1]
        filenames.append(filename)

        # Read image, and calculate distance
        img = cv2.imread(file)
        hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist, 0,255, cv2.NORM_MINMAX)
        dist_to_target = round(cv2.compareHist(target_hist, hist, cv2.HISTCMP_CHISQR), 2)
        distance_to_target_image.append(dist_to_target)
        
    
        # Create a dataframe with the information on distances
        df = pd.DataFrame(list(zip(filenames, distance_to_target_image)), 
                    columns =['filename', 'dist_to_target'])

        # Create outpath for df
        target_image_filename = os.path.split(targetpath)[1][:-4] + f"- distances.csv"
        outfilepath = os.path.join("output", target_image_filename)

        # Save df
        df.to_csv(outfilepath, index = False)
        print(f"A new file has been created succesfully: \"{outfilepath}\"")
        # print the filename and distance of the image which is closest (min distance)
        
        print(df[df.distance == df.distance.min()]) # Doesnt work
    
    # Define behaviour when called from command line
if __name__=="__main__":
    
    # Initialise argparse
    parser = argparse.ArgumentParser(description = "Calculates distance from the target image to all the other images")
    
    # Add argument which identifies the path to the target image
    parser.add_argument(
        "-t",
        "--targetpath",
        required = False,
        type = str, 
        default = os.path.join("Data", "00001.jpg"),
        help = "string - path to the target image")
    
    # Add argument which identifies the path to all the other images
    parser.add_argument(
        "-f",
        "--filepath", 
        required = False,
        type = str,
        default = os.path.join("Data", "*.jpg"),
        help= "string - path to all the images")
    
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()
    
    main(args.targetpath, args.filepath)
    
    