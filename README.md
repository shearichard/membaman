Introduction
------------
This is membaman ! Beyond that I could not say.

Use of bookkeeper 
--------
The version of bookkeeper used as at Dec 2014 is taken from https://github.com/shearichard/bookkeeper.git as there are some Django 1.7 specific fixes which I've made and which haven't yet been applied to the main repos at SwingTix/bookkeeper .

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

Environment Variables
-------------------
Using `autoenv` to set a ENV VAR of SECRET_KEY when we cd into membaman. Longer term need a better solution.

Use printenv to confirm the SECRET_KEY is set correctly.

Running Instructions
-------------------
Note to self: using `dj17` as virtualenv 
```
python manage.py runserver  --settings=membaman.settings.local 0.0.0.0:8000
```

Version
--------
0.0.1
