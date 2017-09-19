=====
Django Todo List
=====

Todo is a simple Django app to conduct Web-based todo list. 
You can add your new list to do and check for some which had beed finished, 
or recover the finished to un-finished status.
or you can delete items

Detailed documentation is in the "docs" directory.

Installation
------------

you can install via `pip`

    pip install colinws-todo
     
or you can `git clone` this repository and use `setup.py`

    git clone https://github.com/opscolin/Django-todo.git  
    
    cd Django-todo  
    
    python setup.py install  

Quick start
-----------

1. Add "todo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'todo',
    ]

2. Include the todo URLconf in your project urls.py like this::

    url(r'^todo/', include('todo.urls')),

3. Run below command to create todo models migrations.:


    python manage.py makemigrations todo

    
4. Run below command to create todo real models.:


    python manage.py migrate todo

    
5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a todo  (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/todo/ to participate in the todo list.
