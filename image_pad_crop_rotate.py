from PIL import Image, ImageOps
import random


def add_border(input_image, output_image, border):
    ## add 25 pixels padding to image
    img = Image.open(input_image)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image)
    
    
def crop_image(path, cropped_path):
    ## choose random 200x200 pixels cropping and rotate image
    image = Image.open(path)
    randx = random.randint(0, 50)
    randy = random.randint(0, 50)
    rand_rotate = random.randint(-10, 10)
    cropped = image.crop((randx, randy, 200 + randx, 200 + randy)).rotate(rand_rotate)
    cropped.save(cropped_path)