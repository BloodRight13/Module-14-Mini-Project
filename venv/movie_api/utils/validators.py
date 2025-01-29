def validate_genre_name(name):
    if not name:
        raise ValueError("Genre name cannot be empty.")
    if len(name) > 100:
        raise ValueError("Genre name cannot exceed 100 characters.")
