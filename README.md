![ci status](https://github.com/michaelbukachi/django-vuejs-tutorial/actions/workflows/ci.yml/badge.svg)

# django-vuejs-tutorial
This tutorial integrates Vue.js and django into one application, with Vue.js handling frontend logic and django managing backend reponses.

## Installation
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Run `npm install`
4. Run `./node_modules/.bin/webpack`
3. Run `python manage.py runserver`

For a detailed tutorial, checkout this [wiki](https://github.com/michaelbukachi/django-vuejs-tutorial/wiki/Django-Vue.js-Integration-Tutorial).

## No Webpack setup
Sometimes you might not need a whole frontend application. Maybe you just Vue.js to improve functionality on your existing app
To checkout the no webpack example
### Steps:
1. Clone the repo with `git clone --single-branch --branch no_webpack https://github.com/michaelbukachi/django-vuejs-tutorial.git` (You can also clone the repo normal way and checkout the **no_webpack** branch)
2. Run `pip install -r requirements.txt`
3. Run `python manage.py runserver`

If you are done with the tutorial and you feel like you need to know more about Django and VueJs, then check out [this](https://courses.djangowaves.com/?wpam_id=4) comprehensive course. It includes web sockets, celery, authentication and a lot more!
