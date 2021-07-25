class Ship:
    def __init__(self, name, model, release_year, country) -> None:
        self.name = name
        self.model = model
        self.release_year = release_year
        self.country = country

    def __str__(self) -> str:
        return f"This is a {self.name}, model: {self.model}, it was released in {self.release_year} in {self.country}."
        
class Frigate(Ship):
    def __init__(self, speed, **kwargs) -> None:
        super().__init__(**kwargs)
        self.speed = speed

    def speed_frigate(self):
        return f"Speed {self.speed} knots."

class Destroyer(Ship):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Cruiser(Ship):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

miller = Frigate(name = "frigate", model = "FF1091 Miller", release_year = 1971, country = "USA", speed = 26)
arleigh_burke = Destroyer(name = "destroyer", model = "Arleigh Burke N2000", release_year = 2000, country = "USA")
victoria = Cruiser(name = "cruiser", model = "Victoria", release_year = 2020, country = "Ukraine")

print(miller)
print(miller.speed_frigate())
print(arleigh_burke)
print(victoria)


