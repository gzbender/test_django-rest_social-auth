# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from django import forms
from django.utils.translation import ugettext_lazy as _

from project.models import User

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'gender', 'age')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = UserChangeForm
    add_form = UserCreationForm

#admin.site.unregister(User)
admin.site.register(User, UserAdmin)