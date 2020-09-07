import time
# import datetime

from selenium import webdriver
import HtmlTestRunner
import unittest

# import sys

import os
#############################################
#python -m unittest pytest1.py
#####################################################
path = os.path.dirname(__file__)
# print(path)
url = "http://13.233.174.122/"

class awstest(unittest.TestCase):


    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=path + "/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_loginPageTitle(self):
        self.driver.get(url)
        self.assertEqual("Login", self.driver.title, "login success")
        # xpath = "//*[text()=' Login form ']"
        # self.assertEqual(" Login form ", self.driver.find_elements_by_xpath(xpath),"Application launch success")

    def test_loginsuccess(self):
        self.driver.get(url)
        self.driver.find_element_by_name('username').send_keys('asd')
        self.driver.find_element_by_name('password').send_keys('asd')
        self.driver.find_element_by_xpath("//button[text()='Login']").click()
        time.sleep(2)
        self.assertEqual("Welcome", self.driver.title, "login success")

    def test_loginfail(self):
        self.driver.get(url)
        self.driver.find_element_by_name('username').send_keys('testfail')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_xpath("//button[text()='Login']").click()
        self.assertEqual("Login", self.driver.title, "login fail check")
        # if self.assertEqual("Welcome", self.driver.title, "login Fail"):
        #     print("TC pass")
        # else:
        #     print("TC fail")

    def test_registryPageCheck(self):
        self.driver.get(url)
        self.driver.find_element_by_xpath("//*[text()=' Register Yourself ']").click()
        self.assertEqual("Registration", self.driver.title, "Registratin page success")

    def test_booksearch(self):
        self.driver.get(url)
        self.driver.find_element_by_name('username').send_keys('asd')
        self.driver.find_element_by_name('password').send_keys('asd')
        self.driver.find_element_by_xpath("//button[text()='Login']").click()
        time.sleep(2)
        self.assertEqual("Welcome", self.driver.title, "login success")
        self.driver.find_element_by_name("query").send_keys("book")
        self.driver.find_element_by_xpath("//*[text()='Search']").click()

    def test_logout(self):
        self.driver.get(url)
        self.driver.find_element_by_name('username').send_keys('asd')
        self.driver.find_element_by_name('password').send_keys('asd')
        self.driver.find_element_by_xpath("//button[text()='Login']").click()
        time.sleep(2)
        self.assertEqual("Welcome", self.driver.title, "login success")
        self.driver.find_element_by_name("query").send_keys("book")
        self.driver.find_element_by_xpath("//*[text()='logout']").click()

    @classmethod
    def tearDown(cls):
        # cls.driver.close()
        cls.driver.quit()
        print("Test complete")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./report/"))
