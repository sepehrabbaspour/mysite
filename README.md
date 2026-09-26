# 🌍 Django Tourism & Content Management Website

A Django-based tourism and content management website built with **Python and Django 5.2**.

The project focuses on implementing a functional Django backend on top of a pre-designed HTML frontend, including authentication, blog management, comments, search, categories, tags, pagination, protected posts, admin management, static/media files, and other Django features.

---

## ✨ Features

### 🔐 User Authentication

* User registration
* User login and logout
* Django built-in authentication system
* `AuthenticationForm` for login
* `UserCreationForm` for registration
* Protected views using `@login_required`
* Authentication status displayed dynamically in the base template
* Error messages for invalid login credentials
* Preventing authenticated users from accessing login and registration pages
* Protected logout functionality

---

### 📝 Blog System

The project includes a complete blog system with:

* Blog post management
* Individual blog post pages
* Categories
* Tags using `django-taggit`
* Author filtering
* Category filtering
* Tag filtering
* Published / unpublished posts
* Scheduled publishing using `published_date`
* View counter
* Search functionality
* Pagination
* Custom template tags

---

### 🔒 Protected Blog Posts

Blog posts can optionally be protected for authenticated users.

Each post contains a `login_required` field that can be enabled from the Django Admin.

When enabled:

* Unauthenticated users are redirected to the login page.
* Authenticated users can access the post normally.

Example:

```python
if not post.login_required or request.user.is_authenticated:
    return render(
        request,
        "blog/blog-single.html",
        context
    )
else:
    return HttpResponseRedirect(
        reverse("accounts:login")
    )
```

---

### 💬 Comment System

The project includes a custom Django-based comment system.

Comments are handled using Django `ModelForm` and require administrator approval before being displayed.

Main features:

* Comment submission form
* Name, email, subject, and message fields
* Comment approval system
* Django Admin management
* Success and error messages using Django Messages Framework

Example form:

```python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
            "name",
            "email",
            "subject",
            "message",
        ]
```

Comments are not displayed publicly until they are approved from the Django Admin.

---

### 🛠️ Django Admin

The Django Admin panel is used to manage the main content and functionality of the website.

Administrators can manage:

* Blog posts
* Authors
* Categories
* Tags
* Comments
* Publication status
* Scheduled publication dates
* Login-required posts
* Post view counts
* Search and filtering
* Rich-text blog content

Example admin configuration:

```python
list_display = (
    "title",
    "author",
    "counted_views",
    "status",
    "login_required",
    "published_date",
    "created_date",
)
```

---

### 🖼️ Static & Media Files

The project separates static assets and uploaded media.

**Static files include:**

* CSS
* JavaScript
* Images
* Fonts

**Media files include:**

* Uploaded blog images
* Images uploaded through the Django Summernote editor

Project directories:

```text
statics/
media/
```

---

## 🔎 Blog Search

The blog includes a search feature for finding posts based on their content.

Example:

```python
posts = posts.filter(content__contains=s)
```

---

## 📄 Pagination

Blog posts are paginated to improve navigation and page organization.

The project currently displays **3 posts per page**.

Example:

```python
posts = Paginator(posts, 3)
```

---

## 🏷️ Tags & Categories

The blog uses:

* Django `ManyToManyField` for categories
* `django-taggit` for tags

Users can browse posts through:

* Categories
* Tags
* Authors

---

## 🗺️ Sitemap & robots.txt

The project includes support for:

* Django sitemap generation
* `robots.txt`

These features are used to provide basic search-engine-related functionality for the website.

---

## ✍️ Django Summernote

The Django Admin uses **Django Summernote** to provide a rich-text editing interface for blog content.

This makes it possible to create formatted blog posts and manage content more conveniently through the Admin panel.

---

## 🔧 Django Debug Toolbar

**Django Debug Toolbar** is included as a development tool for inspecting and debugging Django requests and application behavior during development.

---

## 🤖 CAPTCHA

The project uses Django CAPTCHA functionality for forms that require CAPTCHA protection.

The following packages are included:

