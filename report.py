from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(executable_path="C:\\Users\\Jason PBE\\projects\\selenium_script\\chromedriver.exe")
browser.get("https://pbergo.az1.qualtrics.com/login?path=%2FControlPanel%2F&product=ControlPanel")

UserName = browser.find_element_by_id("UserName")
UserName.send_keys("jason@pbergo.com")

Password = browser.find_element_by_id("UserPassword")
Password.send_keys("apEeLh3D3EpExZC" + Keys.RETURN)

sleep(3)

assert "GitHub 2018" in browser.find_element_by_class_name("folders-list")