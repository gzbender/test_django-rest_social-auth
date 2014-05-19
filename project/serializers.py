# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from rest_framework import serializers

from project.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'age')