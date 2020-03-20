from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import ASCIIUsernameValidator


class Role(models.Model):
    ROLE_CHOICES = (
        (1, 'image_author'),
        (2, 'story_author'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    class Meta:
        verbose_name = '역할'
        verbose_name_plural = '역할'

    def __str__(self):
        return self.ROLE_CHOICES[self.id - 1][1]


class Account(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        _('아이디'),
        max_length=150,
        unique=True,
        help_text=_('4~150자의 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'),
        validators=[username_validator, MinLengthValidator(4)],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('이메일'), unique=True)
    roles = models.ManyToManyField(Role, blank=True)
    # null=True, to create superuser
    name = models.CharField(_('이름'), max_length=50, null=True)
    
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.username + ' ' + self.name
