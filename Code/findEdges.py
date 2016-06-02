import cv2
import numpy as np
import sys
#from matplotlib import pyplot as plt

# NOTE: MUST TAKE A PPM
#       convert with: convert image.jpg -compress none image.ppm
filename = sys.argv[1]
img = cv2.imread(filename,0)
edges = cv2.Canny(img,100,200)

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()

cv2.imwrite(filename[:-4] + 'Edges.jpg', edges)
# NOTE: convert that to ppm after