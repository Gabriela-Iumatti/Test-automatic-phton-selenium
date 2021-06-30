from selenium import webdriver
driver= webdriver.Chrome()
drive.implicitly_wait(10)
driver.get("https://conectarecife.recife.pe.gov.br/recife-vacina/")
myDynamicElement = driver.find_element_by_id('stert-shell')
driver.close()