# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import gettext_lazy

from enumfields import TextChoicesEnum, IntegerChoicesEnum, Choice


class Color(TextChoicesEnum):
    __order__ = 'RED GREEN BLUE'

    RED = Choice('r', 'Reddish')
    GREEN = 'g'
    BLUE = Choice('b', gettext_lazy('bluë'))


class Taste(IntegerChoicesEnum):
    SWEET = 1
    SOUR = 2
    BITTER = 3
    SALTY = 4
    UMAMI = 5


class ZeroEnum(IntegerChoicesEnum):
    ZERO = 0
    ONE = 1


class IntegerEnum(IntegerChoicesEnum):
    A = Choice(0, 'foo')
    B = 1
    C = 2


class LabeledEnum(TextChoicesEnum):
    FOO = Choice('foo', 'Foo')
    BAR = Choice('bar', 'Bar')
    FOOBAR = Choice('foobar', 'Foo')  # this is intentional. see test_nonunique_label


class SubIntegerEnum(IntegerChoicesEnum):
    C = Choice(0, 'C', parents=(IntegerEnum.A, IntegerEnum.B))
    D = Choice(1, 'D', parents=(IntegerEnum.B,))


class StateFlowAnyFirst(IntegerChoicesEnum):
    START = Choice(0, 'start', next={'PROCESSING'})
    PROCESSING = Choice(1, 'processing', next={'END'})
    END = Choice(2, 'end', next=set())


class StateFlow(IntegerChoicesEnum):
    START = Choice(4, 'start', next={'PROCESSING'})
    PROCESSING = Choice(5, 'processing', next={'END'}, initial=False)
    END = Choice(6, 'end', next=set(), initial=False)
