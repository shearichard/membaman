Introduction
------------
Membaman is a membership management system intended for Youth and Sports Groups.

Its intended scope includes :

 * Membership registration within Organisations and sub-organisations
 * Invoicing and tracking of payments for regular payments
 * Production of PDF's to support the invoicing process
 * Production of CSV downloads to allow data transfer out of Membaman to other systems
 * Ability to email members and members caregivers with both regular and ad-hoc emails

Membaman is implemented in Django 1.7 and uses a Posgres database as a data repository. To date it has only been tested in Python 2.7.x . 

----
Absolute Beginners
------
If you're new to Python and / or Django here are some things which you will need to consider to run membaman. This is not intended as a step-by-step guide but rather an outline of areas you will need to deal with. I'm happy to provide more detailed information for anyone who wishes to run their own installation but who is not well versed in Python / Django.

 0. I have only ever run membaman on Linux and so while you're welcome to try Windows/Mac you'll be entering new territory. In theory it should all work but there are small pieces of Python which work in one way for Windows and another way for Unixy type envs. If you are a Windows person one option is to run Ubuntu within [VirtualBox](https://www.virtualbox.org/), there are of course plenty of other options.
 1. I can't remember whether the excellent [pip](https://en.wikipedia.org/wiki/Pip_%28package_manager%29) is installed by default within modern Pythons but if not you're going to want to install it and there are directions [here] (https://pip.pypa.io/en/stable/quickstart.html) for doing that.
 2. Using the Python [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) facility makes life so much easier as you can create your own virtualenv to run membaman within and then be confident that nothing will mess with your environment and vica versa. While we're on virtualenv the [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html) is an excellent adjunct to it but certainly optional. 
 3. Create a virtualenv with a name of your choosing and ensure it is active while doing the next step (and whenever you make use of membaman).
 4. Now (with your virtualenv activated) make use of pip and the [requirements.txt](https://github.com/shearichard/membaman/blob/master/requirements.txt) within this repository to [automatically install](https://pip.pypa.io/en/stable/user_guide.html#requirements-files) everything you need to make membaman work.
 4. Now - you're almost there ! You need a Postgres instance accessible from where membaman will be run. I'm going to leave how you get that for another iteration of edits. Of course being Django there's no need for it to be Postgres but that's what I've used to date. For small local installations [SQLite](https://www.sqlite.org/) might be an interesting option but would require testing.
 5. Lastly you need to create your own version of [local.py] (https://github.com/shearichard/membaman/blob/master/membaman/membaman/settings/local.py) with settings that are relevant to your own environment .

**TODO**: Review how initial data needs to be setup within membaman.  
 

----


Use of bookkeeper 
--------
The version of bookkeeper used as at Dec 2014 is taken from https://github.com/shearichard/bookkeeper.git as there are some Django 1.7 specific fixes which I've made and which haven't yet been applied to the main repos at SwingTix/bookkeeper .

Use of django-feedback
--------
The version of django-feedback used as at Feb 2015 is taken from https://github.com/shearichard/django-feedback.git .

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
0.2.0
