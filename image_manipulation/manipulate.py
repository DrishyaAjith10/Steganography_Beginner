from PIL import Image

image_path = 'example.png'
image = Image.open(image_path)

width, height = image.size

print(width,height)

print(width * height)

new_image = Image.new('RGB',(width,height),(0,0,0))

for i in range(width):
    for j in range(height):
        pixel = image.getpixel((i,j))
        pixel = (pixel[0], pixel[1], 255)
        new_image.putpixel((i,j), pixel)

new_image = new_image.rotate(90)

new_image.show()

