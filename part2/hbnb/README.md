# HbnB Project - Implementation of Business Logic and API Endpoints 🚀

- This phase of the HBnB project focuses on implementing the application's core structure, including the Presentation and Business Logic layers using Python and Flask.
- It involves developing key classes (User, Place, Review, Amenity) and setting up RESTful API endpoints with flask-restx to manage CRUD operations. While authentication and access control will be handled later, the emphasis is on creating a scalable, modular, and well-structured foundation for future enhancements.

## Installation


## Project Structure 📂

```plaintext
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### Explanation 📝

- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the API endpoints, organized by version (`v1/`).
- The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
- The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQLAlchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` will contain a brief overview of the project.

## Business Logic Layer 🧠

The Business Logic layer is responsible for implementing the core functionality of the application. It includes the following key entities:

- **User**: Represents a user of the application.
- **Place**: Represents a place listed by a user.
- **Review**: Represents a review of a place by a user.
- **Amenity**: Represents an amenity available at a place.

### Entities and Responsibilities 📋

#### User 👤
- **Attributes**: `id`, `first_name`, `last_name`, `email`
- **Methods**:
    - `create_user(user_data)`: Creates a new user.
    - `get_user(user_id)`: Retrieves a user by ID.
    - `update_user(user_id, user_data)`: Updates user attributes.
    - `get_all_users()`: Retrieves all users.

#### Place 🏠
- **Attributes**: `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner`, `amenities`
- **Methods**:
    - `create_place(title, description, price, latitude, longitude, owner_id, amenities)`: Creates a new place.
    - `get_place(place_id)`: Retrieves a place by its ID.
    - `update_place(place_id, place_data)`: Updates place attributes.
    - `get_all_places()`: Retrieves all places.

#### Review 📝
- **Attributes**: `id`, `text`, `user_id`, `place_id`, `rating`
- **Methods**:
    - `create_review(text, user_id, place_id, rating)`: Creates a new review.
    - `get_review(review_id)`: Retrieves a review by its ID.
    - `update_review(review_id, review_update)`: Updates review attributes.
    - `delete_review(review_id)`: Deletes a review.
    - `get_reviews_by_place(place_id)`: Retrieves all reviews for a specific place.

#### Amenity 🛠️
- **Attributes**: `id`, `name`
- **Methods**:
    - `create_amenity(amenity_data)`: Creates a new amenity.
    - `get_amenity(amenity_id)`: Retrieves an amenity by its ID.
    - `update_amenity(amenity_id, amenity_data)`: Updates amenity attributes.
    - `get_all_amenities()`: Retrieves all amenities.

### Examples 💡

#### Creating a User
```python
from app.services.facade import HBnBFacade
facade = HBnBFacade()
user = facade.create_user({"first_name": "John", "last_name": "Doe", "email": "john@example.com"})
print(user.id)
```

#### Creating a Place
```python
place = facade.create_place("Cozy Cabin", "A relaxing getaway.", 120, 45.67, -123.45, user.id, [])
print(place.id)
```

#### Creating a Review
```python
review = facade.create_review("Amazing place!", user.id, place.id, 5)
print(review.id)
```

#### Creating an Amenity
```python
amenity = facade.create_amenity({"name": "WiFi"})
print(amenity.id)
```

## Unit Tests 🧪

Unit tests validate the API endpoints for creating, retrieving, updating, and deleting users, places, amenities, and reviews. 

### Covered Test Cases:
- Creating valid users, places, reviews, and amenities.
- Handling invalid input data (e.g., negative prices, missing attributes, incorrect types).
- Retrieving existing entities and verifying data integrity.
- Ensuring endpoints return appropriate status codes.
- Testing edge cases such as empty datasets.

executed using `unittest` and include setup to ensure valid test data is created before running the cases. Errors are logged with clear messages for debugging.

