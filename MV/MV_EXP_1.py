'''Handling Files, Cameras, and GUIs Basic I/O scripts ,Reading/writing an image file ,Converting between an image and raw bytes ,Accessing image data with numpy.array ,Reading/writing a video file ,Capturing camera frames, Displaying images in a window, Displaying camera frames in a window'''

import cv2
import numpy as np

# #Reading Image File
image = cv2.imread('image.jpg')
if image is not None:
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Cannot display image')

# #Writing Image File
output_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('output.jpg',output_image)

# Image to Raw_bytes
image_bytes = image.tobytes()
print(image_bytes) # do not print as it is very large

#Accessing image data with numpy.array
image_array = np.array(image)
height,weight,channel= image_array.shape
print(image_array.shape)

#Video Read- half baked
# video = cv2.VideoCapture('video.webm')
# while True:
#     ret,frame = video.read()
#     if not ret:
#         break
#     cv2.imshow('Frame',frame)
#     if cv2.waitKey(1) == ord("q"):
#         break
#     video.release()
#     cv2.destroyAllWindows()