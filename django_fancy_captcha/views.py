# coding=utf-8
from django_fancy_captcha.utils import create_session_data, session_key, cubes_key, images_key
from django.views.decorators.cache import never_cache
from django.http import HttpResponse


@never_cache
def image(request, cube_num, image_num, num_cubes):
    cube_num = int(cube_num)
    image_num = int(image_num)
    num_cubes = int(num_cubes)

    create_session_data(request.session, num_cubes)

    session_data = request.session[session_key]
    images = session_data[cubes_key][cube_num]
    img = images[image_num]

    return HttpResponse(session_data[images_key][img], mimetype="image/jpeg")
