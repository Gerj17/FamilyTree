import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd() + "../../"))

from core.FamilyTree import *
from core.Human import *

RELATIONSHIP_NAME = {
    RELATIONSHIP.IS_NULL: " [is the current person] ",
    RELATIONSHIP.IS_WIFE: " [is the wife of] ",
    RELATIONSHIP.IS_HUSBAND: " [is the husband of] ",
    RELATIONSHIP.IS_CHILDREN: " [is the children of] ",
    RELATIONSHIP.IS_MOTHER: " [is the mother of] ",
    RELATIONSHIP.IS_FATHER: " [is the father of] "
}

if __name__ == '__main__':
    family = FamilyTree(1, "Cobb")
    if __name__ == '__main__':
        family = FamilyTree(1, "gia dinh toi")


        family.addPerson(1, "Braiden Cobb", 1994, "m")
        family.addPerson(2, "Aiyana Cobb", 1994, "f")
        family.setCouple(1, 2)

        family.addPerson(3, "Han Cobb", 1954, "m")
        family.addPerson(4, "Israel Cobb", 1955, "f")
        family.setCouple(3, 4)
        family.setFather(3, 1)
        family.setMother(4, 1)

        family.addPerson(5, "Mason Cobb", 1990, "m")
        family.addPerson(6, "Krista Cobb", 1990, "f")
        family.setCouple(5, 6)
        family.setFather(3, 5)
        family.setMother(4, 5)
        
        family.addPerson(7, "ong noi toi", 1920, "m")
        family.addPerson(8, "Lillie Cobb", 1925, "f")
        family.setCouple(7, 8)
        family.setFather(7, 3)
        family.setMother(8, 3)

        family.addPerson(9, "Dixie Cobb", 1950, "f")
        family.addPerson(10, "Immanuel Cobb", 1950, "m")
        family.setCouple(9, 10)
        family.setFather(7, 9)
        family.setMother(8, 9)

        family.addPerson(11, "Grady Cobb", 1950, "m")
        family.setFather(7, 11)
        family.setMother(8, 11)

        family.addPerson(12, "Litzy Cobb", 1990, "f")
        family.addPerson(13, "Matthew Cobb", 1989, "m")
        family.setFather(10, 12)
        family.setMother(9, 12)
        family.setFather(10, 13)
        family.setMother(9, 13)

        family.addPerson(14, "Alonzo Cobb", 2010, "m")
        family.setFather(5, 14)
        family.setMother(6, 14)

        family.addPerson(15, "Christian Cobb", 1880, "m")
        family.addPerson(16, "Kristina Cobb", 1885, "f")
        family.setCouple(15, 16)
        family.setFather(15, 7)
        family.setMother(16, 7)

        family.addPerson(17, "Steve Cobb", 1916, "m")
        family.setFather(15, 17)
        family.setMother(16, 17)



    print(family.toString())

    #  relationship = family.search(17, 10)
    relationship = family.search(6, 2)
    # print(relationship)
    print("\n" * 2)
    for i in range(len(relationship)):
        string = family.lookupPerson(relationship[i][0]).getbio() \
                 + RELATIONSHIP_NAME[relationship[i][1]]
        if i > 0:
            # print(i)
            string += family.lookupPerson(relationship[i - 1][0]).getbio()
        # print("--------------",relationship[i - 1])
        # print("--------------",family.lookupPerson(relationship[i ][0]).getbio())

        print(string)
        
input()
