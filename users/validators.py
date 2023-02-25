def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
from django.core.exceptions import ValidationError


def validate_file(value):
    value= str(value)
    if value.endswith(".pdf") != True and value.endswith(".doc") != True and value.endswith(".docx") != True: 
        raise ValidationError("Only PDF and Word Documents can be uploaded")
    else:
        return value
   