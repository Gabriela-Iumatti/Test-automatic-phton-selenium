from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/gabri/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing_Upd.zip/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()