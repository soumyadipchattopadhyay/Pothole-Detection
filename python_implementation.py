import cv2
import numpy as np
import matplotlib.pyplot as plt

#load the image
input_image = cv2.imread('highway2.jpg')

#resize the image for faster processing
img = cv2.resize(input_image, (400, 300))

#converting the image to gray
gray_image=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#detect edges
edges_image = cv2.Canny(gray_image,400,173)

#creating an arrays for ones to increase the area for dilation
se = np.ones((30, 30))

#dilating the images 
img_dilation = cv2.dilate(edges_image, se, iterations=1)

#getting the shape
row, col = img_dilation.shape

#creating an empty lsit
l=[]

#getting each pixel value
for i in range(row):
    for j in range(col):
        #if the current pixel is one, add to list
        if (img_dilation[i,j]==255):
            l.append(j)

#get the number of white pixels
count = len(l)

#if the number of white pixels are greater than some particular value, pothole is detected
if (count>16000):
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, "Pothole detected !", "Alert", 1)

#plot the images 
plt.subplot(121),plt.imshow(edges_image,cmap = 'gray')
plt.title('Edge'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_dilation,cmap = 'gray')
plt.title('Dilation'), plt.xticks([]), plt.yticks([])
plt.show()

print(count)
cv2.waitKey(0)
cv2.destroyAllWindows