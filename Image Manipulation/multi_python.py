############################### P.E. 09 ##########################################################

# 1) Follow the “multi_face.py” in the HOP09 Manipulating Images and GUI Automation. 
# In the similar way download any image of your choice and create a program which 
# displays image in the similar pattern of  “multi_face.png”  

#################################################################################################

from PIL import Image # Import Pillow for images

def multi_python(): # create a function

    """ Resize the image its self """
    img = Image.open('python.jpg')
    width, height = img.size
    resize = img.resize((int(width//10), int(height//10)))
    
    """Flip the image from top to bottom keeping the mirror image. 
    This will be determined to flip top to bottom or left to right 
    from the image on how you want it. For this image it really didn't matter."""
    flip = resize.transpose(Image.FLIP_TOP_BOTTOM) 
    flipw, fliph = flip.size

    pattern = Image.new('RGBA', (475, 510), 'green') # put image in the pattern and crop the size of the image to your liking.
    # image grid will be width 8 images and hieght 9 images 
    w, h = pattern.size
    for top in range(0, w, flipw): # create a nested loop to add the images in the size of the picture you cropped
        for bottom in range(0, h, fliph):
            pattern.paste(flip, (top, bottom))
    pattern.save('multi_python.png') # save image as

multi_python()  # call the function
