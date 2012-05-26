Wikicamp
--------

This is my first application made with Django. It's a *Wiki*. This is a pic of how the (minimalistic) website looks like:

.. image:: https://github.com/palladius/django-wikicamp/raw/master/doc/django-rickywiki.png
   :width:  219 px
   :height: 101 px
   :scale: 50 %
   :alt: This is a snapshot of Riccardo great wiki
   :align: right

I was utterly inspired (read: copied) by an Indian guy who made a screencast on how to create a wiki in Django in just 20'. So I did it. Pity it's so outdated I had to make some changes. See Credits for more info.

Install
-------

Requires module::

  markdown (for wiki markdown)
  docutils (for admin docs)

Todo
----

* Use CSS (!!)
* Refactor templates with generic stub (I dont know *yield* equivalent in python!)
* Put links into the markdown (have [[riccardo]] be correctly linked to the relevant page).

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

