import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Just to test the login
print("Test Case - Login")
 
# need to have a chrome driver in a folder; without this driver Selenium won't be able to control/run the chrome browser
driver = webdriver.Chrome('C:/Windows/chromedriver') #I have place my chromedriver in c:/Windows
driver.implicitly_wait(30)
driver.maximize_window()
 
driver.get("https://demo.getsaleor.com/en/account/login/") # Saleor has a demo site, just use it

# get the email textbox
email_field = driver.find_element_by_name("username")
# input email
email_field.send_keys("admin@example.com")

# get the password textbox
password_field = driver.find_element_by_name("password")
# input password
password_field.send_keys("admin")

# click login
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div/div/button").click()
driver.implicitly_wait(200)

# check if logged in via visible element (this may not be the best way; well, at least it works for now)
if driver.find_element_by_xpath("/html/body/header/div[1]/div/div/div[2]/ul/li[4]/a"):
    print("Login is fine")
    
else:
    print ("Something is not right")

time.sleep(10)

print("Test Case - End")
# closes selected browser
driver.close()

 
 
