# test.py
# convert jpg to polar image in a image buffer and then convert buffer to an output jpg

"""

Iterate over pixels in the output image

  1. Convert Cartesian coordinates to polar
  2. Round polar coordinates to closest start of segment

"""

from PIL import Image
import io, math

# how many segments are in each circle
segments = 100

# todo: make into a terminal argument
input_image_path = 'ei.jpg'

# read input image file into a PIL image
with open(input_image_path, 'rb') as file:
  input_image_buffer = io.BytesIO(file.read())

input_image = Image.open(input_image_buffer)

width, height = input_image.size

# give the image a center in the event that the dimensions are even numbers
if width % 2 == 0:
  width = width - 1
if height % 2 == 0:
  height = height - 1

middle_x = math.ceil(width / 2)
middle_y = math.ceil(height / 2)

# create an empty output image with a black background
output_image = Image.new('RGB', (width, height), 'black')

# fill the pixels in the output, one by one, with the corresponding pixels from the input
for x in range(width):
  for y in range(height):

    # radius = math.sqrt(x*x + y*y)

    segment_angle = 2 * math.pi / segments

    horizontal = x - middle_x
    vertical = y - middle_y

    radius = math.sqrt(horizontal*horizontal + vertical*vertical)

    if horizontal != 0:
      output_angle = math.atan2(vertical, horizontal)
    else:
      if 0 <= vertical:
        output_angle = math.pi/2
      else:
        output_angle = -math.pi/2

    input_angle = segment_angle * math.ceil(output_angle / segment_angle)

    input_x = math.ceil(radius * math.cos(input_angle)) + middle_x
    input_y = math.ceil(radius * math.sin(input_angle)) + middle_y

    if input_x < 0:
      input_x = 0
    elif width <= input_x:
      input_x = width - 1
    if input_y < 0:
      input_y = 0
    elif height <= input_y:
      input_y = height - 1

    try:
      output_image.putpixel((x, y), input_image.getpixel((input_x, input_y)))
    except IndexError:
      print("x: " + str(input_x) + ", y: " + str(input_y))
      input_image_buffer.close()
      exit()

output_image.save('output.jpg')

# remember to close the file uwu
input_image_buffer.close()