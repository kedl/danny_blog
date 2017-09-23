#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2017-09-23 15:33:14
# @Last Modified by:   Danny
# @Last Modified time: 2017-09-23 15:33:14

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get(r'http://localhost:8000')
        self.assertIn('To-Do lists', self.driver.title)
        #self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')