# coding: utf-8
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import Library
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django_fancy_captcha.utils import session_key, cb_key, create_session_data


register = Library()


@register.filter(name='times')
def times(number):
    return range(number)


@register.simple_tag
def fancycaptcha_image(session, cube_num, image_num, num_cubes):
    create_session_data(session, num_cubes)

    return '<img src="{0}?{1}" width="{2}" height="{2}">'.format(
        reverse('image', kwargs={
            'cube_num': cube_num,
            'image_num': image_num,
            'num_cubes': num_cubes,
        }),
        session[session_key][cb_key],
        settings.FANCY_CAPTCHA_IMAGE_SIZE,
    )


@register.simple_tag
def fancycaptcha_css():
    css = render_to_string(
        'django_fancy_captcha/fancycaptcha.css.tpl',
        {'cube_size': settings.FANCY_CAPTCHA_IMAGE_SIZE}
    )

    return mark_safe('<style type="text/css">{0}</style>'.format(css))