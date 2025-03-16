from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Firefox()

#Клик по кнопке

driver.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)")))

close_button.click()

#Поле ввода

driver.get("http://the-internet.herokuapp.com/inputs")


pole = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/input")

pole.send_keys(1000)
sleep(3)

pole.clear()
sleep(3)

pole.send_keys(999)

#Форма авторизации



driver.get("http://the-internet.herokuapp.com/login")


pole_username = driver.find_element(By.CSS_SELECTOR, "#username")
pole_username.send_keys("tomsmith")
sleep(2)

pole_password = driver.find_element(By.CSS_SELECTOR, "#password")
pole_password.send_keys("SuperSecretPassword!")
sleep(2)

Login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa")))
Login_button.click()

sleep(3)
driver.quit()
