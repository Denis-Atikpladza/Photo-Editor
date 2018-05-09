#Denis Atikpladza
#100938122
#Photo editor calls filters upon user requests

import sys  # get_image calls exit
from Cimpl import *
from filters import *

img1 = None 

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

def options():
    """
    Prints messages of options to the user 
    """    
    print('Enter a command from the following options:')
    print('Type L: to Load image')
    print('Type N: for Negative  G: for Grayscale  X: for extreme contrast' +
          '  S: for Sepia tint  E: for Edge detect')
    print('Type Q: to quit')

def check(image):
    """
    Prints messages of options to the user 
    """     
    if image == None:
        print('ERROR: You have not loaded an image ')
        return True
    else: 
        return False

def __sepia_tint(image):
    """
    Checks if an image is loaded, calls sepia tint 
    and displays the image
    """     
    if check(image) == False:
        sepia_tint(image)
        show(image)

def __edge_detect(image, threshold):
    """
    Checks if an image is loaded, calls edge detect 
    and displays the image
    """     
    if check(image) == False:
        detect_edges_better(image, threshold)
        show(image)

def __grayscale(image):
    """
    Checks if an image is loaded, calls grayscale 
    and displays the image
    """     
    if check(image) == False:
        grayscale(image)
        show(image)
    
def __extreme_contrast(image):
    """
    Checks if an image is loaded, calls extreme contrast 
    and displays the image
    """     
    if check(image) == False:
        extreme_contrast(image)
        show(image)

def __negative(image):
    """
    Checks if an image is loaded, calls negative 
    and displays the image
    """     
    if check(image) == False:
        negative(image)
        show(image)
    

def main():
    """
    main program that determins which filter will be used based on user input
    
    Based on character given calls the appropriate filter.
    """      

    while True:
        options()
        var = input()
        if var == 'Q':
            break
        elif var == 'L':
            global img1
            img1 = get_image()
        elif var == 'N':
            __negative(img1)
        elif var == 'G':
            __grayscale(img1)
        elif var == 'X':
            __extreme_contrast(img1)
        elif var == 'S':
            __sepia_tint(img1) 
        elif var == 'E':
            thresh = int (input('Please select a threshold  '))
            __edge_detect(img1, thresh)
            
        else:
            print('ERROR: No such command  ')
        
            
            
        
    print('you have quit the program, Good-Bye')        



if __name__ == "__main__":
    main()