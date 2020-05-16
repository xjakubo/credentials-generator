#!/usr/bin/env python3

from random import randint
from time import strftime

class Picker:
    def __init__(self, firstname, lastname, cities):
        self.firstname = firstname
        self.lastname = lastname
        self.cities = cities
        self.result = {}
        pass

    def load(self):
        with open(self.firstname) as firstnames:
            self.firstname = firstnames.read().split("\n")
            self.firstname.pop()
        with open(self.lastname) as lastnames:
            self.lastname = lastnames.read().split("\n")
            self.lastname.pop()
        with open(self.cities) as city:
            self.cities = city.read().split("\n")
            self.cities.pop()
        pass

    def generateBirthday(self):
        curryear = int(strftime("%Y"))
        birthyear = curryear - randint(18, 75)
        birthmonth = randint(1,12)
        birthday = randint(1,28)
        return birthday, birthmonth, birthyear

    def postalCode(self):
        dd = str(randint(0,95)).zfill(2)
        ddd = str(randint(0,999)).zfill(3)
        return dd + "-" + ddd
    def generate(self):
        self.result["First Name"] = self.firstname[randint(0, (len(self.firstname)-1))]
        self.result["Last Name"] = self.lastname[randint(0, (len(self.firstname)-1))]
        self.result["Date of Birth"] = self.generateBirthday()
        self.result["Postal Code"] = self.postalCode()
        self.result["City"] = self.cities[randint(0, (len(self.cities)-1))]
        pass


if __name__ == "__main__":
    picker = Picker("data/firstnames.txt", "data/lastnames.txt", "data/cities.txt")
    picker.load()
    picker.generate()
    print(picker.result)
