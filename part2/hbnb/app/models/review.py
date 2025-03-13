from .base_model import BaseModel
from .place import Place
from .user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def validate(self):
        """Ensure rating is within the acceptable range"""
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
