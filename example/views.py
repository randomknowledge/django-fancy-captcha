# coding: utf-8
from django.shortcuts import render
from django_fancy_captcha.forms import CaptchaTestForm


class MyForm(CaptchaTestForm):
    pass


def index(request):
    form = MyForm(request, num_images=4)
    valid = False

    if request.POST and form.is_valid():
        valid = True
        form.reset_captcha()

    return render(
        request,
        "example/index.html",
        {
            'form': form,
            'valid': valid,
        }
    )