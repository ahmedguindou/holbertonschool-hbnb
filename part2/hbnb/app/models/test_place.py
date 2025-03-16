from app.models.place import Place
from app.models.user import User
from app.models.review import Review

def test_place_creation():
    # Create the owner (user)
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    
    # Create the place and assign it an owner
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)
    
    # Create a review and associate it with the place and the user
    review = Review(text="Great stay!", rating=5, place=place, user=owner)
    
    # Debugging: Check if the review is already in the place before adding
    print(f"Initial reviews count: {len(place.reviews)}")  # Should be 0 initially
    print(f"Review to be added: {review.text}")
    
    # Adding the review to the place
    place.add_review(review)
    
    # Debugging: Check the reviews after adding
    print(f"Reviews count after adding: {len(place.reviews)}")  # Should be 1
    
    # Check if the review was added to the place
    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1  # This should pass if the review is correctly added
    assert place.reviews[0].text == "Great stay!"  # Ensure the review text matches
    print("Place creation and relationship test passed!")

# Run the test
test_place_creation()
