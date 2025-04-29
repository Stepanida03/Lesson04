import allure
from selenium.webdriver.common.by import By

class InformPage:

    def __init__(self, _driver):
        """
        Инициализация страницы ввода информации.
        """
        self.driver = _driver

    @allure.step("Заполняем форму своими данными и Нажатие Continue")
    def inform(self):
        """
        Заполняет форму (имя, фамилия, почтовый индекс) и нажимаем continue.
        """
        with allure.step("Заполнение поля 'Имя'"):
            self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анастасия")
        with allure.step("Заполнение поля 'Фамилия'"):
            self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Дрожжина")
        with allure.step("Заполнение поля 'Почтовый индекс'"):
            self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("404832")
        with allure.step("Нажатие кнопки 'Продолжить'"):
            self.driver.find_element(By.CSS_SELECTOR, "#continue").click()