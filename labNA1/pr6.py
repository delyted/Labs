from PIL import Image
import numpy as np

# Load the image
image_path = r'D:\Codes\python\labNA1\1_.jpg'
image = Image.open(image_path)
image_array = np.array(image)

# User input for rotation angle and scaling values
rotation_angle = int(input("Enter the rotation angle: "))
scaled_height = int(input("Enter the scaled height: "))
scaled_width = int(input("Enter the scaled width: "))

def rotate_image(angle, img):
    # Create a rotation matrix using the given angle
    theta = np.radians(angle)
    cos = np.cos(theta)
    sin = np.sin(theta)
    rotation_matrix = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])

    # Determine the dimensions of the rotated image
    height, width = img.shape[:2]
    new_width = int(np.round(height * np.abs(sin) + width * np.abs(cos)))
    new_height = int(np.round(width * np.abs(sin) + height * np.abs(cos)))

    # Define the center of rotation
    cx, cy = width / 2, height / 2
    dx, dy = new_width / 2, new_height / 2
    center_matrix = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]])
    center_matrix_inv = np.array([[1, 0, -dx], [0, 1, -dy], [0, 0, 1]])

    # Apply the rotation and centering matrices to the image
    affine_matrix = np.dot(np.dot(center_matrix, rotation_matrix), center_matrix_inv)
    rotated_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    for y in range(new_height):
        for x in range(new_width):
            src_x, src_y, _ = np.dot(affine_matrix, [x, y, 1]).astype(int)
            if 0 <= src_x < width and 0 <= src_y < height:
                rotated_img[y, x, :] = img[src_y, src_x, :]
    return rotated_img

def scale_image(img, new_height, new_width):
    original_height, original_width = img.shape[:2]
    scaled_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    for y in range(new_height):
        for x in range(new_width):
            src_x = int(original_width * x / new_width)
            src_y = int(original_height * y / new_height)
            scaled_img[y, x, :] = img[src_y, src_x, :]
    return scaled_img

# Rotate the image
rotated_image_array = rotate_image(rotation_angle, image_array)
rotated_image = Image.fromarray(rotated_image_array)
rotated_image.show()

# Scale the image
scaled_image_array = scale_image(image_array, scaled_height, scaled_width)
scaled_image = Image.fromarray(scaled_image_array)
scaled_image.show()