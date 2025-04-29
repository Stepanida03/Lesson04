import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator: 

    def __init__(self, driver): 
        """
        Инициализация страницы калькулятора.
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки вычислений")
    def set_pole(self, delay):
        """
        Очистка и изменение значений поля задержки.
        """
        pole = self.driver.find_element(By.CSS_SELECTOR,"#delay")
        pole.clear()
        pole.send_keys(delay)

    @allure.step("Последовательное нажатие кнопок для вычислений")
    def batton(self):
        """
        Нажимаем кнопки на калькуляторе.
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()