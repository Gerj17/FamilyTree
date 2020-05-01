class GENDER:
    """  A class used to identify genders

    Methods
    -------
    to_string(gender)
        identifies parameters gender

    from_string(gender)
        converts gender to object
        Determine if a person instance is male or female."""
    MALE = -1
    FEMALE = 1

    @staticmethod
    def to_string(gender):
        """" Takes an integer and return if it represent male of female."""

        if gender == GENDER.MALE:
            return "Male"
        elif gender == GENDER.FEMALE:
            return "Female"
        else:
            return "Unknown"

    @staticmethod
    def fromString(gender):
        """" Takes a string and return the integer represent male of female."""
        # TODO Find a way to fix this BS
        if gender.lower() == "female":
            return GENDER.FEMALE

        if gender.lower() == "f":
            return GENDER.FEMALE

        if gender.lower() == "male":
            return GENDER.MALE
        if gender.lower() == "m":
            return GENDER.MALE
        else:
            print("This is not a gender")

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
    """
    A class used to represent a human persons and some of their attributes
    Creates members of  a nuclear family.
    """

    def __init__(self, idp, name, year, gender):
        """
        :param int idp: ID number object iteration
        :param str name: Given name of iteration
        :param int b_year: Year of birth for iteration #TODO Change year into date of birth using time package
        :param int gender: the sex of a person F / M #TODO get rid of gender class, change parameter requirement to F/M
        """

        # i think the ID should be randomly created probably with the random module
        self.__id = idp
        self.__fullName = name
        self.__gender = GENDER.fromString(str(gender))
        self.__birthYear = year
        self.__fatherId = None
        self.__motherId = None
        self.__coupleIds = []
        self.__childIds = []

    def setMother(self, mother):
        """ Crates the mother of the person.
          The input is an instance of the person object"""

        if (mother.getGender() == GENDER.FEMALE
                and self.__birthYear - 10 > mother.getBirthYear() > self.__birthYear - 60):

            self.__motherId = mother.getID()
            mother.addChildren(self)
        else:
            Error_ms = 'Error: [Human:Person] Can not set ' + mother.getName() + ' as mother of ' + self.__fullName + \
                       'because she '
            if self.__birthYear - 10 < mother.getBirthYear():
                print(Error_ms + 'can\'t have ', self.__fullName, 'at such a young age')
            if mother.getBirthYear() < self.__birthYear - 60:
                print(Error_ms + 'can\'t have ', self.__fullName, 'at such an old age')

    def setFather(self, father):
        """ Crates the father  of the person.
         The input is an instance of the person object """

        if father.getGender() == GENDER.MALE and self.__birthYear - 10 > father.getBirthYear():
            self.__fatherId = father.getID()
            father.addChildren(self)
        else:
            Error_ms = 'Error: [Human:Person] Can not set ' + father.getName() + ' as mother of ' + self.__fullName + \
                       'because she '
            print(Error_ms + 'can\'t have ', self.__fullName, 'at such a young age')

    def setCouple(self, couple):  # TODO change to fit modern times
        """ Creates the spouse of person.
         The input is an instance of the person object.
         The dictionary 'self.__coupleIds' will contain the ID of the
         spouse of the person. """

        if couple.getGender() + self.__gender == 0 and \
                abs(couple.getBirthYear() - self.__birthYear) < 60:
            self.__coupleIds.append(couple.getID())
            couple.addCouple(self)
        else:
            print("Error: [Human] Can not add " + couple.getName() +
                  " as a couple of " + self.__fullName)

    def addCouple(self, couple):
        """
        The list 'self.__coupleIds' will contain contain the ID of the
         spouse of the person ."""

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

    def getbio(self):
        # TODO use pythonic string formatting
        return str(self.getID()) + ". " + \
               self.getName() + " (" + \
               str(self.getBirthYear()) + "), " + \
               GENDER.toString(self.getGender())
