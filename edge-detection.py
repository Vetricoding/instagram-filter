#project to see edges of a picture 
import cv2
import matplotlib.pyplot as plt
pic = cv2.imread("flower.jpeg")
edgepic = cv2.Canny(pic,100,300)
plt.imshow(edgepic)
plt.show()
