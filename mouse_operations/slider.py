from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')

print("location of sliders before moving")
print(min_slider.location)
print(max_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("location of sliders before moving")
print(min_slider.location)
print(max_slider.location)
