from typing import Self
class User:
    user_type = "standard"
    
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
        self.active = True
        
    def deactivate(self):
        self.active = False
    
    def activate(self):
        self.activate = True
    
    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active
        }


user1 = User(1, "Ana", "ana@example.com")

print(user1.name)
print(user1.get_info())
user1.deactivate()
print(user1.get_info())
print(User.user_type)

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)

print(account.get_balance())


# getters and setters
class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        
        self._price = value
    

product = Product(100)
print(product.price)
product.price = 200
print(product.price)

# Inheritance vs. Composition
# Inheritance
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} logged in")
    

class Admin(User):
    def delete_user(self, user_id):
        print(f"Deleting user {user_id}")

admin = Admin("Manuel", "manuel@example.com")

admin.login()
admin.delete_user(10)

# composition
class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")
    
class UserService:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def register_user(self, email):
        print("User registered")
        
        self.email_service.send_email(
            email,
            "Welcome!"
        )

email_service = EmailService()
user_service = UserService(email_service)
user_service.register_user("manuel@example.com")


# dataclasses
from dataclasses import dataclass

# @dataclass
@dataclass(frozen=True) # inmutable
class Document:
    document_id: int
    name: str
    category: str
    processed: bool = False # predeterminated

document = Document(
    document_id=1,
    name="vacations.pdf",
    category="human_resources"
)

print(document)
