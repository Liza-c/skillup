class Device:
    def __init__(self, name, model, price) -> None:
        self.name = name
        self.model = model
        self.price = price

    def __str__(self) -> str:
        return f"This is a {self.name}, model: {self.model}, price: {self.price}."
        

class CoffeeMachine(Device):
    def __init__(self, name, model, price, water_volume) -> None:
        super().__init__(name, model, price)
        self.water_volume = water_volume

    def get_water_volume(self):
        return f"Volume of water in the coffee machine: {self.water_volume}."

class Blender(Device):
    def __init__(self, name, model, price, bowl_volume) -> None:
        super().__init__(name, model, price)
        self.bowl_volume = bowl_volume
    
    def blender_bowl_volume(self):
        return f"Blender bowl volume : {self.bowl_volume}."

class MeatGrinder(Device):
    def __init__(self, name, model, price, number_attachments) -> None:
        super().__init__(name, model, price)
        self.number_attachments = number_attachments
    
    def attachment(self):
        return f"Number of attachments in a meat grinder {self.number_attachments}."
    
krups = CoffeeMachine(name = "coffe machine", model = "KRUPS EA872B10", price = 29999, water_volume = 2)
print(krups)
print(krups.get_water_volume())
philips_123 = Blender(model = "Philips", name = "blender", price = 2000, bowl_volume = 1)
print(philips_123)
print(philips_123.blender_bowl_volume())
philips_n200 = MeatGrinder(name = "meat grinder", model = "Philips 200", price = 3000, number_attachments = 3)
print(philips_n200)
print(philips_n200.attachment())