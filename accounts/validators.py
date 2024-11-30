from django.core.exceptions import ValidationError
import os


def allow_only_images_validators(value):
    ext = os.path.splitext(value.name)[1] # ? cover-image.jpg, in this [0] position will be cover-image and [1] position will be .jpg 
    print(ext)
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension, Please upload only' +str(valid_extensions))
    