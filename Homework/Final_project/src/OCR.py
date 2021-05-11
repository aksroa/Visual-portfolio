#Importing libraries
import cv2
import pytesseract
import numpy as np
import os
import sys

sys.path.append(os.path.join(".."))

import argparse

def main(inpath):
    
    # Loading image using OpenCV
    img = cv2.imread(inpath)
    
    # Creating the blue rectangle box of the region of interest, which contains the text.
    # Measures are just found by trying and failing
    cv2.rectangle(img, (780,480), (10, 95), (255, 0, 0), 3) #cv2.rectangle( image, start_point, end_pont, color, thickness)
    
    # Defining the center of the image
    (centerX, centerY) = (img.shape[1]//2, img.shape[0]//2)
    
    # Cropping the image based on the centers
    cropped_image = img[centerY-700:centerY+550, centerX-395: centerX +380]
    
    # Preprocessing image
    
    # Converting to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    
    # Creating Binary image by selecting proper threshold
    binary_image = cv2.threshold(gray_image ,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Inverting the image, so we get a white backround and black text
    inverted_bin = cv2.bitwise_not(binary_image)
    
    # Reduce noise on the image
    kernel = np.ones((2,2),np.uint8)# dtype uninteger
    processed_img = cv2.erode(inverted_bin, kernel, iterations = 1) 
    processed_img = cv2.dilate(processed_img, kernel, iterations = 1)

    # Applying image_to_string method
    text = pytesseract.image_to_string(processed_img)
    
    # Printing the text
    print(text)
    
    # Removing whitespaces
    processed = text.replace("\n"," "),
    
    # Printing the processed text
    print(processed)
          
         

# Define behaviour when called from command line
if __name__=="__main__":
    
    # Initialise ArgumentParser class
    parser = argparse.ArgumentParser(description = "Takes an input image, croppes the roi, converts it to grayscale and binary colours and finally returns the imagetext as string")
    
    # Add inpath argument
    parser.add_argument(
        "-i",
        "--inpath", 
        type = str,
        default = os.path.join("..", "Data", "image2.jpg"),
        required = False, #Not required as we have a default parameter.
        help= "str - path to image file we use as default")
    
    # Taking all the arguments we added to the parser and input into "args"
    args = parser.parse_args()

    main(args.inpath)
    