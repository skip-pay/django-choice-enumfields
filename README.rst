This package lets you use real Python (PEP435_-style) enums with Django.

.. image:: https://travis-ci.org/hzdg/django-enumfields.svg?branch=master
    :target: https://travis-ci.org/hzdg/django-enumfields


Installation
------------

1. ``pip install django-enumfields``


Included Tools
--------------


EnumField, NumEnumField
```````````````````````

.. code-block:: python

    from enumfields import EnumField
    from enumfields import ChoiceEnum  # Uses Ethan Furman's "enum34" backport

    class Color(ChoiceEnum):
        RED = 'r'
        GREEN = 'g'
        BLUE = 'b'

    class MyModel(models.Model):

        color = EnumField(Color, max_length=1)

Elsewhere:

.. code-block:: python

    m = MyModel.objects.filter(color=Color.RED)

``NumEnumField`` works identically, but the underlying storage mechanism is
an ``IntegerField`` instead of a ``CharField``.


EnumSubField, NumEnumSubField
`````````````````````````````

.. code-block:: python

    from enumfields import EnumField, EnumSubField
    from enumfields import ChoiceEnum

    class Color(ChoiceEnum):
        RED = 'r'
        GREEN = 'g'
        BLUE = 'b'

    class ColorType(ChoiceEnum):
        LIGHT = Choice('l', 'light', parents=(Color.RED, Color.BLUE))
        DARK = Choice('d', 'dard', parents=(Color.RED, Color.GREEN))
        TRANSPARENT = Choice('t', 'transparent', parents=(Color.GREEN))

    class MyModel(models.Model):

        color = EnumField(Color, max_length=1)
        color_type = EnumSubField('color', ColorType, max_length=1)

    MyModel(color=Color.RED, color_type=Color.LIGHT).full_clean()  # OK
    MyModel(color=Color.RED, color_type=Color.TRANSPARENT).full_clean()  # Raise ValidationError

``EnumSubField`` automatically validates if parents requirement is satisfied.

Usage in Forms
~~~~~~~~~~~~~~

Call the ``formfield`` method to use an ``EnumField`` directly in a ``Form``.

.. code-block:: python

    class MyForm(forms.Form):

        color = EnumField(Color, max_length=1).formfield()

ChoiceEnum
``````````

Normally, you just use normal PEP435_-style enums, however, django-enumfields
also encludes its own version of ChoiceEnum with a few extra bells and whistles.
Namely, the smart definition of labels which are used, for example, in admin
dropdowns. By default, it will create labels by title-casing your constant
names. You can provide custom labels with using Choice to define enum item.

.. code-block:: python

    from enumfields import EnumField, ChoiceEnum, Choice  # Our own Enum class

    class Color(ChoiceEnum):
        RED = Choice('r', 'A custom label')
        GREEN = 'g'
        BLUE = 'b'

    class MyModel(models.Model):
        color = EnumField(Color, max_length=1)

    assert Color.GREEN.label == 'Green'
    assert Color.RED.label == 'A custom label'


.. _PEP435: http://www.python.org/dev/peps/pep-0435/


EnumFieldListFilter
```````````````````

``enumfields.admin.EnumFieldListFilter`` is provided to allow using enums in
``list_filter``.


.. code-block:: python

    from enumfields.admin import EnumFieldListFilter

    class MyModelAdmin(admin.ModelAdmin):
      list_filter = [('color', EnumFieldListFilter)]
