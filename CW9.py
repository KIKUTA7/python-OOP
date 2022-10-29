from functools import reduce


class Student:

    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = []

    def addGrade(self,grade,credit):
        self.grades.append((grade,credit))

    def getGPA(self):
        sum = reduce(lambda x,y: x + y[0]*y[1],list(self.grades),0)
        creditsSum = reduce(lambda x,y: y[1] + x,list(self.grades),0)
        if (creditsSum == 0): return 0.0
        return float(sum) / float(creditsSum)


class Course:

    def __init__(self,name,credits):
        self.name = name
        self.credits = credits
        self.students = []

    def registerStudents(self,student):
        self.students.append(student)

    def gradeStudents(self):
        for student in self.students:
            student.grades.append((4.0,self.credits))

        # meore varianti ari student.addGrade methodit


class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def str(self):
        return self.suit + " " +self.value


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))

    def printDeck (self):
        for card in self.cards:
            print(card.str())

class Book:
    def __init__(self,name,author,ID):
        self.name = name
        self.author = author
        self.__ID = ID

    def getName (self):
        return self.name

    def getAuthor(self):
        return self.author

    def getID (self):
        return self.__ID

    def setID (self,ID):
        self.__ID = ID

class User:
    def __init__(self,name,socialID):
        self.name = name
        self.__socialID = socialID
        self.books = []

    def getName (self):
        return self.name

    def getBooks (self):
        return self.books

    def rentFromLibrary (self,library,bookname):

        if(library.rentBook(bookname,self)):
            self.books.append(bookname)
            return True
        return False




class Library:
    def __init__(self):
        self.users = []
        self.books = []
        self.rentals = {}

    def registerUser (self,user):
        if(user not in self.users):
            self.users.append(user)
            return True
        return False
    def addBook (self,book):
        if(book not in self.books):
           self.books.append(book)
           return True
        return False

    def removeBook (self,book):
        self.books.remove(book)

    def findBookByName (self,bookname):
        for book in self.books:
            if(book.getName() is bookname):
                return book
        return None

    def findBookByID (self,id):
        for book in self.books:
            if(book.getID() is id):
                return book
        return None

    def rentBook (self,user,book):
        # if user not in self.users - asec sheileba
        if((not self.users.__contains__(user)) or (not self.books.__contains__(book))):
            print("user or book can't be found")
            return False
        if book  in self.rentals.keys():
            print("book is already rented")
            return False
        self.rentals[book] = user
        return True

    def returnBook(self, book, user):
        self.rentals.pop(book)

class Fraction:
      def __init__ (self,numerator,denominator):
          self.numerator = numerator
          self.denominator = denominator

      def printFrac (self):
          print(str(self.numerator) + "/" + str(self.denominator))

      def simplify (self):
          numer = self.numerator
          denom = self.denominator

          while (numer != 0 and denom != 0 ):
              if(numer >= denom):
                  numer = numer % denom
              else:
                  denom = denom % numer

          gcd = max(denom,numer)

          self.numerator = self.numerator // gcd
          self.denominator = self.denominator // gcd


      def add(self,fraction):
          denom = self.denominator * fraction.denominator
          num = self.denominator * fraction.numerator + fraction.denominator * self.numerator

          return Fraction(num,denom)

      def subtract (self,fraction):
          denom = self.denominator * fraction.denominator
          numer = fraction.denominator * self.numerator - self.denominator * fraction.numerator

          return Fraction(numer,denom)

      def multiply (self,fraction):
          denom = self.denominator * fraction.denominator
          numer = self.numerator * fraction.numerator

          return Fraction (numer,denom)

      def divide (self,fraction):
          denom = self.denominator * fraction.numerator
          numer = self.numerator * fraction.denominator

          return Fraction(numer,denom)


class Author:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age




class Publisher:
    def __init__(self,name,country):
        self.name = name
        self.country = country

class book:
    def __init__(self,ID,name,author,publisher,number):
        self.ID = ID
        self.name = name
        self.author = author
        self.publisher = publisher
        self.number = number

    def getPublisherByCountry (self,country):
        return [x for x in self.publisher if x.country == country]



class bookshop:

    def __init__(self):
        self.bookprices = []
        self.budget = 0

    def add(self,book,price):
        self.bookprices.append((book,price))

    def remove (self,ID):
        for book in self.bookprices:
            if(book.ID is ID):
                self.bookprices.remove(book)

    def buy (self,book):
        for boook in self.bookprices:
            if(boook[0] == book):
                self.budget += boook[1]
                self.remove(book.ID)
                book.number -= 1
                break






if __name__ == '__main__':
        student = Student("Beqa", 1)
        student2 = Student("Achiko", 2)

        student.addGrade(3.7, 4)
        student.addGrade(3.5, 2)
        student2.addGrade(3.7, 2)

        course = Course("Python", 5)
        course.registerStudents(student)
        course.registerStudents(student2)

        course.gradeStudents()

        print(student.getGPA())

        card = Card ("Hearts","7")

        print(card.str())

        deck = Deck()

        deck.printDeck()

        book = Book("elene","beqa kikutadze",1)

        print(book.getID())
        print(book.getName())
        print(book.getAuthor())
        book.setID(7)
        print(book.getID())

        book2 = Book("80000","beqa kikutadze",2)

        library = Library()

        library.addBook(book)
        library.addBook(book2)

        user = User("Elene",7)
        user2 = User("Beqa",8)

        library.registerUser(user)
        library.registerUser(user2)

        print(library.findBookByName("book3"))

        book3 = Book("book3","beqa kikutadze",3)
        library.addBook(book3)
        print(library.findBookByName("book3"))
        library.removeBook(book3)

        print(library.findBookByName("elene"))
        print(library.findBookByName("book3"))
        print(library.findBookByID(7))

        library.rentBook(user,book)
        library.rentBook(user2,book)
        library.rentBook(user2,book3)

        library.returnBook(book,user)
        library.rentBook(user2,book)
        library.rentBook(user,book)

        fraction1 = Fraction(35,7)
        fraction1.printFrac()

        fraction1.simplify()

        fraction1.printFrac()
        fraction1 = fraction1.add(Fraction(4,5))
        fraction1.printFrac()
        fraction1 = fraction1.subtract(Fraction(4,5))
        fraction1.printFrac()
        fraction1 = fraction1.multiply(Fraction(4,5))
        fraction1.printFrac()
        fraction1.simplify()
        fraction1 = fraction1.divide(Fraction(4,5))
        fraction1.printFrac()


















