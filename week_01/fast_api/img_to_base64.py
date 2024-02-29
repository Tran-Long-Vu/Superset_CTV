# code to take image, turn to base64, save into txt, and upload to server.
# coding convention: functions, imports.
# demo examples. 
# start real project asap.

import base64
from PIL import Image
from io import BytesIO

image_path = "./cat.jpg"
new_image_path = "./decoded_cat.jpg"

# Open the image file as BytesIO
with open('cat.jpg', 'rb') as file:
    image_buffer = BytesIO(file.read()) # bytes

# Encode the image data to Base64
base64_data = base64.b64encode(image_buffer.getvalue()) # b64 string

# Convert the Base64 data to a string
base64_str = base64_data.decode('utf-8') # utf 8 string

# Convert the Base64 string back to bytes
image_data = base64.b64decode(base64_str) #b64 string

# Create a BytesIO object to work with the image data
new_image_buffer = BytesIO(image_data) # bytes

new_image = Image.open(new_image_buffer)

new_image.save(new_image_path)

# Close the images
image_buffer.close()
new_image_buffer.close()
# upload to server.



