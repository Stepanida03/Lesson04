from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import LoginPage
from pages.PageObject import CartPage
from pages.PageObject import InformPage
from pages.PageObject import OverviewPage



def test_shop():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    login_page.login()
    cart_page = CartPage(driver)
    cart_page.cart()
    inform_page = InformPage(driver)
    inform_page.inform()
    over_page = OverviewPage(driver)

    as_is = over_page.overview()

    total = 'Total: $58.29'
    assert as_is == total

    driver.quit()

   