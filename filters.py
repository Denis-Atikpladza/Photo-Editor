from Cimpl import *

#Denis Atikpladza
#Filters 


def negative(image):
    """ (Cimpl.Image) -> None
    Modify image, takes the existing rgb values and subtracts them
    from 255
    >>> image = load_image(choose_file())
    >>> negative(image)
    >>> show(image)
    """    
    for x, y, (r, g, b) in image:
        new_color = create_color(255 - r, 255 - g, 255 - b)
        set_color(image, x, y, new_color)

def solarize(image, threshold):
    """ (Cimpl.Image, int) -> None
    Solarize image, modifying the RGB components that
    have intensities that are less than threshold.
    Parameter threshold is in the range 0 to 256, inclusive.
    >>> image = load_image(choose_file())
    >>> solarize(image, 128)
    >>> show(image)
    """
    for x, y, (red, green, blue) in image:

        # Invert the values of all RGB components that are less than 128,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        solarized = create_color(red, green, blue)
        set_color(image, x, y, solarized) 
        
def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    Modify image, maximizing the contrast between the light
    and dark pixels.
    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(image)
    """
    for x, y, (red, green, blue) in image:      
        
        if red < 128:
            red = 0
        
        else:
            red = 255
        
        if green < 128:
            green = 0
            
        else: 
            green = 255
            
        if blue < 128:
            blue = 0
            
        else:
            blue = 255
            
        contrast = create_color(red, green, blue)
        set_color(image, x, y, contrast)  
        
def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def sepia_tint(image):
    """ (Cimpl.Image) -> None
    Convert image to sepia tones.
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """    
    grayscale(image)
    
    for x, y, (red, green, blue) in image:
        
        if red < 63:
            red = red * 0.9
            blue = blue * 1.1
        
        elif 63<= red <= 191:
            blue = blue * 0.85
            red = red * 1.15
            
        else:
            blue = blue * 0.93
            red = red * 1.08
            

def _adjust_component(amount):
    """ (int) -> int
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if amount <= 63:
        return 31
    
    elif 64 <= amount <= 127:
        return 95
    
    elif 128 <= amount <= 191:
        return 159
    
    else:
        return 223
    
def posterize(image):
    """ (Cimpl.Image) -> None
    "Posterize" the specified image.
    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """
    
    for  x, y, (r, g, b) in image:
        new_r = _adjust_component(r)
        new_g = _adjust_component(g)
        new_b = _adjust_component(b)
         
        new_col = create_color(new_r, new_g, new_b)
        set_color(image, x, y, new_col)  
        
        


def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> None
    Modify image using edge detection.
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 10.0)
    >>> show(image)
    """
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)- 1):
            topR, topG, topB = get_color(image, x, y)
            botR, botG, botB = get_color(image, x, y + 1)
            topC = (topR + topG + topB) / 3
            botC = (botR + botG + botB) / 3
            
            if abs(topC - botC) > threshold:
                black = create_color (0,0,0)
                set_color(image, x, y, black) 
            
            else:
                white = create_color(255,255,255)
                set_color(image, x, y, white) 
            
        
def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> None
    Modify the image using edge detection.
    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, 10.0)
    >>> show(image)
    """
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)- 1):
            topR, topG, topB = get_color(image, x, y)
            botR, botG, botB = get_color(image, x, y + 1)
            
            rightR, rightG, rightB = get_color(image,x + 1, y)
            
            topC = (topR + topG + topB) / 3
            botC = (botR + botG + botB) / 3
            
            rightC = (rightR + rightG + rightB) / 3
            
            if abs(topC - botC) > threshold or abs(topC - rightC) > threshold :
                black = create_color (0,0,0)
                set_color(image, x, y, black) 
            
            else:
                white = create_color(255,255,255)
                set_color(image, x, y, white)    
                
                
def blur_better(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @ (x, y) and its four neighbours
            #LC = left corner RC = right corner etc

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            
            #new#################################################################
            topLC_red, topLC_green, topLC_blue = get_color(source, x - 1, y - 1)#
            topRC_red, topRC_green, topRC_blue = get_color(source, x + 1, y - 1)#
            #new#################################################################
            
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            
            #new#################################################################
            botLC_red, botLC_green, botLC_blue = get_color(source, x - 1, y + 1)#
            botRC_red, botRC_green, botRC_blue = get_color(source, x + 1, y + 1)#
            #new#################################################################
            
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + topLC_red + topRC_red + 
                       botLC_red + botRC_red ) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                         right_green + center_green +topLC_green + topRC_green + 
                         botLC_green + botRC_green ) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                        right_blue + center_blue + topLC_blue + topRC_blue + 
                        botLC_blue + botRC_blue ) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)
    
    return target
