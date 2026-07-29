from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_page():
    options = webdriver.ChromeOptions()
    options.browser_version = "stable"


    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0.5)

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    title = driver.title
    print(title)

    add_box_button = driver.find_element(by=By.XPATH, value="//input[@id='adder' and @type='button']")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')

    add_box_button.send_keys('Selenium')
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    print(text)
    driver.quit()

def test_dynamic_page_with_selenium_doc():
    """
    Учебное задание из документации селениум
    """
    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.browser_version = "stable"
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)

    # Переход на страницу
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

    # Given: бокса ещё нет
    assert driver.find_elements(By.ID, "box0")

    # Получение и проверки видимости кнопки 'Добавить коробку'
    add_box_button = driver.find_element(By.XPATH, value="//input[@id='adder' and @type='button']")
    assert add_box_button.is_displayed()
    # When
    add_box_button.click()

    # Проверка появления первого красного квадрата после нажатия на кнопку add_box_button
    red_box = driver.find_element(By.XPATH, value="//*[@id='box0']")
    assert red_box.is_displayed()


