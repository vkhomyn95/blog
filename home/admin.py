# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from home.models import News, Carusel, Gallery, Photo, Comment, Events

# Register your models here.

admin.site.register(News)
admin.site.register(Carusel)
admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Events)
