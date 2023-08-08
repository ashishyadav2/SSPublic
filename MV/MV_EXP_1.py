import cv2
import numpy as np
import matplotlib.pyplot as plt
# # Reading Image File
image = cv2.imread('image.jpg')
if image is not None:
    image = cv2.resize(image, (720-int(50/100*720), 1280-int(50/100*1280)))
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Cannot display image')

# # Writing Image File
output_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('output.jpg',output_image)

# # Image to Raw_bytes
image_bytes = image.tobytes()
print(image_bytes) 

# # Subplot
og_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(og_image,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title("Image 1")
plt.imshow(og_image)
plt.axis('off')
plt.subplot(1,2,2)
plt.title("Image 2")
plt.imshow(gray_img,cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()

# # Accessing image data using numpy.array
image_array = np.array(image)
height,width,channel= image_array.shape
print(f"{image_array.shape}")
print(f"Height: {height}")
print(f"Width: {width}")
print(f"Channels: {channel}")

# # Reading Video file
cap = cv2.VideoCapture('video.webm')
if (cap.isOpened()== False):
	print("Error opening video file")
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow('Reading Video', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()

# # #Writing Video file
def write_video():
    cap = cv2.VideoCapture("video.webm")
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # for webm use XVID, for mp4 use MPEG
    output = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width,frame_height))
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        cv2.rectangle(frame,(50,50),(150,150),(0,0,255),3)
        output.write(frame)
    cv2.destroyAllWindows()
    output.release()
    cap.release()
if __name__ == "__main__":
	write_video()