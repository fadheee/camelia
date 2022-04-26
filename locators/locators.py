from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

class locators:

# XPATH in locators

    username = "/html/body/app-root/app-login/section/div/div[2]/form/input[1]"
    password = "/html/body/app-root/app-login/section/div/div[2]/form/input[2]"
    login_btn = "/html/body/app-root/app-login/section/div/div[2]/form/button"

    # test click ok announcement
    # ancm = drv.find_element(By.CSS_SELECTOR, '[class="button-rounded button-rounded--orange button-rounded--small m-l-10"]')
    search_tab = "/html/body/app-root/app-pages/div/app-header/div[1]/div[2]/ul/li[4]/a"
    fibre_radio = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[1]/div[1]/mat-radio-group/mat-radio-button[2]"
    category = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[1]/div[2]/mat-radio-group/mat-radio-button[2]/label"
    fibre = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[1]/div[2]/div[2]/div/mat-form-field/div/div[1]/div[3]/input"
    submit_btn = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[2]/button[2]"

    # def test_linetest():
    lt_btn = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-service-info-fibre/div/div/div[2]/div[2]/div/app-detail/div/div[3]/div[1]/div"

    # def test_cds():
    cds_radio = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[1]/div[1]/mat-radio-group/mat-radio-button[3]/label"
    cds = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-search/div/div/div[1]/div[2]/div[2]/div/mat-form-field/div/div[1]/div[3]/input"
    cds_btn = "/html/body/app-root/app-pages/div/mat-sidenav-container/mat-sidenav-content/app-red-group-id/div/div/div[2]/div[2]/div/div/app-detail/div/div[3]/div[1]/div"

    # def test_customerID():


    # def test_linetest():
    # def test_updatetime():
    curr_date = "// small[contains(text(), 'Last updated: ')]"




