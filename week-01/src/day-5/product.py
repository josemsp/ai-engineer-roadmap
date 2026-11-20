from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int = 0
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Initial price cannot be negative")
        
        if self.stock < 0:
            raise ValueError("Initial stock cannot be negative")
        
    def update_stock(self, quantity: int):
        new_stock = self.stock + quantity
        
        if new_stock < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.stock = new_stock

