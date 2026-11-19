users = [
    {"name": "Ana", "age": 17, "active": True },
    {"name": "Pedro", "age": 25, "active": False },
    {"name": "Carlos", "age":16, "active": True },
    {"name": "Laura", "age": 30, "active": False}
]

def get_adult_users():
    adult_users = []
    for user in users:
        if user["age"] >= 18:
            adult_users.append(user)
    return adult_users

def find_user_by_name(name):
    for user in users:
        if user["name"] == name:
            return user
    
    return None

def get_active_metrics(users_list):
    n_active = 0
    n_inactive = 0
    
    for user in users_list:
        if user["active"]:
            n_active += 1
        else:
            n_inactive += 1
    
    print(f"Active: {n_active} \nInactive: {n_inactive}")

def validate_user(name, email, age):
    if name == "" or name == None:
        return False
    if len(email.split("@")) != 2:
        return False
    if age < 18:
        return False
    
    return True


# help(str)
print(get_adult_users())
print(find_user_by_name("Lauraa"))
print(get_active_metrics(users))
print(f"Is Valid user: {validate_user("Manuel", "oexample.com", 18)}")
