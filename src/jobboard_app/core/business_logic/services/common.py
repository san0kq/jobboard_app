from __future__ import annotations

import uuid
from io import BytesIO
from sys import getsizeof

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


def rename_file_to_uuid(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
    file_extansion = file.content_type.split("/")[-1]
    file_name = str(uuid.uuid4()) + "." + file_extansion
    file.name = file_name

    return file


def change_file_size(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
    file_format = file.content_type.split("/")[-1].upper()
    output = BytesIO()
    with Image.open(file) as image:
        image.thumbnail(size=(1400, 1400))
        image.save(output, format=file_format, quality=100)

    return InMemoryUploadedFile(
        file=output,
        field_name=file.field_name,
        name=file.name,
        content_type=file.content_type,
        size=getsizeof(output),
        charset=file.charset,
    )
