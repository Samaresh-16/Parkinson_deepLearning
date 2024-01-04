import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

fig, axs = plt.subplots(2, 2, figsize=(15, 15))

# Display first row of images
# img1 = mpimg.imread('RFC_Error.png')
# axs[0, 0].imshow(img1)
# axs[0, 0].axis('off')

# img2 = mpimg.imread('DTC_Error.png')
# axs[0, 1].imshow(img2)
# axs[0, 1].axis('off')

# # Display second row of images
# img3 = mpimg.imread('GBC_Error.png')
# axs[1, 0].imshow(img3)
# axs[1, 0].axis('off')

# img4 = mpimg.imread('Knn_Error.png')
# axs[1, 1].imshow(img4)
# axs[1, 1].axis('off')

# # Display third row of images
# img5 = mpimg.imread('LR_Error.png')
# axs[2, 0].imshow(img5)
# axs[2, 0].axis('off')

# img6 = mpimg.imread('XGBC_Error.png')
# axs[2, 1].imshow(img6)
# axs[2, 1].axis('off')

# Display third row of images
img5 = mpimg.imread('ResNet Error.png')
axs[0, 0].imshow(img5)
axs[0, 0].axis('off')
axs[0,0].set_title('ResNet Error')

img6 = mpimg.imread('Ann Error.png')
axs[0, 1].imshow(img6)
axs[0, 1].axis('off')

# Display fourth row of images
img7 = mpimg.imread('MLP Error.png')
axs[1, 0].imshow(img7)
axs[1, 0].axis('off')

# Hide axis for last subplot
axs[1, 1].axis('off')

# Display the figure
plt.show()