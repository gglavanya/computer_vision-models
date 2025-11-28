import cv2

img = cv2.imread("data/avtar.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (21, 21), 0)

# Invert and blend
invert = 255 - gray
invert_blur = 255 - blur
sketch = cv2.divide(gray, blur, scale=256)

cv2.imshow("Original", img)
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
