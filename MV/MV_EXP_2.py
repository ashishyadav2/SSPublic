import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'image.jpg'
original_image = cv2.imread(image_path)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Gray Image
plt.subplot(1, 4, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Gray Image')
plt.axis('off')

# HSV Image
plt.subplot(1, 4, 3)
plt.imshow(hsv_image)
plt.title('HSV Image')
plt.axis('off')

# Lab Image
plt.subplot(1, 4, 4)
plt.imshow(lab_image)
plt.title('Lab Image')
plt.axis('off')

plt.tight_layout()
plt.suptitle("Different Color Spaces")
plt.show()
