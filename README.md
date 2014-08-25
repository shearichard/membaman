Introduction
------------
This is membaman ! Beyond that I could not say.

Use of Selenium
--------
To facilitate the use of Selenium I installed Xvfb
```
sudo apt-get install xvfb
```
Then I installed Firefox
```
sudo apt-get install firefox
```
Then I installed PyVirtualDisplay
```
sudo pip install pyvirtualdisplay
```

After that, without explicitly starting xvfb, I was able to run a test script, courtesy of http://coreygoldberg.blogspot.co.nz/2011/06/python-headless-selenium-webdriver.html, such as 

```
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.
browser = webdriver.Firefox()
browser.get('http://www.google.com')
print browser.title
browser.quit()

display.stop()
```

Version
--------
0.0.1
