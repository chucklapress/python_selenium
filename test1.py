from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')
elem.send_keys('Santa Claus Conquers the Martians' + Keys.RETURN)

browser.quit()
