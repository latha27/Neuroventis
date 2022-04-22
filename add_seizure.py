# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:20:48 2022

@author: Latha
"""
#importing selenium webdrivers
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import configparser

#Read config file
config = configparser.ConfigParser()
config.read("conf.ini")
username = config['Default']['username']
password = config["Default"]['password']

driverPath = r"C:\Users\Jay\Desktop\Latha Python\venv\Lib\site-packages\chromedriver_win32\chromedriver.exe"
homeUrl = "https://dq09byyrr73nc.cloudfront.net/Home"

#Loading web page and navigate to the browser
driver=webdriver.Chrome(executable_path=driverPath)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(homeUrl)

#Loading login page
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[4]/div").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div").click()

#Providing username and password
wait=WebDriverWait(driver,10)
email_id=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/input")))      
email_id.send_keys(username)
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/input").send_keys(password)
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[3]").click()

#Adding Seizure
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div[2]/div[5]/div/div").click()
Type= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/div/div[5]/div[2]/div"))).click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[4]/div/div/div/div[2]/div").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/div/div[6]/div[2]/div/div/div[2]/div[2]/div").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div/div[3]/div/div/div").click()


