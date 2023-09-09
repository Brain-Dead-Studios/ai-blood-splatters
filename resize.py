import PIL
from PIL import Image

dest_size = (512, 512)

# https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    print("new size: " + str(new_width) + "x" + str(new_height))
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

for i in range(1, 9):
    fname = "source/bloodsplatter" + str(i) + ".png"
    img = PIL.Image.open(fname)
    aspect_ratio = min(dest_size[0] / img.size[0], dest_size[1] / img.size[1])
    new_size = (int(img.size[0] * aspect_ratio), int(img.size[1] * aspect_ratio))
    img = img.resize(new_size)

    # Add margin
    left = (dest_size[0] - new_size[0]) // 2
    top = (dest_size[1] - new_size[1]) // 2
    img = add_margin(img, top, left, top, left, (0, 0, 0, 0))

    print(img.size)
    # Save
    img.save("512/bloodsplatter" + str(i) + ".png")
