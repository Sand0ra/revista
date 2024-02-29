import re
from django.core.exceptions import ValidationError


def validate_tg_nickname(value):
    try:
        if value.startswith('@'):
            _validate_telegram_username(value)
        elif value.startswith('+'):
            _validate_phone_number(value)
        else:
            raise ValidationError('Contact must be either a valid Telegram username or a valid phone number.')
    except ValidationError as error:
        raise ValidationError(error.message)


def _validate_telegram_username(value):
    if not value.startswith('@'):
        raise ValidationError('Telegram username must start with @.')
    elif len(value) < 6:
        raise ValidationError('Telegram username must be at least 5 characters long.')


def _validate_phone_number(value):
    pattern = r'^\+\d{1,3}\d{7,12}$'
    if not re.match(pattern, value):
        raise ValidationError('Phone number must be in a valid international format.')
