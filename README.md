# brimstone

This project is part of my portfolio. All code is documented in 
their respective modules and packages.

Author: Ramsharan Kanwar (ryonistic)
## **This code was written with Django 4.0.4.**

## Showcase
![showcase/home.png]() 
Setting up brimstone to work is very easy. You need to
make install dependencies from requirements.txt, alter some code 
in settings.py. Some of these changes are covered below.

## Configuring brimstone (settings.py)

To configure brimstone to work, you will need a postgresql database named brimstone with
user 'brimstone_admin' and password set according to the settings.py file. You may use sqlite 
if you want to, but you may then set the DATABASES settings to the following:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
You'll also need to setup your environment, because the project expects environment
variables to show a secret key. Since the project is left in DEBUG mode, you may want to set up your own
secret key in the .env file.
Other dependencies are listed in the Pipfile as well as the requirements.txt

## Get involved!

I am happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](https://github.com/ryonistic/brimstone/issues).

Main [git repository](https://github.com/ryonistic/brimstone):

* `git clone https://github.com/ryonistic/brimstone.git`

## Licensing

This project is MIT-licensed.
