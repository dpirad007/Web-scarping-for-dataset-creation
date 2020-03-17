
# Web-scarping-for-dataset-creation
This is an ongoing project to create custom datasets using image scraping via google images

## Getting Done With The Basics 
- step 1]  Download and install chrome.
- step 2]  Identify your chrome version-(typically found in the about google chrome -eg)Version 80.0.3987.132)
this was my version ,yours may differ.
- step 3] Download the corresponding ChromeDriver [ChromeDriver-Download](https://chromedriver.chromium.org/downloads)

## Getting The Required Packages
- for this project we will use the Selenium Package

```cmd
pip install selenium
```

Your All Set Up!
---

# Understanding How To Make It Run

Initally you will have to specify your driver path - (In the code published, my driver path is specified)
```javascript
...
driver_path=r'C:\Users\Dionp\Desktop\dataset creator\chromedriver.exe--(delete previous path and specify your own)'
wd =webdriver.Chrome(executable_path=driver_path)
...
```

Once you've finished setting up your driver path, You can finally run the program!

You will have the following output in the terminal:
```text
type your query: Enter the name of the images that you need for your dataset-eg dog
specify no of images between 100: Enter the integer value of how many images that you need
```
**Note**-Currently this project only supports first 100 images, it will be updated soon!
Once you hit enter you should be able to see the chrome browser scrolling through your specified query

By default it will store the images in the dataset folder in the current working directory

**Note**-Currently this project on supports creation of a single folder to store images in, it will be updated soon!