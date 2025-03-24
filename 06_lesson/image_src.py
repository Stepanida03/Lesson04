from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40)

#Получить значение атибута src у 3 картинки

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"),"Done!")
    )

order = driver.find_element(By.CSS_SELECTOR, "#award"). get_attribute("src")
print(order)

driver.quit()
