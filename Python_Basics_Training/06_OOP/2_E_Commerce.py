class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        
    

class Electonics(Product):
    def __init__(self,name,price,stock,brand,warranty):
        super().__init__(name,price,stock)
        self.brand=brand
        self.warranty=warranty

    def display_info(self):
        print()
        super().display_info()
        print(f"Brand: {self.brand}")  
        print(f"Warranty: {self.warranty} months")
        print("---")

class Clothing(Product):   
    def __init__(self,name,price,stock,material,size,warranty,brand):
        super().__init__(name,price,stock)
        self.material=material
        self.size=size
        self.warranty=warranty
        self.brand=brand

    def display_info(self):
        super().display_info()
        print(f"Material: {self.material}") 
        print(f"Size: {self.size}")
        print(f"Warranty: {self.warranty} months")
        print(f"Brand: {self.brand}")
        print("---")

p1=Product("Shirt", 20, 50)
p1.display_info()

e1=Electonics("Laptop", 1500, 10, "Dell", 24)
e1.display_info()

c1=Clothing("Shirt", 20, 50, "Cotton", "M", 12, "Nike")
c1.display_info()


