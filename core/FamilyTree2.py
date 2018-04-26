import core.Person as Person
import copy

class FamilyTree:
    """ Creates persons in the using the Person class. Stores their ID in the
    self.__tree dectionary, the ID is the key and the value is the instance of
    the person class, all all interactions betweeen individuals take place in
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

        # perform BFS to find the relationship with 2 persons
        result = []
        backTracer = {}
        Q = [rootId]
        print("first things first  ", Q)
        history = []
        while len(Q) > 0:
            print("\nthis is the length of Q", "---", len(Q), ",", Q, )
            nodeId = Q.pop()
            print("this is node", nodeId)
            history.append(nodeId)
            print("this is currently history", history)

            # TODO recode this section of the function
            # current person is the interested person
            if nodeId == leafId:
                print(" nodeId == leafId", nodeId, leafId)
                # trace back to find a relationship path, continue to search another path
                print("this is leafId ", leafId)
                p = backTracer[leafId]
                print("this is p ", p)
                relationship = [(leafId, Person.RELATIONSHIP.IS_NULL), p]
                print("this is relationship", relationship)
                while p[0] != rootId:
                    print("p[0] is,", p[0])
                    p = backTracer[p[0]]
                    print("this is backTracer[p[0]] ", p)
                    relationship.append(p)
                    print("new relationship", relationship)
                result = relationship
                print('this is the result ', result)
                break

            # search in his/her coupleID attribute
            # determines if 'nodeId' is the husband or wife of the person in the coupleID attribute  '
            for coupleID in self.__tree[nodeId].getCoupleIDs():
                # print("  current the couple id list",len(self.__tree[nodeId].getCoupleIDs()))
                if coupleID is not None and coupleID not in history:
                    print("the couples ID ", coupleID)
                    Q.append(coupleID)
                    print("the is Q coupleID ,", Q)
                    if self.__tree[nodeId].getGender() == Person.GENDER.MALE:
                        backTracer[coupleID] = (nodeId, Person.RELATIONSHIP.IS_HUSBAND)
                        print('this is backTracer if coupleID  --husband--', backTracer)
                    else:
                        backTracer[coupleID] = (nodeId, Person.RELATIONSHIP.IS_WIFE)
                        print('this is backTracer if coupleID  --wife--', backTracer)

            # search in his/her children
            # determines if 'nodeId' is the father or mother of the person(s) in the childrenID attribute  '
            for childrenID in self.__tree[nodeId].getChildIDs():
                if childrenID is not None and childrenID not in history:
                    print("the children ", childrenID)
                    Q.append(childrenID)
                    print("the is Q children ", Q)
                    if self.__tree[nodeId].getGender() == Person.GENDER.MALE:
                        backTracer[childrenID] = (nodeId, Person.RELATIONSHIP.IS_FATHER)
                        print('this is backTracer if childrenID --father--', backTracer)
                    else:
                        backTracer[childrenID] = (nodeId, Person.RELATIONSHIP.IS_MOTHER)
                        print('this is backTracer if childrenID --mother--', backTracer)

            # search in his/her father
            # determines if 'nodeId' is the child of the person(s) in the FatherID attribute  '

            fatherID = self.__tree[nodeId].getFatherID()
            motherID = self.__tree[nodeId].getMothreID()
            if fatherID is not None and fatherID not in history:
                Q.append(fatherID)
                print("the is Q FatherID", Q)
                backTracer[fatherID()] = (nodeId, Person.RELATIONSHIP.IS_CHILDREN)
                print('this is backTracer if fatherID --child--', backTracer)

            elif motherID is not None and motherID not in history:
                Q.append(motherID)
                print("the is Q MotherID", Q)
                backTracer[motherID()] = (nodeId, Person.RELATIONSHIP.IS_CHILDREN)
                print('this is backTracer if motherID --child--', backTracer)

        # [TODO] after find a path, post process to find the shortest path

        return result

    def toString(self):
        stringData = ""
        for key, person in self.__tree.items():
            stringData += person.toString() + "\n"
        return stringData

    def toListString(self, omitGender=0):
        listData = []
        for key, person in self.__tree.iteritems():
            if person.getGender() != omitGender:
                listData.append(person.toString() + "\n")
        if len(listData) == 0:
            listData.append("no person to choose")
        return listData





a = FamilyTree(2,"goal")

a.addPerson(1,"cat",1999,)
