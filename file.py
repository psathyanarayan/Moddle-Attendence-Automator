#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support import expected_conditions as EC
import time



username = #"{Your moodle username}"
password = #"{Your moodle password}"

PATH = #"{chrome driver path (can use any other but do change the rest)}"
driver = webdriver.Chrome(PATH)
driver.get("{Moodle login page url}")

username_textbox = driver.find_element_by_id("username") #id of the username box here its username
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")  #id of the password box here its password
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("loginbtn")  #id of the login button box here its loginbtn
login_button.submit()
driver.get("attendence subject page url. The page where you mark attendence")
try:
    m=driver.find_element_by_link_text("Submit attendance") #get the link text if the submit button
    driver.implicitly_wait(5)
    m.click()
    driver.find_element_by_xpath("//input[@name='status']").click() #paste your xpath 
    driver.find_element_by_id("id_submitbutton").submit()
    time.sleep(20)
    driver.quit()
except:     
    driver.quit()

