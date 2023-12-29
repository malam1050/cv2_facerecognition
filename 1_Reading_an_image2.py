
 # Importing the OpenCV library 
import cv2 
#Introduction to OpenCV
#https://www.geeksforgeeks.org/introduction-to-opencv/?ref=lbp

#Reading an image

   
# Reading the image using imread() function 
image = cv2.imread('/home/hirok/cv2_facerecognition/road.jpg') 

# Extracting the height and width of an image 
h, w = image.shape[:2] 
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w)) 
    
'''
Now we will focus on extracting the RGB values
So the 0th value will correspond to Blue pixel and not Red.
'''

#Extracting the RGB values of a pixel
# Extracting RGB values. 
 # Here we have randomly chosen a pixel 
# by passing in 100, 100 for height and width. 
(B, G, R) = image[100, 100] 

# Displaying the pixel values 
print("R = {}, G = {}, B = {}".format(R, G, B)) 

# We can also pass the channel to extract 
# the value for a specific channel 
B = image[100, 100, 0] 
print("B = {}".format(B)) 

#Extracting the Region of Interest (ROI)
# We will calculate the region of interest 
# by slicing the pixels of the image 
roi = image[100 : 500, 200 : 700] 
    
#display image
cv2.imshow('Extracting the RGB values of a pixel', roi)

'''
The problem with this approach is that the aspect ratio of the image is not maintained. 
So we need to do some extra work in order to maintain a proper aspect ratio.
'''
    
# Calculating the ratio 
ratio = 800 / w 

# Creating a tuple containing width and height 
dim = (800, int(h * ratio)) 

# Resizing the image 
resize_aspect = cv2.resize(image, dim) 

#Rotating the Image
    
# Calculating the center of the image 
center = (w // 2, h // 2) 

# Generating a rotation matrix 
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) 

# Performing the affine transformation 
rotated = cv2.warpAffine(image, matrix, (w, h)) 

#display image
cv2.imshow('Rotating the Image', rotated)
    
    
#Drawing a Rectangle
# We are copying the original image, 
# as it is an in-place operation. 
output = image.copy() 

# Using the rectangle() function to create a rectangle. 
rectangle = cv2.rectangle(output, (1500, 900), 
                            (600, 400), (255, 0, 0), 2) 

 #Displaying text
 #It is also an in-place operation
    
 # Copying the original image 
output = image.copy() 
    
 #display image
cv2.imshow('output', output)

# Adding the text using putText() function 
text = cv2.putText(output, 'OpenCV Demo', (500, 550), 
                    cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2) 

#display image
cv2.imshow('image', text)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    
