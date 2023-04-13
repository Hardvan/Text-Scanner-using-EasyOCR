import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

IMAGE_PATH = "./images/surf.jpg"

reader = easyocr.Reader(['en'])

# Read the image
result = reader.readtext(IMAGE_PATH)

# Display the result
print(result)

# ## 4. Drawing Ressult

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]

# Read the image
img = cv2.imread(IMAGE_PATH)

# Draw the bounding box
img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)

# Put the text
img = cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX,
                  1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the image
plt.imshow(img)
plt.show()


IMAGE_PATH = "./images/out-of-service.jpg"

# Create a reader
reader = easyocr.Reader(['en'])

# Read the image
result = reader.readtext(IMAGE_PATH)

# Display the result
print(result)

img = cv2.imread(IMAGE_PATH)
for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]

    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
    img = cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX,
                      2, (255, 255, 255), 2, cv2.LINE_AA)

plt.imshow(img)
plt.show()
