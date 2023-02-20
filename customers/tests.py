from django.test import TestCase

# Create your tests here.
from customers.models import Customer


class ModelsTestCase(TestCase):
    def test_customer_is_created(self):
        """Test Customer model"""
        customer = Customer.objects.create_user(
            email="roychowdhurysouvik94@gmail.com",
            first_name="Souvik",
            last_name="Ghosh Roy Chowdhury",
            date_of_birth="1994-02-02",
            password="password",
        )

        self.assertEqual(str(customer), "roychowdhurysouvik94@gmail.com")
