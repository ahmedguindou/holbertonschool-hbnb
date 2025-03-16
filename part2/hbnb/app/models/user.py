import re
from .base_model import BaseModel
from .place import Place  

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name[:50]
        self.last_name = last_name[:50]
        self.email = email if self.validate_email(email) else None
        self.is_admin = is_admin
        self.places = []  # List to store places owned by this user

    def validate_email(self, email):
        """Validates email format."""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None

    def add_place(self, place):
        """Add a place to the user's list of owned places."""
        if not isinstance(place, Place):
            raise ValueError("Only Place instances can be added.")
        self.places.append(place)
