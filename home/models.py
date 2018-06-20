# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class News(Base):
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = ' Новини'

    img = models.ImageField(upload_to='books/', null=True, blank=True)
    title = models.TextField(max_length=250, db_index=True)
    description = models.TextField(verbose_name=u'Oпис події')
    more_description = models.TextField(blank=True, null=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Carusel(models.Model):
    image = models.ImageField(upload_to='slider/', null=True, blank=True)
    name = models.CharField(max_length=50, db_index=True)
    desc = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    images = models.ImageField(upload_to='photoes/', null=True, blank=True)


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
    name = models.CharField(max_length=80)
    photo = models.ManyToManyField(Photo)


class Comment(models.Model):
    user = models.ForeignKey(User)
    news = models.ForeignKey(News)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Events(models.Model):
    class Meta:
        ordering = ('-time',)
        indexes = [
            models.Index(fields=['time']),
        ]
        verbose_name = 'Події'
        verbose_name_plural = 'Події'
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=400)

    def __str__(self):
        return self.title

    def datepublished(self):
        return self.time.strftime('%B %d %Y')

