from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = max(1, min(rating, 5))
        self.place = place  # The place being reviewed
        self.user = user  # The user who wrote the review
        # Add the review to the place's list of reviews
        if place:
            place.add_review(self)
