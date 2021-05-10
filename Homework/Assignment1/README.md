Assignment 1 - Basic image processing

Write a Python script which does the following:

- For each image, find the width, height, and number of channels
- For each image, split image into four equal-sized quadrants (i.e. top-left, top-right, bottom-left, bottom-right)
- Save each of the split images in JPG format
- Create and save a file containing the filename, width, height for all of the new images.


Methods:

For this assignment a dataset consisting of images of 10 footballplayers have been used. Using indexing I have been able to get the height and width of the images, in addition to splitting them into four equal sized quadrants. This is later appended to empty lists I created before, and saved as a dataframe with the new filenames.   

Cloning repo and installing dependencies      


To run scripts within this repository, I recommend cloning the repository and installing relevant dependencies in a virtual ennvironment:     


$ git clone https://github.com/aksroa/Visual-portfolio.git

$ cd cds-visual

$ bash ./create_vision_venv.sh                                                                                                                  

If some of the libraries is not installed properly you can install these manually by running the following in the terminal:                   


$ cd cds-visual

$ source cv101/bin/activate

$ pip install {module_name}

$ deactivate


Discussion of results:

As of now most of the assignment is completed succesfully. However I was not able to find the number of channels in the images.