import time
from selenium import webdriver

driver_path=r'C:\Users\Dionp\Desktop\dataset creator\chromedriver.exe'

wd =webdriver.Chrome(executable_path=driver_path)
a=input("type your query: ")
b=int(input("specify no of images between 100: "))
#a='dog'
#b=5
url="https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={a}&oq={a}&gs_l=img"

wd.get(url.format(a=a))
time.sleep(2)
start=0
#wd.back()
thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
print(len(thumbnail_results))


actualURL=set()
#iterating over the the thumbnails
for img in thumbnail_results[start:len(thumbnail_results)]:

    try:
        img.click()
        time.sleep(1)
    except Exception:
        continue

    #actual images links
    actual_images = wd.find_elements_by_css_selector('img.n3VNCb')

    for img in actual_images:
        if img.get_attribute('src') and 'http' in img.get_attribute('src'):
            actualURL.add(img.get_attribute('src'))
            print(len(actualURL))
        if(len(actualURL)>=b):
            break
    else:
        continue
    break
     

print(actualURL)

#now the code gives valid http links of data


time.sleep(2)
wd.quit()