from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class UsernameValidator(RegexValidator):
    regex = r'^[\w.@+-]+$'
    flags = 0


def meusername(value):
    if value == "me":
        raise ValidationError(
            _('username %(value)s is not permited'),
            params={'value': value},
        )
