#https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

import time
from selenium import webdriver

driver_path=r'C:\Users\Dionp\Desktop\dataset creator\chromedriver.exe'

wd =webdriver.Chrome(executable_path=driver_path)

wd.get('https://google.com')

search_box=wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')
time.sleep(10)
wd.quit()