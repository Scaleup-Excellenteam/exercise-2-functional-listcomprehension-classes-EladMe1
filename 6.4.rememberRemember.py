from PIL import Image


def decrypt_Image_Message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    decrypt_string = ""
    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            if pixels[i, j] == (0, 0, 0):  # check if the pixel is black
                decrypt_string += chr(j)
    return decrypt_string



