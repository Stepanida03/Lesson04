import allure
from selenium.webdriver.common.by import By

class LoginPage:
  
    def __init__(self, _driver):
        """
        Инициализация страницы авторизации.
        """
        self.driver = _driver
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
        """
        Выполнение авторизации.
        """
        with allure.step("Заполнение поля 'Логин'"):
            self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        with allure.step("Заполнение поля 'Пароль'"):
            self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        with allure.step("Нажимаем кнопку Login"):
            self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()