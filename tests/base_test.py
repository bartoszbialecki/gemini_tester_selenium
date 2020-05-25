import unittest
from selenium import webdriver

PAGE_URL = "https://www.aptekagemini.pl/"


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(PAGE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()
