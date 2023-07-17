import logging

from django.utils import timezone
from django.utils.deconstruct import deconstructible

logger = logging.getLogger(__name__)


@deconstructible
class UploadToDateDir:
    def __init__(self, dir_name: str):
        self.dir_name = dir_name

    def __call__(self, instance, filename) -> str:
        return f'{self.dir_name}/{timezone.now()}/{filename}'
