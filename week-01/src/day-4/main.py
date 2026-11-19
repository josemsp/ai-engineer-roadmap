# Data Structures, Mutability, and Copies in Python

users = ["Ana", "Pedro", "Carlos"]

# add
users.append("Laura")

# remove for value
users.remove("Pedro")

# remove for index
users.pop(0)

# check length
print(len(users))

# check exist
print("Carlos" in users)

# sort
users.sort()

print(users)

# extend (Adds all items from another collection.)
users = ["Ana", "Pedro"]

users.extend(["Carlos", "Laura"])

print(users)
# ['Ana', 'Pedro', 'Carlos', 'Laura']


# Dictionaries
user = {
    "id": 1,
    "name": "Ana"
}

# get value
print(user.get("name"))

# get inexistent value
print(user.get("email"))

# add or update
user["email"] = "ana@example.com"

# check availablity
print("email" in user)

# delete
user.pop("email")

# iterate
for key, value in user.items():
    print(key, value)
    
# Sets
permissions = {"read", "write", "delete"}

permissions.add("admin")

permissions.discard("write")

print("read" in permissions)
print(permissions)

# operations
user_permissions = {"read", "write"}
admin_permissions = {"read", "write", "delete"}

# common elements
print(user_permissions & admin_permissions)

# all elements without duplicates
print(user_permissions | admin_permissions)

# elements that are in the first list but not in the second
print(admin_permissions - user_permissions)


# references
user1 = {
    "name": "Ana",
    "age": 25
}

user2 = user1

user2["age"] = 30

print(user1)
print(user2)

# avoid reference issues
user1 = {
    "name": "Ana",
    "age": 25
}

user2 = user1.copy()

user2["age"] = 30

print(user1["age"])  # 25
print(user2["age"])  # 30


# Shallow copy vs Deep copy
user1 = {
    "name": "Ana",
    "address": {
        "city": "CDMX"
    }
}

user2 = user1.copy()

user2["address"]["city"] = "Cuernavaca"

print(user1["address"]["city"])

# deepcopy
import copy

user1 = {
    "name": "Ana",
    "address": {
        "city": "CDMX"
    }
}

user2 = copy.deepcopy(user1)
user2["address"]["city"] = "Cuernavaca"

print(user1["address"]["city"])
# CDMX
print(user2["address"]["city"])
# Cuernavaca


# List comprehension
# tradicional
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# with comprehension
numbers = [1,2,3,4,5]
squares = [num **2 for num in numbers]
print(squares)

# with conditionals
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    num
    for num in numbers
    if num % 2 == 0
]
print(even_numbers)


# Dictionary comprehension
numbers = [1,2,3,4]

squares = {
    number: number **2
    for number in numbers
}
print(squares)

