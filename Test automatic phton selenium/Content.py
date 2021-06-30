from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/gabri/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing_Upd.zip/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
content = driver.find_element_by_class_name('content')
print("My class element is:")
print(content)
driver.close()
