from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def find_the_end(browser: webdriver):
    page_loaded = browser.execute_script("return document.readyState")
    if page_loaded == "complete":
        body = browser.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)


driver = webdriver.Chrome(executable_path='C:\\Users\\koliveiraba\\Downloads\\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/infinite_scroll")
while(True):
    find_the_end(driver)
