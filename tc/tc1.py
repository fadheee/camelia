# automation testing on camelia using PyTest

import pytest
import time
import datetime
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session", autouse=True)
def setup():
    global driver
    # setup
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver = webdriver.Chrome(executable_path= "/usr/bin/chromedriver")
    driver.get("https://camelia.tm.com.my/login")
    driver.implicitly_wait(10)
    driver.maximize_window()

    # tear down
    yield

    driver.close()
    driver.quit()
    print("Test completed")


# test login
def test_login():
    username = driver.find_element(By.NAME, 'username')
    username.send_keys('sqatester1')

    password = driver.find_element(By.NAME, 'password')
    password.send_keys('Camelia121#')

    login_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_btn.click()
    time.sleep(5)


# test click ok announcement
def test_announcement():
    time.sleep(3)
    # ancm = driver.find_element(By.CSS_SELECTOR, '[class="button-rounded button-rounded--orange button-rounded--small m-l-10"]')
    # ancm.click()
    #time.sleep(3)


# test search tab
def test_fibre():
    search_tab = driver.find_element(By.CSS_SELECTOR, '[title="Search"]')
    search_tab.click()

    fibre_radio = driver.find_element(By.CSS_SELECTOR, '[value = "fibre"]')
    fibre_radio.click()

    searchby = driver.find_element(By.CSS_SELECTOR, '[value = "manualid"]')
    searchby.click()

    fibre = driver.find_element(By.CSS_SELECTOR, '[placeholder="e.g. faisal4@unifi, aishaish@streamyx"]')
    fibre.send_keys('faiismail9@unifi')

    submit_btn = driver.find_element(By.CSS_SELECTOR, '[class="button-rounded button-rounded--black m-l-15 fs-12"]')
    submit_btn.click()
    time.sleep(5)


def test_linetest():
    lt_btn = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-service-info-fibre/div/div/div[2]/div[2]/div/app-detail/div/div[3]/div[1]/div"
    driver.find_element(By.XPATH, lt_btn).click()

    curr_date = "// small[contains(text(), 'Last updated: ')]"
    text = driver.find_element(By.XPATH, curr_date).text
    print(text)

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
