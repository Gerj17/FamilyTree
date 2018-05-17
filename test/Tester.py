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

    family.addPerson(1, "Braiden Cobb", 1994, "m")
    family.addPerson(1, "Braiden Cobb", 1924, "F")
    family.addPerson(2, "Aiyana Cobb", 1924, "m")
    family.setCouple(1, 2)


    family.setCouple(1, 2)
    #print(family.treedict())

    family.addPerson(3, "Israel Cobb", 1954, "F")
    family.addPerson(4, "Ariel Cobb", 1975, "F")
    family.setMother(1, 3)
    family.setMother(1, 4)

    family.setFather(2, 4)
    family.setFather(2, 4)


    family.setCouple(3, 4)
    family.setFather(3, 1)
    family.setMother(4, 1)

    family.setCouple(5, 6)
    family.setFather(3, 5)
    family.setMother(4, 5)



    family.addPerson(8, "Krista Cobb", 1925, "F")
    family.setCouple(7, 8)
    family.setFather(7, 3)
    family.setMother(8, 3)

    family.addPerson(9, "Lillie Cobb", 1950, "F")
    family.addPerson(10, "Mason Cobb", 1950, "m")
    family.setCouple(9, 10)
    family.setFather(7, 9)
    family.setMother(8, 9)

    family.addPerson(11, "Alonzo Cobb", 1950, "m")
    family.setFather(7, 11)
    family.setMother(8, 11)

    family.addPerson(12, "Dixie Cobb", 1990, "F")
    family.addPerson(13, "Immanuel Cobb", 1989, "m")
    family.setFather(10, 12)
    family.setMother(9, 12)
    family.setFather(10, 13)
    family.setMother(9, 13)

    family.addPerson(14, "Matthew Cobb", 2010, "m")
    family.setFather(5, 14)
    family.setMother(6, 14)

    family.addPerson(15, "Grady Cobb", 1880, "m")
    family.addPerson(16, "Litzy Cobb", 1885, "F")
    family.setCouple(15, 16)
    family.setFather(15, 7)
    family.setMother(16, 7)

    family.addPerson(17, "Christian Cobb", 1916, "m")
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
