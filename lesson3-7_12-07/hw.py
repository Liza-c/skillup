class Car:
    def __init__(self, model, year, engine, color, price):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price
    
    def car_parameters(self):
        return f"This is {self.model}, {self.year} release, engine size: {self.engine}, "\
            f"car color: {self.color}, price: {self.price}:"
    
camry = Car(
    model= 'Camry', 
    year= 2015, 
    engine= '3.5', 
    color = 'red', 
    price = 14000
    )
        