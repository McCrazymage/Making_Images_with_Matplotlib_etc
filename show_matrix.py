import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np
w = np.random.rand(50,50)
# first way
plt.imshow(w, cmap=plt.cm.gray)
plt.show()
#second way
image = Image.fromarray(np.uint8(w))
image.show()
image.save('a.png')
