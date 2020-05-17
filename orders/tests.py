from django.db.models import Max
from django.test import Client, TestCase
from .models import User


# Create your tests here.
class OrdersTestCase(TestCase):

    def setUp(self):
        pass

    def acessAllPages(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        response = c.get("/signin/")
        self.assertEqual(response.status_code, 404)
        response = c.get("/signup/")
        self.assertEqual(response.status_code, 200)
        response = c.get("/contact/")
        self.assertEqual(response.status_code, 200)
        response = c.get("/about/")
        self.assertEqual(response.status_code, 200)

    def userCreation(self):
        c = Client()
        response = c.post('/signin/',
                          {'userName': 'john', 'firstName': 'john', 'lastName': 'Victor', 'email': 'john@gmail',
                           'password': '12345678'})
        self.assertEqual(response.status_code, 200)

    def userLoginAttempt(self):
        c = Client()
        response = c.post('/login/',
                          {'userName': 'john', 'password': '12345678'})
        self.assertEqual(response.status_code, 200)


