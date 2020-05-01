import math as ma


class Gender:
    """
    A class used to identify genders

    Methods
    -------
    to_string(gender)
        identifies parameters gender

    from_string(gender)
        converts gender to object
    """
    MALE = -1
    FEMALE = 1

    @staticmethod
    def to_string(gender):
        if gender == Gender.MALE:
            return "male"
        elif gender == Gender.FEMALE:
            return "female"
        else:
            return "unknown"

    @staticmethod
    def from_string(gender):
        """
        converts gender to object
        :param str gender:
        :return:
        """
        if gender == "male" or gender == "MALE":
            return Gender.MALE
        else:
            return Gender.FEMALE

    @staticmethod
    def from_int(gender):
        """

        :param gender:
        :return:
        """
        if gender == 1:
            return Gender.FEMALE
        else:
            return Gender.MALE


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
    """

    def __init__(self, idp, name, b_year, gender):
        """
        :param int idp: ID number object iteration
        :param str name: Given name of iteration
        :param int b_year: Year of birth for iteration #TODO Change year into date of birth using time package
        :param int gender: the sex of a person F / M #TODO get rid of gender class, change parameter requirement to F/M
        """
        self.__id = idp
        self.__fullName = name
        self.__gender = gender
        self.__birthYear = b_year
        self.__fatherId = None
        self.__motherId = None
        self.__coupleIds = []
        self.__childIds = []

    def set_mother(self, mother):
        if (mother.get_gender() == Gender.FEMALE
                and mother.get_birth_year() < self.__birthYear - 10
                and mother.get_birth_year() > self.__birthYear - 60):
            self.__motherId = mother.get_id()
            mother.add_children(self)
        else:
            print("Error: [Person] Can not set " + mother.get_name() + \
                  " as mother of " + self.__fullName)

    def set_father(self, father):
        if (father.get_gender() == Gender.MALE
                and father.get_birth_year() < self.__birthYear - 10
                and father.get_birth_year() > self.__birthYear - 60):
            self.__fatherId = father.get_id()
            father.add_children(self)
        else:
            print("Error: [Person] Can not set " + father.get_name() + \
                  " as father of " + self.__fullName)

    def set_couple(self, couple):
        if couple.get_gender() + self.__gender == 0 and \
                ma.fabs(couple.get_birth_year() - self.__birthYear) < 60:
            self.__coupleIds.append(couple.get_id())
            couple.add_couple(self)
        else:
            print("Error: [Person] Can not add " + couple.get_name() + \
                  " as a couple of " + self.__fullName)

    def add_couple(self, couple):
        self.__coupleIds.append(couple.get_id())

    def add_children(self, children):  # why not add_child
        self.__childIds.append(children.get_id())

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__fullName

    def get_gender(self):
        return self.__gender

    def get_birth_year(self):
        return self.__birthYear

    def get_father_id(self):
        return self.__fatherId

    def get_mother_id(self):
        return self.__motherId

    def get_couple_i_ds(self):
        return self.__coupleIds

    def get_child_i_ds(self):
        return self.__childIds

    def get_num_of_child(self):
        return len(self.__childIds)

    def to_string(self):
        # TODO simplify the code below
        return str(self.get_id()) + ". " + \
               self.get_name() + " (" + \
               str(self.get_birth_year()) + "), " + \
               Gender.to_string(self.get_gender())
