# HW 17. Django CBV detail page
___
This is a Django-based project of social network web-site. 

### Getting started
Currently, project can be run on localhost only (http://127.0.0.1:8000/) by applying command:
```
python manage.py runserver
```

### Project structure
*...Under construction...*
```
├───config                  # project root directory
├───core                    # app "Core" directory
│   ├───migrations              # built-in folder for generated migrations files
├───users                   # app "Users" directory
│   ├───migrations              # built-in folder for generated migrations files
├───templates               # HTML-templates directory
│   ├───core                    # app "Core" related HTML-templates
│   └───users                   # app "Users" related HTML-templates


```

**CONFIG**

> *asgi.py* | *wsgi.py* : asynchronous and synchronous app-server gateway interfaces
> 
> *urls.py* : list routes URLs to views
>
> *settings.py* : list of project settings and variables

**CORE**

>*models.py* : list of models describing data structure
> 
>*views.py* : list of class methods for building up web-requests
___
