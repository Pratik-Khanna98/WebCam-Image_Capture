# Fetch picture from the file and display it.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.

# STEP 1: Import values
import argparse  # parse the path for the image
import cv2  # opencv library

# STEP 2: Fetching the argument and save in dictionary
ap = argparse.ArgumentParser()  # Parse the command line
ap.add_argument('-i', '--image', required=True, help='Enter the path to the image')  # pass image from command line labelled as argument '-image'
args = vars(ap.parse_args())  # parse the arguments and store them in a dictionary


# STEP 3: Loading and converting the image into numpy array
# Printing the corresponding values
image = cv2.imread(args['image'])  # load image off the desk using cv2.imread function
print('width: {} pixels'.format(image.shape[1]))  # since images are represented as NumPy arrays, we can use the shape attribute to examine the width, height and the number of channels
print('height: {} pixels'.format(image.shape[0]))
print('channels: {}'.format(image.shape[2]))

# STEP 4: Display the image and save the image in another format
cv2.imshow('image'.image)  # display actual image in screen, where 'image' is the window title.
cv2.waitKey(1000)  # wait.Key(0) means indefinite wait. wait key 1000 means wait for 1 sec etc
cv2.imwrite('cat.jpeg', image)  # write our image to file JPG format.





