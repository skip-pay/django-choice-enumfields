# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy

from enumfields import ChoiceEnum, NumChoiceEnum, Choice


class Color(ChoiceEnum):
    __order__ = 'RED GREEN BLUE'

    RED = Choice('r', 'Reddish')
    GREEN = 'g'
    BLUE = Choice('b', ugettext_lazy('bluë'))


class Taste(ChoiceEnum):
    SWEET = 1
    SOUR = 2
    BITTER = 3
    SALTY = 4
    UMAMI = 5


class ZeroEnum(ChoiceEnum):
    ZERO = 0
    ONE = 1


class IntegerEnum(NumChoiceEnum):
    A = Choice(0, 'foo')
    B = 1
    C = 2


class LabeledEnum(ChoiceEnum):
    FOO = Choice('foo', 'Foo')
    BAR = Choice('bar', 'Bar')
    FOOBAR = Choice('foobar', 'Foo')  # this is intentional. see test_nonunique_label


class SubIntegerEnum(NumChoiceEnum):
    C = Choice(0, 'C', parents=(IntegerEnum.A, IntegerEnum.B))
    D = Choice(1, 'D', parents=(IntegerEnum.B,))
