from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name[:50]  # Limit name length to 50 characters

    def to_dict(self):
        """Convert the Amenity object to a dictionary."""
        return {
            "id": self.id,  # Include the id if it's part of your base model
            "name": self.name
        }
