from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
       #Авторизация
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

class CartPage:

    def __init__(self, _driver):
        self.driver = _driver

    def cart(self):
        #Выбор товара
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # Корзина
        self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

class InformPage:

    def __init__(self, _driver):
        self.driver = _driver

    def inform(self):
        # Заполняем форму своими данными и Нажатие Continue"
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анастасия")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Дрожжина")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("404832")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

class OverviewPage:

    def __init__(self, _driver):
        self.driver = _driver

    def overview(self):
       #Вывести значение 
        itogo = self.driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
        return itogo

   