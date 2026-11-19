# conditionals
age = 34

if age >= 18:
    print("adult")
else:
    print("minor")


score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 60:
    print("Regular")
else:
    print("Failed")

age = 25
has_account = True

if age >= 18 and has_account:
    print("Access granted")


users = ["Ana", "Pedro", "Carlos"]
for user in users:
    print(user, end=' ')

for number in range(5):
    print(number)

for number in range(1, 6):
    print(number)

counter = 0
while counter < 5:
    print(counter)
    counter += 1


import sys_users
# O si prefieres importar funciones específicas:
# from sys_users import get_active_users, find_user, print_users

