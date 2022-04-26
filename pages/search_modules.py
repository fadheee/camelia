from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators
import time

class search_modules:
    wait_time_out = 5

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = WW(self.drv, self.wait_time_out)

    def test_searchfibre(self):
        search_tab = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.search_tab)))
        search_tab.click()

        fiber_radio = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.fibre_radio)))
        fiber_radio.click()

        category = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.category)))
        category.click()

        fibre = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.fibre)))
        fibre.send_keys("fai.zalsalim@unifi")

        submit_btn = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.submit_btn)))
        submit_btn.click()
        time.sleep(5)

    def test_searchcds(self):
        search_tab = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.search_tab)))
        search_tab.click()

        cds_radio = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.cds_radio)))
        cds_radio.click()

        category = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.category)))
        category.click()

        cds = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.cds)))
        cds.send_keys("LD1000020010")

        submit_btn = self.wait_variable.until(EC.presence_of_element_located((By.XPATH, locators.submit_btn)))
        submit_btn.click()
        time.sleep(5)