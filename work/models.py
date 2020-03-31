import os
import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from connectoon import settings


class Work(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_works",
        related_query_name="liked_work",
        verbose_name=_("좋아요"),
        blank=True
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="disliked_works",
        related_query_name="disliked_work",
        verbose_name=_("싫어요"),
        blank=True
    )
    chapter = models.PositiveIntegerField(_('챕터'))

    title = models.CharField(_('제목'), max_length=255)
    description = models.CharField(_('설명'), max_length=500)

    CATEGORY_CHOICES = (
        (1, 'romance'),
        (2, 'life'),
        (3, 'fun'),
        (4, 'fantasy'),
        (5, 'action'),
        (6, 'drama'),
        (7, 'thrill'),
        (8, 'history'),
        (9, 'sports'),
    )
    category = ArrayField(
        models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES),
        verbose_name=_('카테고리'),
        size=3
    )

    class Meta:
        verbose_name = _("작품")
        verbose_name_plural = verbose_name


class Story(Work):
    content = models.TextField(_("스토리 본문"))
    
    class Meta:
        verbose_name = _("스토리")
        verbose_name_plural = verbose_name


def get_uuid_artwork_image_url(instance, filename):
    extension = os.path.splitext(filename)[1]
    return 'artwork/' + str(uuid.uuid4()) + extension


class Artwork(Work):

    class Meta:
        verbose_name = _("작화")
        verbose_name_plural = verbose_name


class ArtworkImage(models.Model):
    artwork = models.ForeignKey('Artwork', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_uuid_artwork_image_url)
    
    class Meta:
        verbose_name = _("작화 이미지")
        verbose_name_plural = verbose_name
