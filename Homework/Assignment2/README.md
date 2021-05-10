Assignment 2 - Simple image search

Download the Oxford-17 flowers image data set, available at this link: https://www.robots.ox.ac.uk/~vgg/data/flowers/17/

Choose one image in your data that you want to be the 'target image'. Write a Python script or Notebook which does the following:

- Use the cv2.compareHist() function to compare the 3D color histogram for your target image to each of the other images in the corpus one-by-one.
- In particular, use chi-square distance method, like we used in class. Round this number to 2 decimal places.
- Save the results from this comparison as a single .csv file, showing the distance between your target image and each of the other images.The .csv file should show the filename for every image in your data except the target and the distance metric between that image and your target. Call your columns: filename, distance.
- Print the filename of the image which is 'closest' to your target image

Methods:

First of all a target image was selected while the path to the other images was defined. Using opencv, the channels of the images was split and 3D colour histograms was created of the target image, and the other images. Then, using the chi-squared distance method, the images was compared to each other and appended to an empty list called "distance", and into a df. By using the df.min function I found out what the lowest difference was and which file this was.

Cloning repo and installing dependencies

To run scripts within this repository, I recommend cloning the repository and installing relevant dependencies in a virtual ennvironment:

$ git clone https://github.com/aksroa/Visual-portfolio.git

$ cd cds-visual

$ bash ./create_vision_venv.sh


If some of the libraries is not installed properly you can install these manually by running the following in the terminal:

$ cd cds-visual

$ source ./cv101/bin/activate

$ pip install {module_name}

$ deactivate

Discussion of results:

The assignment have been completed succesfully and the image wich is closest to the target image has a distance of 347200.09 and is the file image_0090.jpg