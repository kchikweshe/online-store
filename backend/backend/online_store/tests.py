from django.test import TestCase
from testing import postgresql

# Create your tests here.
from backend.online_store.models import Product, Category


class TestProductView(TestCase):
    postgresql = postgresql.Postgresql(port=7654)

    def setup(self):
        postgresql = self.postgresql
        postgresql.start()

    def test_create(self):
        category = Category.objects.create(name="Footwear")
        product = Product.objects.create(name="Shoe", description="Adiddas XL Size 7", category_id=category.id)
        self.assertEqual(product.name, "Shoe")

    def test_category_in_product(self):
        category = Category.objects.create(name="Footwear")
        product = Product.objects.create(name="Shoe", description="Adiddas XL Size 7", category_id=category.id)
        self.assertEqual(product.category.name, "Footwear")

    def tearDown(self):
        self.postgresql.stop()
