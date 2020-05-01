import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd() + "../../"))

from core.FamilyTree import *
from core.Person import *

RELATIONSHIP_NAME = {
    RELATIONSHIP.IS_NULL: " [is the current person] ",
    RELATIONSHIP.IS_WIFE: " [is the wife of] ",
    RELATIONSHIP.IS_HUSBAND: " [is the husband of] ",
    RELATIONSHIP.IS_CHILDREN: " [is the children of] ",
    RELATIONSHIP.IS_MOTHER: " [is the mother of] ",
    RELATIONSHIP.IS_FATHER: " [is the father of] "
}

if __name__ == '__main__':
    family = FamilyTree(1, "gia dinh toi")

    family.add_person(1, "toi", 1994, Gender.MALE)
    family.add_person(2, "vo toi", 1994, Gender.FEMALE)
    family.set_couple(1, 2)

    family.add_person(3, "cha toi", 1954, Gender.MALE)
    family.add_person(4, "me toi", 1955, Gender.FEMALE)
    family.set_couple(3, 4)
    family.set_father(3, 1)
    family.set_mother(4, 1)

    family.add_person(5, "anh trai toi", 1990, Gender.MALE)
    family.add_person(6, "vo anh trai toi", 1990, Gender.FEMALE)
    family.set_couple(5, 6)
    family.set_father(3, 5)
    family.set_mother(4, 5)

    family.add_person(7, "ong noi toi", 1920, Gender.MALE)
    family.add_person(8, "ba noi toi", 1925, Gender.FEMALE)
    family.set_couple(7, 8)
    family.set_father(7, 3)
    family.set_mother(8, 3)

    family.add_person(9, "chi cua cha toi", 1950, Gender.FEMALE)
    family.add_person(10, "chong cua chi cha toi", 1950, Gender.MALE)
    family.set_couple(9, 10)
    family.set_father(7, 9)
    family.set_mother(8, 9)

    family.add_person(11, "em cua cha toi", 1950, Gender.MALE)
    family.set_father(7, 11)
    family.set_mother(8, 11)

    family.add_person(12, "con cua chi cha toi", 1990, Gender.FEMALE)
    family.add_person(13, "con cua chi cha toi", 1989, Gender.MALE)
    family.set_father(10, 12)
    family.set_mother(9, 12)
    family.set_father(10, 13)
    family.set_mother(9, 13)

    family.add_person(14, "con cua anh trai toi", 2010, Gender.MALE)
    family.set_father(5, 14)
    family.set_mother(6, 14)

    family.add_person(15, "cha cua ong noi toi", 1880, Gender.MALE)
    family.add_person(16, "me cua ong noi toi", 1885, Gender.FEMALE)
    family.set_couple(15, 16)
    family.set_father(15, 7)
    family.set_mother(16, 7)

    family.add_person(17, "anh trai ong noi toi", 1916, Gender.MALE)
    family.set_father(15, 17)
    family.set_mother(16, 17)

    print(family.toString())

    relationship = family.search(17, 10)

    for i in range(len(relationship)):
        string = family.lookup_person(relationship[i][0]).to_string() \
                 + RELATIONSHIP_NAME[relationship[i][1]]
        if i > 0:
            string += family.lookup_person(relationship[i - 1][0]).to_string()
        print(string)
