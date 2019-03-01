# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy

from enumfields import Enum, NumEnum, Choice


class Color(Enum):
    __order__ = 'RED GREEN BLUE'

    RED = Choice('r', 'Reddish')
    GREEN = 'g'
    BLUE = Choice('b', ugettext_lazy('bluë'))


class Taste(Enum):
    SWEET = 1
    SOUR = 2
    BITTER = 3
    SALTY = 4
    UMAMI = 5


class ZeroEnum(Enum):
    ZERO = 0
    ONE = 1


class IntegerEnum(NumEnum):
    A = Choice(0, 'foo')
    B = 1


class LabeledEnum(Enum):
    FOO = Choice('foo', 'Foo')
    BAR = Choice('bar', 'Bar')
    FOOBAR = Choice('foobar', 'Foo') # this is intentional. see test_nonunique_label
