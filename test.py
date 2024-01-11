# test.py
# convert jpg to polar image in a image buffer and then convert buffer to an output jpg

from PIL import Image
import io

# read input image file into a PIL image
with open('ei.jpg', 'rb') as file:
    input_image_buffer = io.BytesIO(file.read())

input_image = Image.open(input_image_buffer)



# remember to close the file uwu
input_image_buffer.close()
