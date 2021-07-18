class Cat:
    def __init__(self, **kwargs) -> None:
        self.__name = kwargs.get('name', 'robot')
        self.__age = kwargs.get("age", 0)
        self.__satiety = kwargs.get("satiety", 50)
        self.__money = kwargs.get("money", 0)
        #for key, value in kwargs.items():
            #self.__setattr__(key, value)
        
    def __str__(self) -> str:
        return f"Name: {self.__name}, age: {self.__age}, satiety: {self.__satiety}, money: {self.__money}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
    
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def satiety(self):
        return self.__satiety
    
    @satiety.setter
    def satiety(self, value):
        if type(value) != int or (value < 0 or value > 100):
            raise ValueError("The value must be an integer. The value must be between 0 and 100.")
        else:
            self.__satiety = value
    
    @property
    def check_satiety(self):
        if self.__satiety <= 20:
            return "I am very hungry. I urgently need to eat! Feed me!"
        if self.__satiety in range(20, 40):
            return "I am hungry. Feed me"
        if self.__satiety in range(40, 60):
            return "I don't mind something to eat."
        if self.__satiety in range(60, 80):
            return "I'm fine. I don't think about food."
        if self.__satiety >= 80:
            return "I'm full."
    
    def eat(self):
        if self.__money > 5:
            self.satiety += 10
            self.__money -= 5
            print("Thanks for the food")
        else:
            print("You have no money. Go play!")

    def play(self):
        self.__money += 10
        self.__satiety -= 5
        print("You received 10 coins for the game.")
    
if __name__ == "__main__":
    bob = Cat(name="Bob", age = 2, satiety = 30, money = 10)
    bob.age = 3
    print(bob)
    print(bob.check_satiety)
    bob.eat()
    print(bob.check_satiety)
    print(bob)
    bob.eat()
    bob.play()
    bob.play()
    print(bob)

        
        