#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2017-09-23 15:33:14
# @Last Modified by:   Danny
# @Last Modified time: 2017-09-23 15:33:14

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'http://localhost:8000')

assert 'Django' in driver.title

driver.quit()