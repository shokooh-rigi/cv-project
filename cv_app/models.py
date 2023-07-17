from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from cv_app import enums
from cv_app.utils import UploadToDateDir
from cv_app.validators import validate_only_numbers, validate_telephone_number, validate_mobile


class User(AbstractUser):
    pass


class AbstractBaseData(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('نام'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class University(AbstractBaseData):
    university_id = models.PositiveIntegerField(verbose_name=_('کد دانشگاه'))
    name = models.CharField(max_length=100, verbose_name=_('نام'))

    class Meta:
        verbose_name = _('دانشگاه')
        verbose_name_plural = _('دانشگاه ها')

    def __str__(self):
        return self.name


class Biography(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('نام'),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('نام خانوادگی'),

    )
    age = models.IntegerField(
        default=0,
        verbose_name=_('سن'),
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=UploadToDateDir('biography/picture'),
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'gif'])],
        verbose_name=_('تصویر‌شخص')
    )
    gender = models.CharField(
        choices=enums.Gender.choices,
        verbose_name=_('جنسیت'),
        default=enums.Gender.MALE,
        max_length=10,
        null=True,
        blank=True,
    )
    marital_status = models.CharField(
        choices=enums.MaritalStatus.choices,
        max_length=10,
        verbose_name=_('وضعیت تاهل'),
        default='',
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_('پست الکترونیکی'),
        null=True,
        blank=True,
    )
    telephone = models.CharField(
        max_length=11,
        verbose_name=_('تلفن ثابت'),
        null=True,
        blank=True,
        validators=[
            validate_only_numbers,
            validate_telephone_number,
        ]
    )

    phone_number = models.CharField(
        max_length=11,
        verbose_name=_('تلفن همراه'),
        null=True,
        blank=True,
        validators=[
            validate_mobile
        ]
    )
    address = models.TextField(
        max_length=2000,
        verbose_name=_('آدرس'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('بیوگرافی')
        verbose_name_plural = _('بیوگرافی ها')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class EducationHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    institution = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_('آموزشگاه'),
    )
    major = models.CharField(
        verbose_name=_('رشته تحصیلی'),
        max_length=100,
    )
    education_orientation = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('گرایش'),
    )
    university = models.ForeignKey(
        'cv_app.University',
        on_delete=models.PROTECT,
        verbose_name=_('دانشگاه محل تحصیل')
    )
    education_place = models.CharField(
        verbose_name=_('محل تحصیل'),
        max_length=50,
    )
    start_date = models.DateField(
        null=True,
        verbose_name=_('از تاریخ'),
    )
    end_date = models.DateField(
        null=True,
        verbose_name=_('تا تاریخ'),
    )
    study_level = models.CharField(
        max_length=50,
        choices=enums.StudyLevel.choices,
        verbose_name=_('مقطع تحصیلی'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('توضیحات'),
    )

    class Meta:
        verbose_name = _('سابقه تحصیلی')
        verbose_name_plural = _('سوابق تحصیلاتی')
        ordering = (
            'pk',
        )

    def __str__(self):
        return f'{self.major}'

    @property
    def name(self):
        return str(self)


class Certificate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('مدرک حرفه ای'),
    )
    description = models.TextField(
        null=True,
        blank=True, 
        verbose_name=_('توضیحات'),
    )
    received_date = models.DateField(
        verbose_name=_('تاریخ اخذمدرک'),
        null=True,
        blank=True,
    )
    expire_date = models.DateField(
        verbose_name=_('تاریخ پایان اعتبار'),
        null=True,
        blank=True,
    )
    course_duration = models.CharField(
        max_length=50,
        verbose_name=_('مدت دوره'),
    )

    class Meta:
        verbose_name = _('مدرک حرفه‌ای')
        verbose_name_plural = _('مدارک حرفه‌ای')

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('نام مهارت'),
    )
    level = models.CharField(
        choices=enums.SkillLevel.choices,
        verbose_name=_('سطح'),
    )

    class Meta:
        verbose_name = _('مهارت')
        verbose_name_plural = _('مهارت ها')

    def __str__(self):
        return f'{self.name}'


class JobExperience(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    currently_status = models.BooleanField(
        null=True,
        blank=True,
        default=False,
        verbose_name=_('شاغل تاکنون'),
    )
    job_title = models.CharField(
        max_length=50,
        verbose_name=_('سمت'),
    )

    start_date = models.DateField(
        null=True,
        verbose_name=_('از تاریخ'),
    )
    end_date = models.DateField(
        null=True,
        verbose_name=_('تا تاریخ'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('توضیحات'),
    )

    class Meta:
        verbose_name = _('سابقه شغلی')
        verbose_name_plural = _('سوابق شغلی')

    def __str__(self):
        return f'{self.job_title}'
