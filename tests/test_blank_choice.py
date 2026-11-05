import django
import pytest
from django.db import models
from django.test import override_settings

from .models import MyModel

DJANGO_DASH = ('', '---------')


def get_enum_choices(*args, **kwargs):
    return list(MyModel._meta.get_field('int_enum').get_choices(*args, **kwargs))


def get_plain_choices(*args, **kwargs):
    return list(models.IntegerField(choices=[(0, 'foo')], null=True, blank=True).get_choices(*args, **kwargs))


def test_blank_choice_matches_plain_field():
    assert get_enum_choices()[0] == get_plain_choices()[0]
    assert get_enum_choices()[1:] == [(0, 'foo'), (1, 'B'), (2, 'C')]


@pytest.mark.skipif(django.VERSION < (6, 1), reason='USE_BLANK_CHOICE_DASH was added in Django 6.1')
@pytest.mark.parametrize('use_blank_choice_dash', [True, False])
@pytest.mark.filterwarnings('ignore:The USE_BLANK_CHOICE_DASH setting is deprecated')
def test_blank_choice_follows_use_blank_choice_dash_setting(use_blank_choice_dash):
    with override_settings(USE_BLANK_CHOICE_DASH=use_blank_choice_dash):
        blank_choice = get_enum_choices()[0]
        assert blank_choice == get_plain_choices()[0]
    assert (blank_choice == DJANGO_DASH) is use_blank_choice_dash


@pytest.mark.skipif(django.VERSION >= (6, 1), reason='Django 6.1 decides the blank choice label from settings')
def test_blank_choice_is_dash_before_django_6_1():
    assert get_enum_choices()[0] == DJANGO_DASH


def test_explicit_blank_choice_is_used():
    blank_choice = [('', 'Any')]
    assert get_enum_choices(blank_choice=blank_choice) == blank_choice + [(0, 'foo'), (1, 'B'), (2, 'C')]
    assert get_enum_choices(True, blank_choice) == blank_choice + [(0, 'foo'), (1, 'B'), (2, 'C')]


def test_blank_choice_can_be_excluded():
    assert get_enum_choices(include_blank=False) == [(0, 'foo'), (1, 'B'), (2, 'C')]
