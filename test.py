# test.py
# convert jpg to polar image in a image buffer and then convert buffer to an output jpg

from PIL import Image
import io

# read input image file into a PIL image
with open('ei.jpg', 'rb') as file:
    input_image_buffer = io.BytesIO(file.read())

input_image = Image.open(input_image_buffer)

width, height = input_image.size

# create an empty output image with a black background
output_image = Image.new('RGB', (width, height), 'black')

# fill the pixels in the output, one by one, with the corresponding pixels from the input
for x in range(width):
    for y in range(height):
        output_image.putpixel((x, y), input_image.getpixel((x, y)))

output_image.save('output.jpg')

# remember to close the file uwu
input_image_buffer.close()
