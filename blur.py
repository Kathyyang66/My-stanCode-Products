"""
File: blur.py
Name: Kathy Yang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original smiley-face picture.
    :return: SimpleImage, blurred smiley-face picture.
    """
    new_image = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = new_image.get_pixel(x, y)
            total_red = 0
            total_blur = 0
            total_green = 0
            total_num = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = min(max(x + i, 0), img.width - 1)
                    pixel_y = min(max(y + j, 0), img.height - 1)
                    total_red += img.get_pixel(pixel_x, pixel_y).red
                    total_blur += img.get_pixel(pixel_x, pixel_y).blue
                    total_green += img.get_pixel(pixel_x, pixel_y).green
                    total_num += 1
            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blur / total_num
    return new_image


def main():
    """
    TODO: Taking every valued point and replacing with blurred one.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
