

import cv2
import numpy as np

# read image
img = cv2.imread('C:\\Users\\LENOVO\\Desktop\\300DPI\\Template5_300dpi\\19.jpg')
ht, wd, cc= img.shape

# create new image of desired size and color (blue) for padding, the white space around the image
ww = 300
hh = 300


color = (255,255,255)
result = np.full((hh,ww,cc), color, dtype=np.uint8)

# compute center offset
xx = (ww - wd) // 2
yy = (hh - ht) // 2

# copy img image into center of result image
result[yy:yy+ht, xx:xx+wd] = img

# view result
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite("C:\\Users\\LENOVO\\Desktop\\after_addind_white_space_19.jpg", result)

mm
 