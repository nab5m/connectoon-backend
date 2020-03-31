from django.contrib import admin

from work.models import Work, Story, Artwork, ArtworkImage

admin.site.register(Work)
admin.site.register(Story)
admin.site.register(Artwork)
admin.site.register(ArtworkImage)
