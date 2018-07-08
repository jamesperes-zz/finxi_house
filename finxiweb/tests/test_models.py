
from django.test import TestCase

from finxiweb.models import Seller, House, Customer, BasicUserMod 

class SellerTest(TestCase):
    """
    Test Seller Models

    """

    def setUp(self):
        self.basic_user = BasicUserMod.objects.create(
            email="test@test.com",
            password="abcd123456",
            username="usernameTest",
            first_name="TestName",
            last_name="TestLastName",
            phone="123456789"
            )
        self.seller = Seller.objects.create(user=self.basic_user)

    def test_create(self):
        self.assertTrue(BasicUserMod.objects.exists())

    def test_seller_exists(self):
        self.assertTrue(Seller.objects.exists())

    def test_is_instance_of_BasicUserMod(self):
        self.assertIsInstance(self.basic_user, BasicUserMod)


class HouseTest(TestCase):

    def setUp(self):
        self.basic_user = BasicUserMod.objects.create(
            email="test@test.com",
            password="abcd123456",
            username="usernameTest",
            first_name="TestName",
            last_name="TestLastName",
            phone="123456789"
            )
        self.seller = Seller.objects.create(user=self.basic_user)
        self.house = House.objects.create(
            seller=self.seller,
            title="Test Title",
            about="Test Text",
            street="Rua candido benicio 1050",
            city="Rio de Janeiro",
            district="Campinho",
            rent="500",
            )

    def test_seller(self):
        self.assertEqual(self.seller.user.first_name, "TestName")

    def test_house_exists(self):
        self.assertEqual(self.house.title, "Test Title")

    def test_house_seller(self):
        self.assertEqual(self.house.seller, self.seller)

    def test_house_geocoder(self):
        lat= str(self.house.lat)
        self.assertEqual(lat, "-22.8913874")