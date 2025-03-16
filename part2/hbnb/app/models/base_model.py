import uuid
from datetime import datetime

class BaseModel:
    instances = {}  # A class-level dictionary to store instances by their UUIDs.

    def __init__(self):
        self.id = str(uuid.uuid4())  # Store the UUID as a string.
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Register the instance in the in-memory repository
        BaseModel.instances[self.id] = self

    def save(self):
        """Update the updated_at timestamp whenever the object is modified."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Warning: Attribute '{key}' does not exist.")
        self.save()

    def to_dict(self):
        """Convert the object to a dictionary representation."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """Create an instance from a dictionary representation."""
        instance = cls()
        for key, value in data.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def retrieve(cls, instance_id):
        """Retrieve an instance by its ID."""
        return cls.instances.get(instance_id, None)

    @classmethod
    def all(cls):
        """Return all instances."""
        return list(cls.instances.values())
