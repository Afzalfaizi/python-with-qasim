class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_details(self):
        return f"{self.brand} {self.model}"        
        
    
my_car = Car("Honda", "Civic")
print(my_car.brand)
print(my_car.model)
print(my_car.display_details())

# commit: feat: Add Car class with basic attributes and display method
