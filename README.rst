Wikicamp
--------

How to do a Wiki on Django.

Copied / extrapolated from here::

  http://showmedo.com/videotutorials/video?name=1100000&fromSeriesID=110

Install
-------

Requires module::

  markdown
  docutils

Develop
-------

I've done this::

   django-admin.py startproject wikicamp
   cd wikicamp/
   python manage.py startapp wiki
   # Edit models and settings for DB and app
   python manage.py syncdb

