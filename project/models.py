# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', u'Male'),
        ('female', u'Female'),
    )
    gender = models.CharField(u'Gender', choices=GENDER_CHOICES, max_length=6, blank=True)
    age = models.SmallIntegerField(u'Age', db_index=True, default=0)
