Wikicamp
--------

How to do a Wiki on Django. This is a pic of how it comes out :)

.. image:: https://github.com/palladius/django-wikicamp/raw/master/doc/django-rickywiki.png
   :height: 100px
   :scale: 50 %
   :alt: This is a snapshot of Riccardo great wiki
   :align: right

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

Credits
-------

Copied and perfect from this nice Indian chap::

  http://showmedo.com/videotutorials/video?name=1100000&fromSeriesID=110

