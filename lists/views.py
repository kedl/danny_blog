#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2017-09-23 16:18:57
# @Last Modified by:   Danny
# @Last Modified time: 2017-09-23 16:18:57
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'home.html')