import datetime
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_numbers(string):
    """
    Checks if the string was not a number raise ValidationError
    """
    string = str(string)
    string = re.sub(r'\s+', "", string)
    pattern = re.compile(r'[0-9]+')
    if not bool(pattern.match(string)):
        raise ValidationError('فقط اعداد قابل قبول هستند.')


def validate_telephone_number(telephone):
    if not re.match(r'^0\d{2,3}(-|)\d{5,8}$', telephone):
        raise ValidationError('شماره تلفن نادرست است.')


def validate_18_years_old(date):
    up_limit = datetime.date.today() - datetime.timedelta(days=18 * 365)
    if date > up_limit:
        raise ValidationError(_('سن شخص باید بالاتر از ۱۸ سال باشد.'))


def check_mobile(mobile):
    """
    Checks mobile string to ensure
    it starts with 09 and has correct length.
    Also removes any spaces before validation
    :param mobile:
    :return: bool
    """
    mobile = str(mobile)
    mobile = re.sub(r'\s+', "", mobile)
    if len(mobile) != 11:
        return False
    if not re.match(r'^09\d{9}$', mobile):
        return False
    return True


def validate_mobile(mobile):
    """
    Wraps check_mobile() method to use with
    form validations.
    :param mobile:
    :raises ValidationError
    :return:
    """
    if not check_mobile(mobile):
        raise ValidationError('شماره همراه نادرست است.')