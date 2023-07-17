from django.db import models
from django.utils.translation import gettext_lazy as _


class StudyLevel(models.TextChoices):
    ASSOCIATE = 'ASSOCIATE', _('کاردانی')
    BACHELOR = 'BACHELOR', _('کارشناسی')
    MASTER = 'MASTER', _('کارشناسی ارشد')
    PHD = 'PHD', _('دکتری')
    POSTDOC = 'POSTDOC', _('فوق دکتری')


class Gender(models.TextChoices):
    MALE = 'MALE', _('مرد')
    FEMALE = 'FEMALE', _('زن')


class MaritalStatus(models.TextChoices):
    SINGLE = 'SINGLE', _('مجرد')
    MARRIED = 'MARRIED', _('متاهل')


class SkillLevel(models.TextChoices):
    ELEMENTARY = 'ELEMENTARY', _('مقدماتی')
    INTERMEDIATE = 'INTERMEDIATE', _('متوسط')
    ADVANCE = 'ADVANCE', _('پیشرفته')
    PROFESSIONAL = 'PROFESSIONAL', _('حرفه ای')