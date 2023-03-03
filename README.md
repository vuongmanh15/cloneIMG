import cv2
import os

# Path to the original images folder
original_folder = 'path/to/original/folder'

# Path to the cropped images folder
cropped_folder = 'path/to/cropped/folder'

# Create the cropped images folder if it doesn't exist
if not os.path.exists(cropped_folder):
    os.makedirs(cropped_folder)

# Loop through each image in the original folder
for img_name in os.listdir(original_folder):
    # Load the image
    img_path = os.path.join(original_folder, img_name)
    img = cv2.imread(img_path)

    # Define the ROI
    x1, y1, x2, y2 = 100, 100, 500, 500  # Replace with your own ROI coordinates
    roi = img[y1:y2, x1:x2]

    # Calculate the aspect ratio of the ROI
    roi_width, roi_height = roi.shape[1], roi.shape[0]
    aspect_ratio = roi_width / roi_height

    # Define the new size for the cropped image based on the aspect ratio of the ROI
    new_width = 200
    new_height = int(new_width / aspect_ratio)

    # Resize the ROI while maintaining the aspect ratio
    cloned_img = cv2.resize(roi, (new_width, new_height))

    # Save the cloned image to the cropped folder
    cropped_img_name = os.path.splitext(img_name)[0] + '_cropped.png'
    cropped_img_path = os.path.join(cropped_folder, cropped_img_name)
    cv2.imwrite(cropped_img_path, cloned_img)

    # Display the result (optional)
    cv2.imshow('Cloned image', cloned_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
