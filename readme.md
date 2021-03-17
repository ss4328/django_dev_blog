# BlogMatter
BlogMatter is a simple, blog-aware, site generator perfect for personal, project, or organization sites. Think of it like a Markdown-based CMS, without all the complexity. BlogMatter takes your Markdown Content, renders it into a HTML templates, and spits out a complete, Dynamic Blog ready to be served by Heroku, Nginx or another web server.

# Core Competencies
- Fast deployment via heroku
- Completely Free
- Custom Blog Models
- Integrated support for /portfolio
- Integrated Heroku-PostGreSQL 

## Getting Started
- Set up the repo
- Read up on the configuration
- Create a superuser for Django admin Panel 
- Set up YOUR portfolio
- Fork/Contribute your own modifications (Optional)

### 1. Set up the repo
You could also leverage a virtual environment (Highly recommended)
```bash
python3 -m venv <repo name>
source <repo name>/bin/activate
```

Set up the repo:
```bash
git clone https://github.com/ss4328/django_dev_blog.git
pip install requirements.txt 
cd django_portfolio_blog
python manage.py runserver
# => Starting development server at http://127.0.0.1:8000/
```
### 2. Configuration
All settings are managed via django_portfolio_blog/settings.py
- [Markdownify's flag settings](https://github.com/matthewwithanm/python-markdownify)
- Static File Directories (Set up in STATIC_URL variable)
- To make DB migrations, 
```bash
python manage.py migrate
```

### 3. Superuser Creation
From the root directory (where manage.py resides), run:
```bash
python manage.py createsuperuser 
```
Expected Flow: 
```bash
Enter your desired username and press enter.
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

### 4. Set up your portfolio
You could now set up your own portfolio by setting up a portfolio.html in templates and setting up portfolio.styling.css in static/css. The respective url endpoint is already set up and your online resume is live!

## Demo

## Hosting
I think the easiest option to go along is to host on Heroku. Why?
- We've already set up the Procfile in the project with auto migration build support. 
- It's as easy as:
```bash
brew install heroku/brew/heroku
heroku login
=> heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
=> heroku: Waiting for login...
=> Logging in... done
=> Logged in as me@example.com
heroku create
git push heroku master
heroku open
```
- Production logs are easily viewable
```bash
heroku logs --tail
```
- Migrations are easy on the server
```bash
heroku python manage.py makemigrations
heroku python manage.py migrate
```

Optionally now you could do some simple DNS Setup if you've a custom domain.


### Follow up & Important links
1. https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
2. https://devcenter.heroku.com/articles/django-app-configuration


