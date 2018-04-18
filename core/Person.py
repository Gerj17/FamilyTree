import math as ma


class GENDER:
    MALE = -1
    FEMALE = 1

    @staticmethod
    def toString(gender):
        """" Takes an integer and return if it represent male of female."""

        if gender == GENDER.MALE:
            return "male"
        elif gender == GENDER.FEMALE:
            return "female"
        else:
            return "unknown"

    @staticmethod
    def fromString(gender):
        """" Takes an string and return the integer represent male of female."""

        if gender == "male" or gender == "MALE":
            return GENDER.MALE
        else:
            return GENDER.FEMALE

    @staticmethod
    def fromInt(gender):
        if gender == 1:
            return GENDER.FEMALE
        else:
            return GENDER.MALE


class RELATIONSHIP:
    IS_NULL = -1
    IS_WIFE = 0
    IS_HUSBAND = 1
    IS_CHILDREN = 2
    IS_MOTHER = 3
    IS_FATHER = 4


class Person:
    # i think the ID should be randomly created probably with the random module

    def __init__(self, idp, name, year, gender):
        self.__id = idp
        self.__fullName = name
        self.__gender = gender
        self.__birthYear = year
        self.__fatherId = None
        self.__motherId = None
        self.__coupleIds = []
        self.__childIds = []

    def setMother(self, mother):
        """ Crates the mother of the person. """

        if (mother.getGender() == GENDER.FEMALE
                and mother.getBirthYear() < self.__birthYear - 10
                and mother.getBirthYear() > self.__birthYear - 60):
            self.__motherId = mother.getID()
            mother.addChildren(self)
        else:
            print("Error: [Person] Can not set " + mother.getName() +
                  " as mother of " + self.__fullName)

    def setFather(self, father):
        """ Crates the father  of the person. """

        if (father.getGender() == GENDER.MALE
                and father.getBirthYear() < self.__birthYear - 10
                and father.getBirthYear() > self.__birthYear - 60):
            self.__fatherId = father.getID()
            father.addChildren(self)
        else:
            print("Error: [Person] Can not set " + father.getName() + \
                  " as father of " + self.__fullName)

    def setCouple(self, couple):
        if couple.getGender() + self.__gender == 0 and \
                ma.fabs(couple.getBirthYear() - self.__birthYear) < 60:
            self.__coupleIds.append(couple.getID())
            couple.addCouple(self)
        else:
            print("Error: [Person] Can not add " + couple.getName() + \
                  " as a couple of " + self.__fullName)

    def addCouple(self, couple):
        self.__coupleIds.append(couple.getID())

    def addChildren(self, children):
        self.__childIds.append(children.getID())

    def getID(self):
        return self.__id

    def getName(self):
        return self.__fullName

    def getGender(self):
        return self.__gender

    def getBirthYear(self):
        return self.__birthYear

    def getFatherID(self):
        return self.__fatherId

    def getMotherID(self):
        return self.__motherId

    def getCoupleIDs(self):
        return self.__coupleIds

    def getChildIDs(self):
        return self.__childIds

    def getNumOfChilds(self):
        return len(self.__childIds)

    def toString(self):
        return str(self.getID()) + ". " + \
               self.getName() + " (" + \
               str(self.getBirthYear()) + "), " + \
               GENDER.toString(self.getGender())



