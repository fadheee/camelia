# automation testing on camelia using unittest but not error free (before reconstruct folders :D)

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_modules import login_modules
from pages.search_modules import search_modules
from pages.line_test_modules import line_test_modules


class test_cases_0(unittest.TestCase):
    driver = None
    exec_path = "/usr/bin/chromedriver"
    base_URL = "https://camelia.tm.com.my/login"

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        cls.driver = webdriver.Chrome(executable_path=cls.exec_path)
        driver = cls.driver
        driver.maximize_window()
        driver.get(cls.base_URL)


    def test_login(self):
        login = login_modules(self.driver)
        login.test_login()

    def test_search(self):
        login = login_modules(self.driver)
        login.test_login()

        search = search_modules(self.driver)
        search.test_searchfibre()

    def test_line(self):
        login = login_modules(self.driver)
        login.test_login()

        search = search_modules(self.driver)
        search.test_searchfibre()

        line_test = line_test_modules(self.driver)
        line_test.test_linetest()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
