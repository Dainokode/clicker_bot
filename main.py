import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


chrome_driver_path = "C:\\Users\\amton\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element_by_css_selector("#cookie")


timeout = time.time() + 60 * 1
while True:
    cookie.click()


    if time.time() > timeout:
        cookie_seconds = driver.find_element_by_css_selector("#cps")
        print(cookie_seconds.text)
        break