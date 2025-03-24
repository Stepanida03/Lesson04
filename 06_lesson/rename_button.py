from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 5)

#Переименовать кнопку

driver.get("http://uitestingplayground.com/textinput")

pole = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"),"SkyPro")
    )

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(blue_button)

driver.quit()

