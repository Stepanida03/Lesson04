import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Login_class import LoginPage
from pages.Cart_class import CartPage
from pages.Inform_class import InformPage
from pages.Overview_class import OverviewPage

@allure.title("Сквозной тест покупки товара")
@allure.description("Тест проверяет полный сценарий покупки товара: авторизация, добавление в корзину, заполнение информации и проверка итоговой суммы.")
@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)

def test_shop():
    driver = webdriver.Chrome()
    with allure.step("Авторизация на сайте"):
        login_page = LoginPage(driver)
        login_page.login()
    with allure.step("Добавление товара в корзину"):
        cart_page = CartPage(driver)
        cart_page.cart()
    with allure.step("Заполнение информации о покупателе"):
        inform_page = InformPage(driver)
        inform_page.inform()
    with allure.step("Проверка итоговой суммы заказа"):
        over_page = OverviewPage(driver)
        as_is = over_page.overview()
        total = 'Total: $58.29'
    assert as_is == total

    driver.quit()