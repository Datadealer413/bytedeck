from django import template
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from courses.models import MarkRange

User = get_user_model()

register = template.Library()


@register.simple_tag()
def color_style_from_mark(user):
    """ This should go in the style tag: style="{}"
    """
    mark_range = MarkRange.objects.get_range_for_user(user)
    if mark_range:
        if user.profile.dark_theme:
            hex_color = mark_range.color_dark
        else:
            hex_color = mark_range.color_light

        return "background-image: none; background-color: {};".format(hex_color)
    else:
        return ""
