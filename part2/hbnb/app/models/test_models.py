import unittest
from app.models.amenity import Amenity
from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.review import Review
from app.models.user import User

class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(user.email, "alice.smith@example.com")

class TestPlace(unittest.TestCase):
    def test_create_place(self):
        # Create a user instance first
        user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        # Provide values for description, latitude, and longitude
        place = Place(title="Beach House", owner=user, price=100, description="A nice place", latitude=34.0522, longitude=-118.2437)
        self.assertEqual(place.title, "Beach House")
        self.assertEqual(place.owner.first_name, "Alice")
        self.assertEqual(place.price, 100)
        self.assertEqual(place.description, "A nice place")
        self.assertEqual(place.latitude, 34.0522)
        self.assertEqual(place.longitude, -118.2437)

class TestReview(unittest.TestCase):
    def test_create_review(self):
        user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        # Provide values for description, latitude, and longitude
        place = Place(title="Beach House", owner=user, price=100, description="A nice place", latitude=34.0522, longitude=-118.2437)
        review = Review(text="Great place!", rating=5, place=place, user=user)
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)

if __name__ == "__main__":
    unittest.main()
