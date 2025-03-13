from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def validate(self):
        """Validate the attributes before saving"""
        if len(self.first_name) > 50:
            raise ValueError("First name cannot be more than 50 characters.")
        if len(self.last_name) > 50:
            raise ValueError("Last name cannot be more than 50 characters.")
        if not isinstance(self.email, str) or "@" not in self.email:
            raise ValueError("Invalid email format.")
