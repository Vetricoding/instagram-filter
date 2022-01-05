#project to see a picture blurred
import cv2

import matplotlib.pyplot as plt
pic = cv2.imread("house.jpeg")
blurpic = cv2.GaussianBlur(pic,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(blurpic)
plt.show()
