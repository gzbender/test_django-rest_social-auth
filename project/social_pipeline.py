# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from datetime import datetime
from dateutil.relativedelta import relativedelta

def user_details(strategy, details, user=None, *args, **kwargs):
    provider = strategy.backend.name
    gender = None
    age = None
    changed = False
    social = kwargs.get('social')
    if provider == 'vk-oauth2':
        # Получаем пол
        gender_choices = [None, 'female', 'male']
        gender = gender_choices[int(social.extra_data.get('sex', 0))]
        # Получаем возраст
        bd = social.extra_data.get('bdate')
        if bd:
            bd = datetime.strptime(bd, "%d.%m.%Y")
            rd = relativedelta(datetime.today(), bd)
            age = rd.years
    elif provider == 'facebook':
        # Получаем пол
        gender = str(social.extra_data.get('gender'))
        # Получаем возраст
        bd = social.extra_data.get('birthday')
        if bd:
            bd = datetime.strptime(bd, "%m/%d/%Y")
            rd = relativedelta(datetime.today(), bd)
            age = rd.years

    fields = {
        'gender': gender,
        'age': age,
    }
    for name, value in fields.items():
        if value and value != getattr(user, name, None):
            try:
                setattr(user, name, value)
                changed = True
            except AttributeError:
                pass
    if changed:
        strategy.storage.user.changed(user)
