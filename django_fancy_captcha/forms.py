from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import Field, MultiWidget, HiddenInput, Widget, Form
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class FancyCaptchaImageWidget(Widget):
    user_session = None

    def __init__(self, attrs=None, num_images=4):
        self.num_images = num_images
        super(FancyCaptchaImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return render_to_string(
            "django_fancy_captcha/cubes.html",
            {
                'count': self.num_images,
                'id': 'fancycaptcha_0',
                'session': self.user_session,
            },
        )


class FancyCaptchaInput(MultiWidget):
    _user_session = None
    _num_images = 4

    def __init__(self, attrs=None, **kwargs):
        attrs = {'id': 'fancycaptcha'}
        widgets = (
            HiddenInput(attrs),
            FancyCaptchaImageWidget(attrs, num_images=kwargs.pop('num_images', 4)),
        )
        super(FancyCaptchaInput, self).__init__(widgets, attrs, **kwargs)

    def _set_user_session(self, value):
        self._user_session = value
        self.widgets[1].user_session = value

    def _get_user_session(self):
        return self._user_session

    def _set_num_images(self, value):
        self._num_images = value
        self.widgets[1].num_images = value

    def _get_num_images(self):
        return self._num_images

    user_session = property(_get_user_session, _set_user_session)
    num_images = property(_get_num_images, _set_num_images)

    def decompress(self, value):
        if value:
            return value.split(',')
        return []

    def value_from_datadict(self, data, files, name):
        widgets = filter(lambda w: isinstance(w, HiddenInput), self.widgets)
        return [widget.value_from_datadict(data, files, name + '_%s' % i) for i, widget in enumerate(widgets)]


class FancyCaptchaField(Field):
    _user_session = None
    _num_images = 4

    def __init__(self, *args, **kwargs):
        self.num_images = kwargs.pop('num_images', 4)
        self.widget = FancyCaptchaInput(num_images=self.num_images)
        if 'error_messages' not in kwargs or 'invalid' not in kwargs.get('error_messages'):
            if 'error_messages' not in kwargs:
                kwargs['error_messages'] = {}
            kwargs['error_messages'].update({'invalid': _('Invalid CAPTCHA')})
        super(FancyCaptchaField, self).__init__(*args, **kwargs)

    def _set_user_session(self, value):
        self._user_session = value
        self.widget.user_session = value

    def _get_user_session(self):
        return self._user_session

    def _set_num_images(self, value):
        self._num_images = value
        self.widget.num_images = value

    def _get_num_images(self):
        return self._num_images

    user_session = property(_get_user_session, _set_user_session)
    num_images = property(_get_num_images, _set_num_images)

    def clean(self, value):
        super(FancyCaptchaField, self).clean(value)
        value = [int(v) for v in value[0].split(',')]

        if not self.user_session:
            self.raise_error()

        key = "fancycaptcha_data"
        if not key in self.user_session:
            self.raise_error()
        elif not "cubes" in self.user_session[key]:
            self.raise_error()
        for i in range(self.num_images):
            if not self.user_session[key]["cubes"][i]:
                self.raise_error()
            else:
                data = self.user_session[key]["cubes"][i]
                tmp = data[1]
                data[1] = data[2]
                data[2] = tmp
                if data[value[i]] != settings.FANCY_CAPTCHA_CORRECT_IMAGE:
                    self.raise_error()
        return value

    def raise_error(self):
        raise ValidationError(getattr(self, 'error_messages', {}).get('invalid', _('Invalid CAPTCHA')))


class CaptchaTestForm(Form):
    captcha = FancyCaptchaField()

    def __init__(self, request, num_images, **kwargs):
        self.request = request
        super(CaptchaTestForm, self).__init__(request.POST or None, **kwargs)
        if request and request.session:
            self.fields['captcha'].user_session = request.session
        self.fields['captcha'].num_images = num_images

    def reset_captcha(self):
        try:
            del self.fields['captcha'].user_session["fancycaptcha_data"]
        except KeyError:
            pass