* `django-simple-captcha`
* `django-multi-captcha-admin`

---

## 🌐 Django Sites Framework

The project uses Django's **Sites Framework** for site-level configuration and functionality.

---

## 🧩 Custom Template Tags

The `blog` application contains custom template tags:

```text
blog/
└── templatetags/
```

These tags are used to provide reusable functionality inside Django templates.

---

## 🧪 Response Test Endpoints

The project also includes simple endpoints for testing:

* HTTP responses
* JSON responses

These endpoints were implemented for learning and testing Django response handling.

---

## 🧰 Technologies Used

### Backend

* 🐍 Python
* 🌐 Django 5.2.15
* 🗄️ Django ORM
* 📝 Django Forms & ModelForms
* 🔐 Django Authentication
* 🛠️ Django Admin
* 💬 Django Messages Framework
* 🧩 Django Templates

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript
* Django Template Language

### Django Packages

* `django-taggit`
* `django-summernote`
* `django-debug-toolbar`
* `django-simple-captcha`
* `django-multi-captcha-admin`
* `django-extensions`
* `django-ranged-response`
* `django-robots`

### Database

* SQLite

### Development Tools

* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
mysite/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── blog/
│   ├── migrations/
│   ├── templatetags/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── website/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── setting/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
├── statics/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 📦 Requirements

Before running the project, make sure you have:

* Python 3.x
* pip
* Git

All required Python packages are listed in `requirements.txt`.

The project dependencies include:

* `Django`
* `django-taggit`
* `django-summernote`
* `django-debug-toolbar`
* `django-simple-captcha`
* `django-multi-captcha-admin`
* `django-extensions`
* `django-ranged-response`
* `django-robots`
* `Pillow`
* `bleach`
* `webencodings`
* `asgiref`
* `sqlparse`
* `tzdata`

The `requirements.txt` file contains the installed package versions for the project.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sepehrabbaspour/mysite.git
cd mysite
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

> The virtual environment name `env` is only an example. You can use any name you prefer.

---

### 3. Install project dependencies

All required Python packages are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

This installs the Django packages and other dependencies required by the project, including CAPTCHA, Taggit, Summernote, Debug Toolbar, and other packages used by the application.

---

### 4. Apply database migrations

```bash
python manage.py migrate
```

---

### 5. Create a superuser

To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your administrator account.

---

### 6. Run the development server

```bash
python manage.py runserver
```

The website will be available at:

```text
http://127.0.0.1:8000/
```

The Django Admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

## 🗄️ Database

The project uses **SQLite** during development.

Database configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

SQLite was chosen for simplicity during development and learning.

---

## 📝 Development Notes

This project was developed as a Django learning and portfolio project.

The frontend was based on a pre-designed HTML template, while the main development work focused on implementing the Django backend and integrating the frontend with Django.

The project covers practical Django concepts including:

* Project and application structure
* URL routing
* Views
* Models
* Django ORM
* Forms and ModelForms
* Authentication
* Access control
* Django Admin
* Template inheritance
* Custom template tags
* Static and media files
* Pagination
* Search
* Categories and tags
* Comments
* Messages Framework
* Sitemap
* CAPTCHA
* Django Sites Framework
* Development and debugging tools

The project is currently intended for development and portfolio purposes and has not been deployed as a production website.

---

## 🚀 Future Improvements

Possible future improvements include:

* 🌐 Production deployment
* 🗄️ PostgreSQL database
* 🔐 Environment variable management
* 🔌 REST API
* 🔎 Improved search functionality
* 💬 Improved relationship between comments and users
* 🧪 Automated tests
* 🐳 Docker support
* 🔒 Production security configuration
* 📧 Email verification
* 🔑 Password reset functionality
* 📱 Improved frontend responsiveness

---

## 👨‍💻 Author

**Sepehr Abbaspour**

Computer Science Graduate
Python & Django Backend Developer

🔗 GitHub:
https://github.com/sepehrabbaspour

---

⭐ If you find this project useful, feel free to explore the code and give the repository a star.
