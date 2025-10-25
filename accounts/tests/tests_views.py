from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignUpViewTests(TestCase):
    def test_signup_page_renders_correct_template(self):
        """ Is the SignUp template rendered correctly? """
        response = self.client.get('/accounts/sign_up/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_up.html')

    def test_can_create_user_via_signup_form(self):
        """ Is it possible to create user via SignUp form? """
        response = self.client.post(reverse('sign_up'), {
            'username': 'konrad',
            'email': 'konrad@example.com',
            'password1': 'superpassword123',
            'password2': 'superpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='konrad').exists())

    def test_invalid_signup_shows_errors(self):
        """ Are incorrect data show errors? """
        response = self.client.post(reverse('sign_up'), {
            'username': '',
            'email': '123@',
            'password1': 'abc',
            'password2': 'xyz',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too short", status_code=200)


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='konrad', password='StrongPassword123')

    def test_login_page_renders_correctly(self):
        """ Is the login page rendered correctly? """
        response = self.client.get('/accounts/sign_in/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_in.html')

    def test_can_login_user(self):
        """ Is the user correctly logged in? """
        response = self.client.post(reverse('sign_in'), {
            'username': 'konrad',
            'password': 'StrongPassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_wrong_password_shows_error(self):
        """ If user provide incorrect password, he can see error? """
        response = self.client.post(reverse('sign_in'), {
            'username': 'konrad',
            'password': 'WrongPassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")
