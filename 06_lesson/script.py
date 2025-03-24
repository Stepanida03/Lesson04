from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

#Получить текст из зеленой плашки

driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

green_line = driver.find_element(By.CSS_SELECTOR, "#content > p").text
print(green_line)

driver.quit()
