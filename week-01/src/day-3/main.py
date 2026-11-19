from user_service import (
    create_user,
    get_user_by_id,
    get_active_users,
    deactive_user
)

users = []

create_user(users, 1, "Ana", "ana@example.com", 25)
create_user(users, 2, "Pedro", "pedro@example.com", 30)
create_user(users, 3, "Carlos", "carlos@example.com", 22)

print("All users:")
print(users)

print("\nFind user:")
print(get_user_by_id(users, 2))

print("\nDeactivate user:")
print(deactive_user(users, 2))

print("\nActive users:")
print(get_active_users(users))

# exercise 1
def calculate_price(price, quantity=1, discount=0):
    total = price * quantity
    
    if discount:
        return total - (total * discount / 100)
    
    return total


print(calculate_price(100))
print(calculate_price(100, 2))
print(calculate_price(100, 2, 10))

# excercise 2
def calculate_average(*args):
    if len(args) == 0:
        return 0
    
    sum = 0
    for num in args:
        sum += num
    
    return sum / len(args)

print(calculate_average(10, 20,30))
print(calculate_average())

# exercise 3
def get_user_summary(user):
    return f"user name: {user["name"]} \nemail: {user["email"]}"
    

print(get_user_summary({ "name": "Ana", "email": "ana@example.com"}))

# exercise 4
def update_user_email(users, user_id, new_email):
    user = get_user_by_id(users, user_id)
    
    if user == None:
        return False
    
    user["email"] = new_email
    return True

print(update_user_email(users, 1, "updated@example.com"))
print(get_active_users(users))
