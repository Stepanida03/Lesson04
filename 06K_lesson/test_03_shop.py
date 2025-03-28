from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 30)

driver.get("https://www.saucedemo.com/")

#Авторизация

pole = driver.find_element(By.CSS_SELECTOR,"#user-name")
pole.send_keys("standard_user")

pole = driver.find_element(By.CSS_SELECTOR,"#password")
pole.send_keys("secret_sauce")

button_1 = driver.find_element(By.CSS_SELECTOR, "#login-button").click()

#Выбор товара
tovar_1_1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
tovar_2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
tovar_3 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

#Вход в корзину
cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").click()

#Нажатие Checkout

button_2 = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

#Заполнение формы

pole_i = driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анастасия")
pole_f = driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Дрожжина")
pole_ad = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("404832")

#Нажатие Continue

button_2 = driver.find_element(By.CSS_SELECTOR, "#continue").click()

#Вывести значение 

Total = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text

#Закрыть браузер нажатие Finish

button_3 = driver.find_element(By.CSS_SELECTOR, "#finish").click()

#Проверочка

assert Total == "Total: $58.29"

if Total == "Total: $58.29":
    print ("Итоговая сумма = $58.29")
else: print("ошибка")

driver.quit()
