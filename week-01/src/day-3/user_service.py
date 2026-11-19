from typing import Optional

User = dict

def create_user(
    users: list[User],
    user_id: int,
    name: str,
    email: str,
    age: int = 18
) -> User:
    """
    Creates a new user and adds it to the users collection.
    """
    
    new_user = {
        "id": user_id,
        "name": name,
        "email": email,
        "age": age,
        "active": True
    }
    
    users.append(new_user)
    
    return new_user


def get_user_by_id(
    users: list[User],
    user_id: int
) -> Optional[User]:
    """
    Returns a user by ID or None if it doesn't exist.
    """
    for user in users:
        if user["id"] == user_id:
            return user
    
    return None

def get_active_users(users: list[User]) -> list[User]:
    """
    Return only active users.
    """
    return [user for user in users if user["active"]]

def deactive_user(
    users: list[User],
    user_id: int
) -> bool:
    """
    Deactivates a user and returns whether it was successful.
    """
    user = get_user_by_id(users, user_id)
    if user is None:
        return False
    
    user["active"] = False
    
    return True



