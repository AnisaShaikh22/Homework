class Human:
    def __init__(self, name = "Anisa", surname = "Shaikh", age = "100", country = "Turkey", city = "Istanbul"):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.talents = []

    def add_talent(self, talent):
        return self.talents.append(talent)

    def person_info(self):
        return "Name: "+ self.name + "\nSurname: "+ self.surname + "\nAge: "+ self.age + "\nCountry: "+ self.country + "\nCity: "+ self.city + "\nTalents: "+ str(self.talents)

# Test
anisa = Human()
anisa.add_talent("Dance")
anisa.add_talent("Music")
anisa.add_talent("Soccer")
print(anisa.person_info())



