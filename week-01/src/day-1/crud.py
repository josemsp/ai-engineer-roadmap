users = []

def create(id, name, age):
    """
    Creates a new user in the list
    """
    new_user = {
        "id": id,
        "name": name,
        "age": age
    }
    users.append(new_user)
    
    return new_user

def get_by_id(id):
    """
    Get a user by Id
    """
    for user in users:
        if user["id"] == id:
            return user
    
    return None

def get_all():
    """
    Get all users
    """
    return users

def update(id, name, age):
    """
    Update a user by Id
    """
    user = get_by_id(id)
    user["name"] = name
    user["age"] = age
    
    return True

def delete(id):
    """
    Delete a user by Id
    """
    user = get_by_id(id)
    users.remove(user)
    return True

create(1, "manuel", 34)
print(get_all())
update(1, "jose", 34)
print(get_all())
delete(1)
print(get_all())
