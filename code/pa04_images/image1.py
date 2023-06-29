from matplotlib import pyplot
from matplotlib import image
import numpy as np

image = image.imread('coffee.jpg')

print(image.dtype)
print(image.shape)
print(image[100][100])

img = np.asarray(image)
print(img[100][100])

print(img.flags)

img2 = img.copy()

for i in range(len(img2)):
    for j in range(len(img2[0])):
        x = img2[i][j]
        m = (x[0]//2+x[1]//2)
        x[0]=m
        x[1]=m

imgplot = pyplot.imshow(img2)

# display the array of pixels as an image
#pyplot.imshow(image)
pyplot.show()
