Self-designed project

For the self-designes assignment the purpose is to take an image with text as input and do some optical character recognition and get the text on the image as output. The script is created so that it can run from the command line.

Methods:
For the assignment I started by loading the image usisng cv2.imread. I then drew a blue rectangle of the region of interest which is the area with text. The image was then cropped by defining the centers of the image, and trying and failing. The image was the converted to grayscale for easier character recognition and then to binary colours. In addition this was inverted so that we get a white background with black text on it. Furthermore, some noisereduction was completed. Finally whitespaces was removed before pytesseract.image_to_string was used to extract all the text in the image. The text was the printed.

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
The basics of the assignment have been finished succesfully with some small errors. For example it can be seen that the final text consists of a few extra characters and additional blanc spaces, which should have been removed. Furthermore I was not able to create a script which takes into account that different pictures need to be cropped differently in regards to the size of the image and where in the image, the text is located.