from django.db import models

from enumfields import EnumField, NumEnumField

from .enums import Color, IntegerEnum, LabeledEnum, Taste, ZeroEnum


class MyModel(models.Model):
    color = EnumField(Color, max_length=1)
    taste = EnumField(Taste, default=Taste.SWEET)
    taste_null_default = EnumField(Taste, null=True, blank=True, default=None)
    taste_int = NumEnumField(Taste, default=Taste.SWEET)

    default_none = NumEnumField(Taste, default=None, null=True, blank=True)
    nullable = NumEnumField(Taste, null=True, blank=True)

    random_code = models.TextField(null=True, blank=True)

    zero_field = NumEnumField(ZeroEnum, null=True, default=None, blank=True)
    int_enum = NumEnumField(IntegerEnum, null=True, default=None, blank=True)

    zero2 = NumEnumField(ZeroEnum, default=ZeroEnum.ZERO)
    labeled_enum = EnumField(LabeledEnum, blank=True, null=True)
