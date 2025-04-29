import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Proverka:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверка результата вычислений")
    def chislo(self):
        """
        Принимает результат вычислений.
        """
        ravno = self.driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text
        return ravno
