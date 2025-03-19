import unittest
from app import create_app

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # --- Ensure a test user exists ---
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com"
        })
        print("🔹 User Creation Response:", user_response.json if user_response.status_code == 201 else "Failed to create user")

        if user_response.status_code == 201:
            self.test_user = user_response.json
        else:
            users_response = self.client.get('/api/v1/users/')
            users = users_response.json if users_response.status_code == 200 else []
            self.test_user = users[0] if users else None
        
        if not self.test_user:
            self.skipTest("🚨 Skipping tests: No valid user available")

        # --- Ensure a test place exists ---
        place_response = self.client.post('/api/v1/places/', json={
            "name": "Test Place",
            "price": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.test_user["id"]
        })
        print("🔹 Place Creation Response:", place_response.json if place_response.status_code == 201 else "Failed to create place")

        if place_response.status_code == 201:
            self.test_place = place_response.json
        else:
            places_response = self.client.get('/api/v1/places/')
            places = places_response.json if places_response.status_code == 200 else []
            self.test_place = places[0] if places else None

    # --- PLACE ENDPOINT TESTS ---
    def test_create_place(self):
        if not self.test_user:
            self.skipTest("🚨 Skipping test: No valid user available")

        response = self.client.post('/api/v1/places/', json={
            "name": "Beach House",
            "price": 120,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.test_user.get("id")  # <-- Ensure owner_id is valid
        })
        print("✅ Place Creation Response:", response.json)
        self.assertEqual(response.status_code, 201)
    
    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/places/', json={
            "name": "",
            "price": -50,
            "latitude": "invalid",
            "longitude": "invalid",
            "owner_id": "abc"
        })
        print("❌ Invalid Place Creation Response:", response.json)
        self.assertEqual(response.status_code, 400)
    
    def test_get_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
    
    # --- AMENITY ENDPOINT TESTS ---
    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Swimming Pool"
        })
        print("✅ Amenity Creation Response:", response.json)
        self.assertEqual(response.status_code, 201)
    
    def test_create_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        print("❌ Invalid Amenity Creation Response:", response.json)
        self.assertEqual(response.status_code, 400)
    
    def test_get_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
    
    # --- REVIEW ENDPOINT TESTS ---
    def test_create_review(self):
        if not self.test_place or not self.test_user:
            self.skipTest("🚨 Skipping test: No valid place or user available")

        response = self.client.post('/api/v1/reviews/', json={
            "place_id": self.test_place.get("id"),
            "user_id": self.test_user.get("id"),
            "rating": 5,
            "comment": "Amazing place!"
        })
        print("✅ Review Creation Response:", response.json)
        self.assertEqual(response.status_code, 201)
    
    def test_create_review_invalid_data(self):
        response = self.client.post('/api/v1/reviews/', json={
            "place_id": "abc",
            "user_id": "xyz",
            "rating": 6,
            "comment": ""
        })
        print("❌ Invalid Review Creation Response:", response.json)
        self.assertEqual(response.status_code, 400)
    
    def test_get_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
