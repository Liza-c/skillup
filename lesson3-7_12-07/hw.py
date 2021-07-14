#===========================================================================================
#=============================== Task 1 ====================================================
#===========================================================================================

class Car:
    def __init__(self, model, year, engine, color, price):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price
   
    def get_name(self):
        return f"This is {self.model}."

    def get_parameters(self):
        return f"This car is {self.year}, engine size: {self.engine}, car color: {self.color}."
    
    def get_price(self):
        return f"The price: {self.price}."

audi_q7 = Car(
    model="Audi Q7", 
    year = 2015, 
    engine= "Diesel 3.0L", 
    color = "black", 
    price = 55000)

print(audi_q7.get_name())
print(audi_q7.get_parameters())
print(audi_q7.get_price())
#===========================================================================================
#=============================== Task 2 ====================================================
#===========================================================================================

class Book:
    def __init__(self, name, year, author, genre, price, availability = True):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.price = price
        self.availability = availability
    
    def book_description(self):
        return f"Name: {self.name}, author: {self.author}, year: {self.year}, genre: {self.genre}."
    
    def get_author(self):
        return f"The {self.name} was written by {self.author}."

    def get_year(self):
        return f"This book was written in {self.year}."

    def get_price(self):
        return f"Book price - {self.price}."

    def availability_in_store(self):
        if self.availability is True:
            return f"This book is in the store, its price - {self.price}."
        else:
            print("This book is not available for sale.")

harry_potter = Book(
        name = "Harry Potter and the Chamber of Secrets",
        year=1998,
        author = "J. K. Rowling",
        genre = "fantasy",
        price = 100)
book_thief = Book(
        name = "The Book Thief",
        year = 2005,
        author = "Markus Zusak",
        genre = "military, drama",
        price = 90,
        availability = False)

print(harry_potter.get_author())
print(harry_potter.get_year())
print(harry_potter.availability_in_store())
print(book_thief.book_description())
print(book_thief.get_price())
print(book_thief.availability_in_store())

#===========================================================================================
#=============================== Task 3 ====================================================
#===========================================================================================

class Stadium:
    def __init__(self, name, country, city, date, capacity):
        self.name = name
        self.country = country
        self.city = city
        self.date = date
        self.capacity = capacity
    
    def get_name(self):
        return f"This is {self.name}."

    def get_location(self):
        return f"This stadium is located in {self.country} in the city of {self.city}."

    def get_date(self):
        return f"The opening date of the stadium is {self.date}."

    def get_capacity(self):
        return f"Stadium capacity - {self.capacity} seats."

dnipro_arena = Stadium(
    name = "Dnipro Arena",
    date = "14.09.2008",
    country = "Ukraine",
    city = "Dnipro",
    capacity = 34000)

print(dnipro_arena.get_name())
print(dnipro_arena.get_date())
print(dnipro_arena.get_location())
print(dnipro_arena.get_capacity())
