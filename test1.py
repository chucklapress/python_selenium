from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')
elem.send_keys('smokingpipes.com Alex Florov Sandblasted Ryukin' + Keys.RETURN)

browser.quit()
