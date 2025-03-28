from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

#Заполнение формы

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

pole = driver.find_element(By.CSS_SELECTOR,"#delay")

pole.clear()

pole.send_keys(45)

#Ввод расчета
button_7 = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
button_p = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
button_8 = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
button_s = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()

WebDriverWait(driver, 70).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), '15')
)

#Проверочка
itog = driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text
assert itog == "15"

print(itog)

driver.quit()
