from skimage import data,feature,filters,io,morphology
from scipy import ndimage
from matplotlib import pyplot as plt
import numpy as np
ax=((0,0,0),(0,0,0))

images=["samolot00.jpg","samolot14.jpg","samolot07.jpg","samolot08.jpg","samolot04.jpg","samolot17.jpg",
        ]

images=[io.imread(image,as_grey=True) for image in images]
images=[filters.rank.median(image,morphology.disk(5)) for image in images]
images=[filters.gaussian(image,4) for image in images]

images=[image+30*(image-filters.gaussian(image,1)) for image in images]

images=[filters.sobel(image) for image in images]

#images=[filters.rank.median(image,morphology.disk(5)) for image in images]

#images=[morphology.erosion(image,morphology.disk(5)) for image in images]
#images=[morphology.dilation(image,morphology.square(5)) for image in images]
##images=[morphology.erosion(image,morphology.square(3)) for image in images]


fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(16, 9))
index=0
for i in ax:
    for j in i:
       j.imshow(images[index],cmap=plt.cm.gray)
       j.axis("off")
       index+=1
plt.show()
