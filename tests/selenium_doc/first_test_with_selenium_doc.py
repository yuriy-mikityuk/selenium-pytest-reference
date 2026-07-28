from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.browser_version = "stable"


driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)

driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
title = driver.title
print(title)

text_box = driver.find_element(by=By.XPATH, value="//input[@id='adder' and @type='button']")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')

text_box.send_keys('Selenium')
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)
driver.quit()
