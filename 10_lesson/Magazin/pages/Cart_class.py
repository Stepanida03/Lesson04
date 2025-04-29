import allure
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, _driver):
        """
        Инициализация страницы корзины.
        """
        self.driver = _driver

    @allure.step("Добавление товаров в корзину и переход к оформлению заказа")
    def cart(self):
        """
        Добавляет товары в корзину и переходит к оформлению заказа.
        """
        #Выбор товара
        with allure.step("Добавление товара 'Sauce Labs Backpack' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        with allure.step("Добавление товара 'Sauce Labs Bolt T-Shirt' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        with allure.step("Добавление товара 'Sauce Labs Onesie' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # Корзина
        with allure.step("Переход в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()
        with allure.step("Переход к оформлению заказа"):
            self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()