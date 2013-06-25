# coding: utf-8
import time
import os
import re
import random
from django.conf import settings
from django.core.cache import cache


session_key = "fancycaptcha_data"
cubes_key = "cubes"
images_key = "images"
cb_key = "cb"


def create_session_data(session, num_cubes, force=False):
    if not session_key in session or force:
        session[session_key] = {
            cubes_key: [],
            cb_key: time.time()
        }
        for i in range(10):
            session[session_key][cubes_key].append(None)
    all_images = cache.get("fancycaptcha_images")
    if not all_images:
        all_images = filter(
            lambda x: bool(re.search(settings.FANCY_CAPTCHA_IMAGE_PATTERN, x)),
            os.listdir(settings.FANCY_CAPTCHA_IMAGES_DIR)
        )
        cache.set("fancycaptcha_images", all_images)

    _generate_session_images(session, all_images, num_cubes, force=force)


def _generate_session_images(session, all_images, num_cubes, force=False):
    session_data = session[session_key]

    changed = False

    if not images_key in session_data:
        session_data[images_key] = {}

    for i in range(num_cubes):
        if not session_data[cubes_key][i] or force:
            changed = True
            images = list(all_images)
            images = random.sample(images, num_cubes - 1)
            images.append(settings.FANCY_CAPTCHA_CORRECT_IMAGE)
            random.shuffle(images)
            session_data[cubes_key][i] = images
            for img in images:
                img_abs = os.path.join(settings.FANCY_CAPTCHA_IMAGES_DIR, img)
                session_data[images_key][img] = open(img_abs, 'rb').read()
    if changed:
        session[session_key] = session_data