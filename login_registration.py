# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_link_text("My Account").click()
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("qwertyu@gmail.com")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("Qwertyuiop123456789!")
# register = driver.find_element_by_css_selector("[name='register']").click()


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_link_text("My Account").click()
# username = driver.find_element_by_id("username")
# username.send_keys("qwertyu@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Qwertyuiop123456789!")
# login = driver.find_element_by_css_selector("[name='login']").click()
# Logout = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))

