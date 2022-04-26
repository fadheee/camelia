from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators
import time
import datetime

class line_test_modules:
    wait_time_out = 30

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = WW(self.drv, self.wait_time_out)

    def test_linetestfibre(self):
        line_test = self.wait_variable.until(EC.element_to_be_clickable((By.XPATH, locators.lt_btn)))
        line_test.click()

        time.sleep(10)

        text = self.wait_variable.until(EC.element_to_be_clickable((By.XPATH, locators.curr_date))).text
        curr_date = text[14:30]
        print(curr_date)

        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M")
        print(now)

        if curr_date == now:
            print("Test Passed")
            assert now
        else:
            print("Test Failed")

    def test_linetestcds(self):
        line_test = self.wait_variable.until(EC.element_to_be_clickable((By.XPATH, locators.cds_btn)))
        line_test.click()

        time.sleep(10)

        text = self.wait_variable.until(EC.element_to_be_clickable((By.XPATH, locators.curr_date))).text
        curr_date = text[14:29]
        print(curr_date)

        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M")
        print(now)

        if curr_date == now:
            print("Test Passed")
            assert True
        else:
            print("Test Failed")
            assert False
