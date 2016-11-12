#-*- coding: utf-8 -*-

__all__ = ['make_password', 'check_password', 'refresh_token_gen']


import contextlib
import random
import string

random_generator = random.SystemRandom()
KEY_CHARACTERS = string.letters + string.digits


def refresh_token_gen(length=40):
    return ''.join([random.choice(KEY_CHARACTERS) for _ in range(length)])


@contextlib.contextmanager
def django_manager(func_name):
    """
    """

    from django.conf import settings

    if not settings.configured:
        settings.configure()

    import django.contrib.auth.hashers as django_util

    try:
        yield  getattr(django_util, func_name)

    except AttributeError:
        raise  TypeError("Django manager provides: <make_password>, <check_password>.")


def make_password(raw_password):
    with django_manager("make_password") as dj_make_password:
        return dj_make_password(raw_password)


def check_password(raw_password, encrypted):
    with django_manager("check_password") as dj_check_password:
        return dj_check_password(raw_password, encrypted)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

