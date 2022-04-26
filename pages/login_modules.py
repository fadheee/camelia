from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators
import time

class login_modules:
    wait_time_out = 5
    cameliausername = 'sqatester1'
    cameliapassword = 'Camelia121#'

    def __init__(self, drv):
        self.drv = drv
        self.wait = WW(self.drv, self.wait_time_out)

    def test_login(self):
        time.sleep(5)
        username = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.username)))
        username.clear()
        username.send_keys(self.cameliausername)

        password = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.password)))
        password.clear()
        password.send_keys(self.cameliapassword)

        login_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_btn)))
        login_btn.click()
