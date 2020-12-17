
############################### P.E. 09 ##########################################################

# 2) Follow the “eyes_cropped.py” in the HOP09 Manipulating Images and GUI Automation. 
# In the similar way use the image which was used in the previous question and create a 
# program which displays image in the similar pattern of  “eyes_cropped.png” and “four_eyes_bulldog.png”.

###############################################################################################

  
from PIL import Image # Import Pillow for images

img = Image.open('python.jpg')
cropped = img.crop((185, 108, 360, 192)) # this is the portion of the image I want to crop out
cropped.save('cropped_python.png') # save the image as a PNG

""" Now copy the image and paste it on the original image """
copy_img = img.copy()
copy_img.paste(cropped, (185, 25)) # This is the position where I want to paste the image
copy_img.save('triple_python.png') # saving the image as ...