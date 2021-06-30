from selenium import webdriver;
import time
browser= webdriver.Chrome();
browser.get('http://www.seleniumhq.org');

driver = webdriver.Firefox()
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()


driver = webdriver.Chrome()
driver.get('https://selenium.dev')
time.sleep(2)

driver.close()