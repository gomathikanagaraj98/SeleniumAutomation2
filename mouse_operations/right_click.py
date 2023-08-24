from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

driver.implicitly_wait(5)
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(button).perform()