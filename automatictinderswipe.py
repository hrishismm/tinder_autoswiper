#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:58:21 2020

@author: hrishi
"""
#Imports Webdriver
from selenium import webdriver
import time
#Imports keys which will be used for typing inside textboxes
from selenium.webdriver.common.keys import Keys
#To get the userpassword without displaying on the command line
from getpass import getpass

#Creating the Webprofile
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") #mime Value
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/Desktop/image")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("geo.prompt.testing", True)
fp.set_preference("geo.prompt.testing.allow", True)

#Get  Email id and password
emailid=str(input("Enter your email id"))
pswd = getpass('Password:')
choice=int(input("Enter your choice:\n1)For right swipe\n2)For left swipe(which ik you won't)"))

#Creating object of webdriver by specifying the gecko driver link in your machine
driver=webdriver.Firefox(executable_path="/home/hrishi/Desktop/geckodriver-v0.27.0-linux64/geckodriver",firefox_profile=fp)

#Getting the link from where we start the automation
driver.get("https://tinder.com/?lang=en")
driver.maximize_window()
time.sleep(10)

#Clicking on the login button
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button").click()
time.sleep(10)

#Creating handles tocheck the number of windows opened
handles=driver.window_handles

#print(handles)

#Switch to Google login window
driver.switch_to_window(handles[1])       
time.sleep(5)

#Entering email and then clicking the button
driver.find_element_by_id("identifierId").send_keys(emailid)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
time.sleep(5)

#Entering password and then clicking the button
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(pswd)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
time.sleep(10)

#Switch to the previous windpw
driver.switch_to_window(handles[0]) 
#Giving permissions
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
time.sleep(5)

def right_swipe():
    for _ in range(100):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button").click()
            time.sleep(0.5)
        except:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]").click()
            print("Limit exceeded please try tommorow")
            
def left_swipe():
    for _ in range(100):
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button").click()
        time.sleep(0.5)

if choice==1:
    right_swipe()
elif choice==2:
    left_swipe()
else:
    print("Invalid choice")
        