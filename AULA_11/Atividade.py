from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = Firefox()

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME, "q")
input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)

result_search =  browser.find_element(By.TAG_NAME, 'Instituto Joga Junto')