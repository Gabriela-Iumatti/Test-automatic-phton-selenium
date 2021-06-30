from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/gabri/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing_Upd.zip/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()