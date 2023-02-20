from django.test import TestCase

# Create your tests here.
from products.models import Category, Product


class ModelsTestCase(TestCase):
    def test_category_is_created(self):
        """Test Category model"""
        category = Category.objects.create(name="phone")
        self.assertEqual(str(category.name), "phone")

    def test_product_is_created(self):
        """Test Product model"""
        product = Product.objects.create(
            name="samsung phone",
            category=Category.objects.create(name="phone"),
            description="mobile phone",
            stock=2,
            sold=0,
            price=50,
        )
        self.assertEqual(str(product.name), "samsung phone")

    def test_product_is_created_with_empty_stock(self):
        """Test Empty Product creation"""
        product = Product.objects.create(
            name="nokia phone",
            category=Category.objects.create(name="phone"),
            description="mobile phone",
            stock=0,
            sold=0,
            price=50,
        )
        self.assertFalse(product.available)
