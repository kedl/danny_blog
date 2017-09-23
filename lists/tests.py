#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2017-09-23 16:12:02
# @Last Modified by:   Danny
# @Last Modified time: 2017-09-23 16:12:02
from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)