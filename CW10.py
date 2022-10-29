from functools import reduce


class Item:

    id_counter = 0
    def __init__(self,type,price):
        Item.id_counter += 1
        self.type = type
        self._id = Item.id_counter
        self._price = price


    @property
    def id(self):
        return self._id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        if(price > 0):
         self._price = price

    @staticmethod
    def priceWithDiscount (price,discount):
        if discount < 0 or discount > 100:
            return None
        return price * ((100 - discount) / 100)


class Toy(Item):

    def __init__(self, price):
        super().__init__("Toy", price)

    def applyDiscount (self, discount):
        super().priceWithDiscount(self.price, discount)

class Book(Item):

    def __init__(self, price):
        super().__init__("Book", price)

    def applyDiscount (self,dicsount):
        super().priceWithDiscount(self.price, min(dicsount + 10, 100))

class Painting(Item):

    def __init__(self, price):
        super().__init__("Painting", price)

    def applyDiscount (self, discount):
        super().priceWithDiscount(self.price, max(discount - 10, 0))

class Shop:

    def __init__(self):
        self.items = []

    def addItem (self,item):
        self.items.append(item)

    def findItemByID (self,id):
        for item in self.items:
            if(item.id == id):
               return item
        return None

    def removeItemByID (self,id):
        for item in self.items:
            if(item.id == id):
                self.items.remove(item)
        # item = self.findItemByID(id)
        # self.items.remove(item)

    def countItemWithType (self,type):
        ans = 0
        for item in self.items:
            if(item.type == type):
                ans += 1
        return ans

    def applyDiscount (self,discount):
        for item in self.items:
            item.applyDiscount(discount)

    def totalSum (self):
        ans = 0
        for item in self.items:
            ans += item.price
        return ans

class Animal:

    def __init__(self,name,age):
        self._name = name
        self._age = age
        self._type = "Animal"

    @property
    def type (self):
        return self._type

    def getFoodCost (self):
        return 100

    def getGroomingCost (self):
        return 100

class ExoticAnimal:

    def getGroomingCost (self):
        return 500

class Wolf(Animal):

    def __init__(self,name,age):
        super().__init__(name,age)
        self._type = "Wolf"

class Parrot(Animal):

    def __init__(self,name,age):
        super().__init__(name,age)
        self._type = "Parrot"

    def getFoodCost(self):
        return 50

class Lion(ExoticAnimal,Animal): # jer Exotic imitoro rac exotics aqvs yvelaferi anu is erti metodi gavrceldes da
    # mere daexmaros danarchen metodebshi Animal
    # piriqit ro dagvewera 100 100 ze dajdeba price bi exotics daikidebda imitoro aq exoticis methodi

    def __init__(self,name,age):
        super().__init__(name,age)
        self._type = "Lion"


class Zebra(ExoticAnimal,Animal):

    def __init__(self,name,age):
        super().__init__(name,age)
        self._type = "Zebra"

    def getFoodCost(self):
        return 80

class Vivarium:

    def __init__(self,area,age):
        self._area = area
        self._age = age
        self._animals = []

    def getUpKeepCost (self):
        return 10*self._area + 500*(self._age//10) + sum(map(lambda a: a.getFoodCost() + a.getGroomingCost(), self._animals))

    def carnivoreCount(self):
        func = lambda num, animal: num + 1 if (animal.type == "Wolf" or animal.type == "Lion") else num
        ans = reduce(func,self._animals,0)
        return ans

    def addAnimal (self,animal):
        self._animals.append(animal)

    def addAnimals (self,*animals):
        for animal in animals:
          self._animals.append(animal)

class Zoo:

    def __init__(self):
        self._vivariums = []

    def addVivarium (self,vivarium):
        self._vivariums.append(vivarium)

    def countCarnivore (self):
        ans = 0
        for vivarium in self._vivariums:
            ans += vivarium.carnivoreCount()

        return ans

    def getUpKeepCost (self):
        ans = 0
        for vivarium in self._vivariums:
            ans += vivarium.getUpKeepCost()

        return ans


















