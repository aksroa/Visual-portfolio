Assignment 3 - Edge detection

Download and save the image at the link below: https://upload.wikimedia.org/wikipedia/commons/f/f4/%22We_Hold_These_Truths%22_at_Jefferson_Memorial_IMG_4729.JPG

Using the skills you have learned up to now, do the following tasks:

- Draw a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image. Save this as image_with_ROI.jpg.
- Crop the original image to create a new image containing only the ROI in the rectangle. Save this as image_cropped.jpg.
- Using this cropped image, use Canny edge detection to 'find' every letter in the image
- Draw a green contour around each letter in the cropped image. Save this as image_letters.jpg

Methods:
In this assignment I started by drawing the green rectangle using cv2.rectangle function, which takes the parameters image, start point, end point, colour and thickness. As instructed, this was saved as Image_with_ROI.jpg. Afterwards, the image was cropped so that the image only contained the text. The measures was found by a trial and fail method. This image was saved as Image_cropped.jpg. Furthermore the image was blurred and flattened using the cv2 functions before cannyedge detection was used. Finally cv2.findcontours was used to find all the letters and draw a green contour around them. This image was then saved as Image_letters.jpg

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
In relation to the results, the purpose of this assignment has been reached. However, when I used cv2.findcountours it seems that the function has found more contours than letters, and that it is a little bit to exact. This is something that could be improved to next time.