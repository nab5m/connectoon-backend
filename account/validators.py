from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def get_help_text(self):
        return "영어 대문자, 소문자, 숫자, 특수문자 중 2종류 조합"

    def validate(self, value, user=None):
        length = len(value)

        low_ascii = 0
        up_ascii = 1
        number = 2
        other = 3

        check_string = []

        for i in range(length):
            if len(check_string) >= 2:
                return value
            elif ord('a') <= ord(value[i]) <= ord('z'):
                if low_ascii not in check_string:
                    check_string.append(low_ascii)
                continue
            elif ord('A') <= ord(value[i]) <= ord('Z'):
                if up_ascii not in check_string:
                    check_string.append(up_ascii)
                continue
            elif ord('0') <= ord(value[i]) <= ord('9'):
                if number not in check_string:
                    check_string.append(number)
                continue
            elif other not in check_string:
                check_string.append(other)

        raise ValidationError(_("영어 대문자, 소문자, 숫자, 특수문자 중 2종류 조합"))

