# DevTrack - Project Documentation

## 1. Overview

DevTrack is a web-based project tracking platform built with Django. It provides:

- User authentication and registration
- Project and task tracking
- Dashboard and home page for logged-in users
- Secure password validation and user management

This documentation describes the project structure, key components, and instructions for setup and testing.

---

## 2. Project Structure

```
DevTrack/
│
├─ DevTrack/ # Django project settings
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
│
├─ accounts/ # User authentication module
│ ├─ forms.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ templates/accounts/
│ │ ├─ sign_up.html
│ │ └─ sign_in.html
│ ├─ tests/tests_views.py
│ └─ models.py # Optional; using built-in User model
│
├─ static/ # CSS and static files
│ └─ styles/style.css
│
├─ templates/ # Global templates
│ └─ home.html
│
├─ manage.py
└─ README.md
```

---

## 3. Accounts Module

### 3.1 Purpose

Handles user registration, login, logout, and password validation.

### 3.2 Forms (`accounts/forms.py`)

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Required. Enter a valid email address.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1
```

### 3.3 Views (accounts/views.py)

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegistrationForm

def sign_up_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def sign_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/sign_in.html', {'form': form})

def sign_out_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign_in')
```

### 3.4 Templates
#### Sign Up (sign_up.html)
- Form fields rendered using {{ form.field_name }}
- Shows validation errors per field
- Link to login page

#### Login (sign_in.html)
- Similar structure as signup page
- Displays authentication errors

### 3.5 URLs (accounts/urls.py)

```python
from django.urls import path
from accounts import views

urlpatterns = [
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('sign_out/', views.sign_out_view, name='sign_out'),
]
```

### 3.6 Tests (accounts/tests/tests_views.py)
- Verify page renders (status_code=200)
- Verify user creation via signup form (status_code=302)
- Check password and email validation messages
- Test login with correct and incorrect credentials

#### Run tests:
```
python manage.py test accounts
```

---

### 4. Global Templates
#### Home Page (templates/home.html)
- Landing page after login
- Displays user dashboard and project/task overview

---

### 5. Static Files
- CSS and assets in static/styles/style.css
- Linked in templates using {% load static %}

---

### 6. Settings
#### Password Validators (settings.py)

```python
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
```

#### Other settings

```python
STATIC_URL = '/static/'
LOGIN_URL = '/accounts/sign_in/'
LOGIN_REDIRECT_URL = '/home/'
```

---

### 7. Getting Started
#### Install dependencies
```
pip install -r requirements.txt
```

#### Run migrations
```
python manage.py migrate
```

#### Create superuser (optional)
```
python manage.py createsuperuser
```

#### Run the development server
```
python manage.py runserver
```

#### Access the app
- Signup: http://127.0.0.1:8000/accounts/sign_up/
- Login: http://127.0.0.1:8000/accounts/sign_in/

---

### 8. Testing

Run all tests:
```
python manage.py test
```
Ensures forms, views, authentication, and validation work correctly.

---

### 9. Notes
- Uses Django’s built-in User model
- All forms are server-side validated using Django forms and password validators
- Templates are minimal and ready for CSS customization