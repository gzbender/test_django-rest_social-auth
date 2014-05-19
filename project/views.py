# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.views.generic import View
from django.shortcuts import render

from project.serializers import UserSerializer
from project.models import User
import social.apps.django_app.urls

class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filter_fields = ('age',)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CurrentUserDetail(generics.RetrieveUpdateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        response = super(CurrentUserDetail, self).patch(request, *args, **kwargs)
        if response.status_code == 200:
            response.status_code = 202
        return response