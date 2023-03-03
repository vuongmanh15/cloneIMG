import cv2
import numpy as np
import os

# Path to the original images folder
OriginalIMG = 'C:/Users/vuong/OneDrive/Desktop/stock'

# Path to the new images folder
CroppedIMG = 'C:/Users/vuong/OneDrive/Desktop/crop'

# Create the new folder if it doesn't exist
if not os.path.exists(CroppedIMG):
    os.makedirs(CroppedIMG)

# Define the ROI
row = 146
col = 124
height = 262
width = 368

# Loop through each image in the original folder
for img in os.listdir(OriginalIMG):
    # Load the image
    img_path = os.path.join(OriginalIMG, img)
    img = cv2.imread(img_path)

    # Extract the ROI
    roi = img[row:row+height, col:col+width]

    # Create a mask
    mask = np.zeros_like(roi)
    mask[100:300, 225:425] = 1

    # Clone the ROI
    new_size=(200,200)
    cloned_img = cv2.resize(roi,new_size)

    # Save the cloned image to the new folder
    new_img = os.path.splitext(os.path.basename(img_path))[0] + '_cloned.jpg'
    new_file_path = os.path.join(CroppedIMG, new_img)
    cv2.imwrite(new_file_path, cloned_img)

    # Display the result (optional)
    cv2.waitKey(0)

cv2.destroyAllWindows()
