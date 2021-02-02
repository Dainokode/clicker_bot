import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


chrome_driver_path = "C:\\Users\\amton\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element_by_id("cookie")
money = driver.find_element_by_id("money")


timeout = time.time() + 60 * 5
time_after_5_seconds = time.time() + 5
while True:
    cookie.click()


    if time.time() > time_after_5_seconds:
        upgrade_items = driver.find_elements_by_css_selector("#store div")
        upgrade_id = [item.get_attribute("id") for item in upgrade_items]
        for item in upgrade_items[::-1]:
            if item.get_attribute("class") != "grayed":
                item.click()
                break

        time_after_5_seconds += 5

    if time.time() > timeout:
        cookie_seconds = driver.find_element_by_css_selector("#cps")
        print(cookie_seconds.text)
        break


