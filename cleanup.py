from PIL import Image, ImageDraw
import os
import numpy as np

def fix_colors(img):
    res = img.convert("RGBA")
    pixels = res.load()
    for i in range(res.size[0]):
        for j in range(res.size[1]):
            pixel = pixels[i, j]
            if pixel[0] + pixel[1] + pixel[2] < 100:
                pixels[i, j] = (0, 0, 0, 0)
            else:
                pixels[i, j] = (162, 23, 1, 255)
    return res

def get_direction(img):
    pixels = img.load()
    direction = np.array([0, 0])
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixels[i, j] != (0, 0, 0, 0):
                vec_from_center = np.array([i - img.size[0] // 2, j - img.size[1] // 2])
                direction += vec_from_center
    return direction / np.linalg.norm(direction)

def crop_img(img):
    pixels = img.load()
    min_x = img.size[0]
    max_x = 0
    min_y = img.size[1]
    max_y = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixels[i, j] != (0, 0, 0, 0):
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)
    return img.crop((min_x, min_y, max_x, max_y))

def draw_line(img, direction):
    draw = ImageDraw.Draw(img)
    draw.line((img.size[0] // 2, img.size[1] // 2, img.size[0] // 2 + direction[0] * 100, img.size[1] // 2 + direction[1] * 100), fill=(255, 0, 0, 255), width=5)
    return img

def rotate_img(img, direction):
    # rotates img so that direction points dead left
    angle = np.arctan2(direction[1], direction[0])
    print(angle)
    return img.rotate(angle / np.pi * 180 + 180, expand=True)

if __name__ == "__main__":
    # get all files in generated/
    for filename in os.listdir("generated"):
        # open image
        img = Image.open("generated/" + filename)
        # fix colors
        img = fix_colors(img)
        # get direction
        direction = get_direction(img)
        # draw line
        # img = draw_line(img, direction)
        img = rotate_img(img, direction)
        img = crop_img(img)
        img = img.resize((512, 512))
        # save image
        img.save("cleanedup/" + filename)