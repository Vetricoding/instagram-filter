import cv2
import matplotlib.pyplot as plt
import numpy as np
pic = cv2.imread("fruit.jpeg")
rows,columns = pic.shape[:2]
kernel_x = cv2.getGaussianKernel(columns,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage_pic = np.copy(pic)
for i in range(3):
    vintage_pic[:,:,i] = vintage_pic[:,:,i] * filter

plt.imshow(vintage_pic)
plt.show()
