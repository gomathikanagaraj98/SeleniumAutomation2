from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

rome_element=driver.find_element(By.ID,"box6")
italy_element=driver.find_element(By.ID,"box106")
act=ActionChains(driver)
act.drag_and_drop(rome_element,italy_element).perform()

washgtn=driver.find_element(By.ID,"box3")
unitedstates=driver.find_element(By.ID,"box103")
act=ActionChains(driver)
act.drag_and_drop(washgtn,unitedstates).perform()
