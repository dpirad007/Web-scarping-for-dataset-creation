#https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

import time
from selenium import webdriver

driver_path=r'C:\Users\Dionp\Desktop\dataset creator\chromedriver.exe'

wd =webdriver.Chrome(executable_path=driver_path)
a=input("type your query: ")
url="https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={a}&oq={a}&gs_l=img"

wd.get(url.format(a=a))
time.sleep(5)
start=0
#wd.back()
thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
#print(len(thumbnail_results))
for img in thumbnail_results[start:len(thumbnail_results)]:
    try:
        img.click()
        
    except Exception:
        continue
time.sleep(10)
wd.quit()