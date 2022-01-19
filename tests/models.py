from django.db import models

from enumfields import CharEnumField, IntegerEnumField, IntegerEnumSubField

from .enums import Color, IntegerEnum, LabeledEnum, StateFlow, StateFlowAnyFirst, SubIntegerEnum, Taste, ZeroEnum


class MyModel(models.Model):
    color = CharEnumField(Color, max_length=1)
    taste = IntegerEnumField(Taste, default=Taste.SWEET)
    taste_null_default = IntegerEnumField(Taste, null=True, blank=True, default=None)

    default_none = IntegerEnumField(Taste, default=None, null=True, blank=True)
    nullable = IntegerEnumField(Taste, null=True, blank=True)

    random_code = models.TextField(null=True, blank=True)

    zero_field = IntegerEnumField(ZeroEnum, null=True, default=None, blank=True)
    int_enum = IntegerEnumField(IntegerEnum, null=True, default=None, blank=True)
    sub_int_enum = IntegerEnumSubField('int_enum', SubIntegerEnum, null=True, default=None, blank=True)

    zero2 = IntegerEnumField(ZeroEnum, default=ZeroEnum.ZERO)
    labeled_enum = CharEnumField(LabeledEnum, blank=True, null=True)
    state = IntegerEnumField(StateFlow, default=StateFlow.START)
    any_first_state = IntegerEnumField(StateFlowAnyFirst, default=StateFlowAnyFirst.START)
