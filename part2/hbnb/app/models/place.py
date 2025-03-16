from .base_model import BaseModel
from .review import Review
from .amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title[:100]
        self.description = description
        self.price = max(price, 0)
        self.latitude = min(max(latitude, -90.0), 90.0)
        self.longitude = min(max(longitude, -180.0), 180.0)
        self.owner = owner  # This will be a User instance
        self.reviews = []  # List of reviews for this place
        self.amenities = []  # List of amenities for this place

        # Add the place to the owner's places list (one-to-many)
        if owner:
            owner.add_place(self)

    def add_review(self, review):
        """Adds a review to the place, validating existence of place and user."""
        if not isinstance(review, Review):
            raise ValueError("Invalid review")
        
        # Debugging: Print the review place and the place this method is being called on
        print(f"Adding review: {review.text} to place: {self.title}")
        print(f"Review belongs to place: {review.place.title} (Expected: {self.title})")
        
        if review.place != self:
            raise ValueError("Review does not belong to this place")
        if review.user not in [self.owner]:  # Ensure that the user is valid
            raise ValueError("Invalid user for this place")
        
        # Ensure no duplicate reviews are added
        if review in self.reviews:
            print(f"Review: {review.text} is already added!")
        else:
            self.reviews.append(review)
            print(f"Review added: {review.text}")  # Debug print to check

    def add_amenity(self, amenity):
        """Adds an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise ValueError("Invalid amenity")
        self.amenities.append(amenity)

    def list_amenities(self):
        """Lists all amenities associated with the place."""
        return [amenity.to_dict() for amenity in self.amenities]

    def list_reviews(self):
        """Lists all reviews for the place."""
        return [review.text for review in self.reviews]  
