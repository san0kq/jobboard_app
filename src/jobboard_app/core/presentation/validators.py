from django.core.exceptions import ValidationError
from django.core.files import File


def phone_number_validator(number: str) -> None:
    if not number.replace("+", "").isdigit() or "+" in number[1::]:
        raise ValidationError(message="Invalid phone number. Example: +375336463322")


class TagsValidator:
    def __init__(self, max_number: int) -> None:
        self._max_number = max_number

    def __call__(self, value: str) -> None:
        tags = value.split("\r\n")
        if len(tags) > self._max_number:
            raise ValidationError(message=f"Max number of tags is {self._max_number}.")
        for tag in tags:
            if not tag:
                raise ValidationError(message="Tag cannot be an empty string.")
            if len(tag) > 30:
                raise ValidationError(message="Max length of tag is 30 symbols.")


class ValidateFileExtension:
    def __init__(self, available_extensions: list[str]) -> None:
        self._available_extensions = available_extensions

    def __call__(self, file: File) -> None:
        if "." not in file.name:
            raise ValidationError(message="File must have extension.")
        file_extension = file.name.split(".")[-1]
        if file_extension not in self._available_extensions:
            raise ValidationError(message=f"Accept only {self._available_extensions}")


class ValidateFileSize:
    def __init__(self, max_size: int) -> None:
        self._max_size = max_size

    def __call__(self, file: File) -> None:
        if file.size > self._max_size:
            max_size_in_mb = int(self._max_size / 1_000_000)
            raise ValidationError(message=f"Max file size is {max_size_in_mb} MB")
