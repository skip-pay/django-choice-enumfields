# -- encoding: UTF-8 --
from __future__ import unicode_literals

import pytest
from django.core.exceptions import ValidationError
from django.forms import BaseForm

from enumfields import Choice, TextChoicesEnum, CharEnumField

from .enums import Color, IntegerEnum


def test_choice_ordering():
    EXPECTED_CHOICES = (
        ('r', 'Reddish'),
        ('g', 'Green'),
        ('b', 'bluë'),
    )
    for ((ex_key, ex_val), (key, val)) in zip(EXPECTED_CHOICES, Color.choices):
        assert key == ex_key
        assert str(val) == str(ex_val)


def test_custom_labels():
    # Custom label
    assert Color.RED.label == 'Reddish'
    assert str(Color.RED) == 'Reddish'
    assert str(IntegerEnum.A) == 'foo'


def test_automatic_labels():
    # Automatic label
    assert Color.GREEN.label == 'Green'
    assert str(Color.GREEN) == 'Green'
    assert str(IntegerEnum.B) == 'B'


def test_lazy_labels():
    # Lazy label
    assert isinstance(str(Color.BLUE), str)
    assert str(Color.BLUE) == 'bluë'


def test_formfield_labels():
    # Formfield choice label
    form_field = CharEnumField(Color).formfield()
    expectations = dict((val.value, str(val)) for val in Color)
    for value, text in form_field.choices:
        if value:
            assert text == expectations[value]


def test_formfield_functionality():
    form_cls = type(str("FauxForm"), (BaseForm,), {
        "base_fields": {"color": CharEnumField(Color).formfield()}
    })
    form = form_cls(data={"color": "r"})
    assert not form.errors
    assert form.cleaned_data["color"] == Color.RED


def test_invalid_to_python_fails():
    with pytest.raises(ValidationError) as ve:
        CharEnumField(Color).to_python("invalid")
    assert ve.value.code == "invalid_enum_value"


def test_import_by_string():
    assert CharEnumField("tests.test_enums.Color").enum == Color


def test_choice_enum_should_be_unique():
    with pytest.raises(ValueError):
        class DuplicateEnum(TextChoicesEnum):
            A = Choice(1, 'a')
            B = Choice(1, 'b')
