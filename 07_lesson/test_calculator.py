from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import Calculator

def test_calculator():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    calculator.set_pole(45)
    calculator.batton()
    
    
    WebDriverWait(driver, 70).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), '15'))

   #Проверочка
    itog = driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text
    assert itog == "15"

    print(itog)

    driver.quit()

 
