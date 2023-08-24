from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,2000)","")
value=driver.execute_script("return window.PageYOffset;")
print("Number of pixels moved:",value)

flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.PageYOffset;")
print("Number of pixels moved:",value)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.PageYOffset;")
print("Number of pixels moved:",value)
