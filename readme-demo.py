import cv2
import numpy as np

frame = cv2.imread("readme-images/frame.png")

# crop to the letter A
A_normal = frame[5:200, 5:200]
cv2.imwrite("readme-images/A-normal.png", A_normal)

# convert to grayscale
gray = cv2.cvtColor(A_normal, cv2.COLOR_BGR2GRAY)
cv2.imwrite("readme-images/A-gray.png", gray)

# binarize
_, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("readme-images/A-bw.png", bw)

# invert
inv = 255 - bw
cv2.imwrite("readme-images/A-inverted.png", inv)

# open using a 5 x 5 kernel
kernel = np.ones((5, 5), np.uint8)
open = cv2.morphologyEx(inv, cv2.MORPH_OPEN, kernel)
cv2.imwrite("readme-images/A-open.png", open)

# crop to bounding box
contours, _ = cv2.findContours(open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(cnt)
bbox = open[y:y+h, x:x+w]
cv2.imwrite("readme-images/A-bbox.png", bbox)

# pad
size = max(w, h)
padded = np.zeros((size, size), dtype=np.uint8)
x_off = (size - w) // 2
y_off = (size - h) // 2
padded[y_off:y_off+h, x_off:x_off+w] = bbox
cv2.imwrite("readme-images/A-padded.png", padded)

resized = cv2.resize(padded, (64, 64), interpolation=cv2.INTER_AREA)
cv2.imwrite("readme-images/A-resized.png", resized)

_, final = cv2.threshold(resized, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite("readme-images/A-final.png", final)
