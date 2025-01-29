from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
#Клик по кнопке

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(By.XPATH, "//button[text() = 'Add Element']")

for x in range(0, 5):
    add_button.click()

delete_button = driver.find_elements(By.XPATH, "//button[text() = 'Delete']")

print(len(delete_button))
sleep(3)

#Клик по кнопке без ID

driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
sleep(3)

#Клик по кнопке с CSS-классом

driver.get("http://uitestingplayground.com/classattr")
sleep(3)

driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
sleep(3)

alert = Alert(driver)
alert.accept()
sleep(3)

driver.quit()
