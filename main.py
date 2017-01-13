import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://google.com')
assert 'Google' in browser.title

search = browser.find_element_by_name('q')
search.send_keys('smokingpipes.com Alex Florov Sandblasted Ryukin')
search.send_keys(Keys.RETURN)
time.sleep(5)

browser.quit()
