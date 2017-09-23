#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2017-09-23 15:34:45
# @Last Modified by:   Danny
# @Last Modified time: 2017-09-23 15:34:45
"""
WSGI config for danny_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "danny_blog.settings")

application = get_wsgi_application()
