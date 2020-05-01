import core.Human as Person
import copy


class FamilyTree:
    """ Creates persons in the using the Human class.
    Stores their ID in the self.__tree dictionary, the ID is the key and the value is the instance of
    the person class, all all interactions between individuals take place in
    the person class """

    def __init__(self, idf, familyName):
        self.__idFamily = int(idf)
        self.__familyName = str(familyName)
        self.__tree = {}

    def treedict(self):
        for key, value in self.__tree.items():
            print(key, "=", value)

    def lookupPerson(self, idp):
        return copy.deepcopy(self.__tree[idp])

    def addPerson(self, idp, name, year, gender):
        person = Person.Person(idp, name, year, gender)
        self.__tree[person.getID()] = person

    def setFather(self, fatherId, childrenId):
        if fatherId <= 0:
            return
        self.__tree[childrenId].setFather(self.__tree[fatherId])

    def setMother(self, motherId, childrenId):
        if motherId <= 0:
            return
        self.__tree[childrenId].setMother(self.__tree[motherId])

    def setCouple(self, person1Id, person2Id):
        if person1Id <= 0:
            return
        self.__tree[person2Id].setCouple(self.__tree[person1Id])

    def search(self, rootId, leafId):
        """ Finds the relationship between two individuals
        Arguments :
        rootID = the person who we are looking at (example son)
        leafId = the person we want to know how they're related (example Father )

        Q = the Queue that stores persons to look at.
        backTracer = dictionary that stores how persons are related.
        """

        if rootId not in self.__tree or leafId not in self.__tree:
            if rootId not in self.__tree:
                print("Error: [FamilyTree]," + rootId + "is not in family")
            else:
                print("Error: [FamilyTree]," + leafId + "is not in family")
            return []  # TODO simplify for error message reasons

    def toString(self):
        stringData = ""
        for key, person in self.__tree.items():
            stringData += person.getbio() + "\n"
        return stringData

    def toListString(self, omitGender=0):
        listData = []
        for key, person in self.__tree.iteritems():
            if person.getGender() != omitGender:
                listData.append(person.getbio() + "\n")
        if len(listData) == 0:
            listData.append("no person to choose")
        return listData


a = FamilyTree(2, "goal")

a.addPerson(1, "cat", 1999, )
