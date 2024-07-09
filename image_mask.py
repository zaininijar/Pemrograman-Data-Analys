
import cv2
import numpy as np

image = cv2.imread('images/image.png')


def create_mask(image, rect):
    mask = np.zeros(image.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    cv2.grabCut(image, mask, rect, bgdModel,
                fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    return mask2


# Create a rectangle
rect = (50, 50, 400, 400)

# Create the mask
mask = create_mask(image, rect)

# Apply the mask to the image
masked_image = image * mask[:, :, np.newaxis]

# Show the masked image
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
