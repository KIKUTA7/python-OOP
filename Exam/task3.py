""" Task 3 [8 points]"""

"""
Write a class Visitor.
Vistor should have 4 attributes:
   * name - name of the visitor, public attribute
   * age - age of the visitor, public attribute
   * id - id of the visitor, hidden attribute
   * passcode - unique passcode of the visitor, property
Class should have a constructor, that gets all 4 value as arguments
and stores them as attributes. Class also should have 'getID' function
that returns id and property getter function for passcode.


Write a class VisitorQueue.
VisitorQueue class should have one static method = 'isValidPasscode'. This
function takes string as an argument and checks if it is valid code. Code is
valid if:
    1. It contains at least 6 characters
    2. All characters are either upper or lower case letters or numbers.
    3. There is at least 1 upper case letter, at least 1 lower case letter
       and at least 1 number.
Class shouls also have one attribute - a list to store visitors, which are in queue.
Furthermore, class should have following methods:
* constructor - To initialise visitor queu attribute with empty list.
* add - Gets visitor as an argument. Visitor's passcode should be checked with 'isValidPasscode'
        function. If visitor has a valid passcode, add him/her at the end of the queue and return
        True. If visitor does not have a valid passcode, do not add him/her into the queue and 
        return False.
* next - Returns the next visitor in the queue. Next visitor is one in the begining of the queue.
         If there is no one in the queue, return None.
* remove - Removes the visitor from the begining of the queue. If visitor is removed from the queue
           function should return True. If there is no one to remove, function should return False.

"""

class Visitor: 
    def __init__(self,name,age,id,passcode):
        self.name = name
        self.age = age
        self.__id = id
        self._passcode = passcode

    @property
    def passcode(self):
        return self._passcode

    def getID(self):
        return self.__id



class VisitorQueue:

    def __init__(self):
        self.visitorqueue = []


    @staticmethod
    def isValidPasscode(str):
        if(len(str) < 6):
            return False
        lower = 0
        upper = 0
        number = 0
        for char in str:
            if(not (char.isalpa() or char.isnumeric())):
                return False
            if(char.isalpa() and char.islower()):
                lower += 1
            elif (char.isalpa() and char.isupper()):
                upper += 1
            else:
                number += 1

        if(lower == 0 or upper == 0 or number == 0):
            return False
        return True

    def add(self, visitor):
        if (VisitorQueue.isValidPasscode(visitor.passcode)):
            self.visitorqueue.append(visitor)
            return True
        return False

    def next(self):
        if(len(self.visitorqueue) > 0):
            return self.visitorqueue[0]
        return None

    def remove(self):
        if(len(self.visitorqueue) > 0):
            self.visitorqueue = self.visitorqueue[1:]
            return True
        return False
