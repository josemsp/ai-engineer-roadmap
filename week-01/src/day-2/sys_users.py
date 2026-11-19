users = [
    {
        "id": 1,
        "name": "Ana",
        "active": True
    },
    {
        "id": 2,
        "name": "Pedro",
        "active": False
    },
    {
        "id": 3,
        "name": "Carlos",
        "active": True
    }
]

def get_active_users():
    active_users = []
    
    for user in users:
        if user["active"]:
            active_users.append(user)
    
    return active_users

def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    
    return None

def print_users():
    for user in users:
        status = "Active" if user["active"] else "Incative"
        print(f"{user["name"]} - {status}")

print("\nsys_user\n")
print("All users:")
print_users()

print("Active users")
get_active_users()

print("Search users")
print(find_user(1))
