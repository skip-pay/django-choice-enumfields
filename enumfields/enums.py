import enum
from django.db.models.enums import ChoicesMeta


class Choice:

    def __init__(self, value, label=None, next=None, initial=True, **kwargs):
        self.value = value
        self.label = label
        self.next = next
        self.initial = initial
        self.extra = kwargs


def set_enum_attribute(enum, name, value_map):
    setattr(enum, name, property(lambda self: value_map[self.value].get(name)))


class ChoiceEnumMeta(ChoicesMeta):

    def __new__(metacls, classname, bases, classdict):
        extra_keys = {'next', 'initial'}

        extra_data = []
        for key in classdict._member_names:
            value = classdict[key]
            if isinstance(value, Choice):
                choice = value
                value = choice.value
                label = choice.label
                extra_keys.update(choice.extra.keys())
                extra_data.append({
                    'next': choice.next,
                    'initial': choice.initial,
                    **choice.extra
                })

                if label is not None:
                    if not isinstance(value, (list, tuple)):
                        value = (value, label)
                    else:
                        value = tuple(value) + tuple(label)
            dict.__setitem__(classdict, key, value)
        cls = super().__new__(metacls, classname, bases, classdict)
        cls._value2data_map_ = dict(zip(cls._value2member_map_, extra_data))

        for key in extra_keys:
            set_enum_attribute(cls, key, cls._value2data_map_)
        return cls


def class_to_str(cls):
    if cls.__class__ == type:
        return cls
    else:
        return '{}.{}'.format(cls.__module__, cls.__name__)


class ChoicesEnum(enum.Enum, metaclass=ChoiceEnumMeta):

    def deconstruct_choice(self):
        keywords = {'value': self.value}
        if self.initial is not None:
            keywords['initial'] = self.initial
        if self.next is not None:
            keywords['next'] = self.next
        return self.name, keywords

    @classmethod
    def deconstruct_cls(cls):
        name = cls.__name__
        if len(cls.__bases__) > 2:
            return name, class_to_str(cls), None, None
        if len(cls.__bases__) == 1:
            enum_type, enum_base = None, class_to_str(cls.__bases__[0])
        elif len(cls.__bases__) == 2:
            enum_type, enum_base = [class_to_str(base) for base in cls.__bases__]
        return name, enum_base, enum_type, dict(choice.deconstruct_choice() for choice in cls)

    def __str__(self):
        """
        Show our label when Django uses the Enum for displaying in a view
        """
        return str(self.label)


class IntegerChoicesEnum(int, ChoicesEnum):
    pass


class TextChoicesEnum(str, ChoicesEnum):

    def _generate_next_value_(name, start, count, last_values):
        return name
