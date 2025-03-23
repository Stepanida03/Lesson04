from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

#Переименовать кнопку

driver.get("http://uitestingplayground.com/textinput")

pole = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
pole.send_keys("SkyPro")
sleep(5)

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()
sleep(5)

blue_button.text

get_title = blue_button.text
print(get_title)

driver.quit()
