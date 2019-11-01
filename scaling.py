import cv2

img = cv2.imread('src.jpg')

res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imwrite("dest.jpg", res)
