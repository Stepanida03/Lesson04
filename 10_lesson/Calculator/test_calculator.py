import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Calc_class import Calculator
from pages.Proverka_class import Proverka

@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка вычисления c задержкой")
@allure.description("Тест проверяет, что калькулятор корректно вычисляет выражение c задержкой.")

def test_calculator():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    pro_verka = Proverka(driver)
    with allure.step("Установка задержки вычислений"):
        calculator.set_pole(45)
    with allure.step("Выполнение вычисления 7 + 8"):
        calculator.batton()

    WebDriverWait(driver, 70).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), '15'))
    
    with allure.step("Проверка результата вычислений"):
        ho_to = pro_verka.chislo()
        itog = '15'
    assert ho_to == itog

    driver.quit() 