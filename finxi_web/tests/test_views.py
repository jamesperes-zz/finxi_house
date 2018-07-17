from django.test import TestCase, Client
from django.shortcuts import resolve_url as r
from django.urls import reverse
from finxi_web.models import BasicUserMod, Customer, Seller


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("home")

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "finxi_web/home.html")


class CreateCustomerTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("create_customer")

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/create_customer.html")

    def test_form_error(self):
        data = {"first_name": "", "email": ""}
        response = self.client.post(self.url, data)
        self.assertFormError(response, "form", "email", "This field is required.")


class SellerTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("create_seller")
        self.login_url = reverse("login")

        self.basic_user = BasicUserMod.objects.create(
            email="test@test.com",
            password="abcd123456",
            username="usernameTest",
            first_name="TestName",
            last_name="TestLastName",
            phone="123456789",
        )
        self.seller = Seller.objects.create(user=self.basic_user)

    def test_view_redirect_not_logged(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)

