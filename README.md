# Django Portfolio Website

A professional portfolio website built with Django for ITS 305.

## Setup Instructions (PyCharm Community Edition)

### 1. Open the Project
- Open PyCharm → File → Open → select the `portfolio_project` folder

### 2. Create a Virtual Environment
- Go to: File → Settings → Project → Python Interpreter
- Click the gear icon → Add Interpreter → Add Local Interpreter
- Select: Virtualenv Environment → New → click OK

### 3. Install Dependencies
Open the Terminal (bottom of PyCharm) and run:
```
pip install -r requirements.txt
```
> Note: If `mysqlclient` fails, you can use SQLite (already configured as default).
> Just remove/comment out the MySQL lines in requirements.txt for local development.

### 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
This creates the database tables AND loads sample data automatically.

### 5. Create a Superuser (for Admin Panel)
```
python manage.py createsuperuser
```
Follow the prompts to set a username and password.

### 6. Run the Development Server
```
python manage.py runserver
```
Open your browser: http://127.0.0.1:8000

### 7. Customize Your Portfolio
- Go to the admin panel: http://127.0.0.1:8000/admin
- Log in with your superuser credentials
- Edit **Profile** with your real name, bio, photo, and social links
- Add your real **Skills**, **Projects**, and **Education**

---

## Project Structure
```
portfolio_project/
├── manage.py
├── requirements.txt
├── db.sqlite3              ← created after migrate
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/
    ├── models.py           ← Profile, Skill, Project, Education, ContactMessage
    ├── views.py            ← All page views
    ├── urls.py             ← URL routing
    ├── forms.py            ← ContactForm
    ├── admin.py            ← Admin panel config
    ├── migrations/
    ├── templates/portfolio/
    │   ├── base.html
    │   ├── home.html
    │   ├── about.html
    │   ├── skills.html
    │   ├── projects.html
    │   ├── education.html
    │   └── contact.html
    └── static/portfolio/
        ├── css/style.css
        └── js/main.js
```

## Pages
| URL | Page |
|-----|------|
| `/` | Home |
| `/about/` | About |
| `/skills/` | Skills |
| `/projects/` | Projects |
| `/education/` | Education |
| `/contact/` | Contact |
| `/admin/` | Admin Panel |

---

## Deploying to PythonAnywhere

1. Push your code to GitHub
2. Log in to PythonAnywhere → Open a Bash console
3. Clone your repo:
   ```
   git clone https://github.com/yourusername/your-repo.git
   ```
4. Create a virtualenv and install requirements
5. Set up a Web App in the PythonAnywhere dashboard:
   - Framework: Django
   - Python version: 3.10+
   - Source directory: path to your project
   - WSGI file: edit to point to `portfolio_project.wsgi`
6. In settings.py, set `DEBUG = False` and add your PythonAnywhere URL to `ALLOWED_HOSTS`
7. Run `python manage.py collectstatic`
8. Reload the web app

Your URL will be: `https://firstname_lastname.pythonanywhere.com`
