import time
import os
import requests
from selenium import webdriver

driver_path=r'C:\Users\Dionp\Desktop\dataset creator\chromedriver.exe'

wd =webdriver.Chrome(executable_path=driver_path)
a=input("type your query: ")
b=int(input("specify no of images between 100: "))
#a='dog'
#b=2
url="https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={a}&oq={a}&gs_l=img"

wd.get(url.format(a=a))
time.sleep(2)
start=0
#wd.back()
thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
print(len(thumbnail_results))


actualURL=list()
#iterating over the the thumbnails
for img in thumbnail_results[start:len(thumbnail_results)]:

    try:
        img.click()
        time.sleep(2)
    except Exception:
        continue

    #actual images links
    actual_images = wd.find_elements_by_css_selector('img.n3VNCb')

    for img in actual_images:
        if img.get_attribute('src') and 'http' in img.get_attribute('src'):
            actualURL.append(img.get_attribute('src'))
            print(len(actualURL))
        if(len(actualURL)>=b):
            break
    else:
        continue
    break
print(actualURL)




path=os.getcwd()
path=path+'\dataset'
try:
    os.mkdir(path)
except:
    print("directory already present")

path=path+'/{d}.png'


for i in range(len(actualURL)):
    with open(path.format(d=i),'wb') as f:
        link=requests.get(actualURL[i])
        f.write(link.content)


time.sleep(2)
wd.quit()