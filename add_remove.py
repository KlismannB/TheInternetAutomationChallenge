from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\\Users\\koliveiraba\\Downloads\\chromedriver.exe')
browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

add = browser.find_element_by_css_selector("button").click()
element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "added-manually")))
sleep(2)
remove = browser.find_element_by_class_name("added-manually").click()

browser.quit()
