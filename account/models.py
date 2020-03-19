from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    roles = models.ManyToManyField(Role, blank=True)
    # null=True, to create superuser
    name = models.CharField(_('이름'), max_length=50, null=True)
    
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.username + ' ' + self.name
