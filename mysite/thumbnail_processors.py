from easy_thumbnails.processors import scale_and_crop

def face_scale_and_crop(image, size, **kwargs):
    # convert image to black and white
    image = image.convert('L')
    kwargs['crop'] = ","
    kwargs['target'] = "50,50"
    return scale_and_crop(image, size, **kwargs)