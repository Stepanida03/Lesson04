from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

#Получить значение атибута src у 3 картинки

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
sleep(15)

order = driver.find_element(By.CSS_SELECTOR, "#award"). get_attribute("src")
print(order)

driver.quit()
