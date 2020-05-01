from core.Person import *
import copy


class FamilyTree:
    def __init__(self, idf, family_name):
        self.__idFamily = idf
        self.__familyName = family_name
        self.__tree = {}

    def lookup_person(self, idp):
        return copy.deepcopy(self.__tree[idp])

    def add_person(self, idp, name, year, gender):
        person = Person(idp, name, year, gender)
        self.__tree[person.get_id()] = person

    def set_father(self, fatherId, childrenId):
        if fatherId <= 0:
            return
        self.__tree[childrenId].set_father(self.__tree[fatherId])

    def set_mother(self, motherId, childrenId):
        if motherId <= 0:
            return
        self.__tree[childrenId].set_mother(self.__tree[motherId])

    def set_couple(self, person1Id, person2Id):
        if person1Id <= 0:
            return
        self.__tree[person2Id].set_couple(self.__tree[person1Id])

    def search(self, rootId, leafId):
        if rootId not in self.__tree or leafId not in self.__tree:
            print("Error: [FamilyTree] Person is not in family")
            return []

        # perform BFS to find the relationship with 2 persons
        result = []
        back_tracer = {}
        Q = [rootId]
        history = []
        while len(Q) > 0:
            nodeId = Q.pop()
            history.append(nodeId)

            # current person is the interested person
            if nodeId == leafId:
                # trace back to find a relationship path, continue to search another path
                p = back_tracer[leafId]
                relationship = [(leafId, RELATIONSHIP.IS_NULL), p]
                while p[0] != rootId:
                    p = back_tracer[p[0]]
                    relationship.append(p)
                result = relationship
                break

            # search in his/her couples
            for coupleID in self.__tree[nodeId].get_couple_i_ds():
                if coupleID is not None and coupleID not in history:
                    Q.append(coupleID)
                    if self.__tree[nodeId].get_gender() == Gender.MALE:
                        back_tracer[coupleID] = (nodeId, RELATIONSHIP.IS_HUSBAND)
                    else:
                        back_tracer[coupleID] = (nodeId, RELATIONSHIP.IS_WIFE)

            # search in his/her children
            for childrenID in self.__tree[nodeId].get_child_i_ds():
                if childrenID is not None and childrenID not in history:
                    Q.append(childrenID)
                    if self.__tree[nodeId].get_gender() == Gender.MALE:
                        back_tracer[childrenID] = (nodeId, RELATIONSHIP.IS_FATHER)
                    else:
                        back_tracer[childrenID] = (nodeId, RELATIONSHIP.IS_MOTHER)

            # search in his/her father
            fatherID = self.__tree[nodeId].get_father_id()
            if fatherID not in history and fatherID is not None:
                Q.append(fatherID)
                back_tracer[self.__tree[nodeId].get_father_id()] = (nodeId, RELATIONSHIP.IS_CHILDREN)

        # [TODO] after find a path, post process to find the shortest path

        return result

    # TODO rename this function it will cause a conflict in the future
    def toString(self):
        string_data = ""
        for key, person in self.__tree.items():
            string_data += person.to_string() + "\n"
        return string_data

    def toListString(self, omitGender=0):
        list_data = []
        for key, person in self.__tree.iteritems():
            if person.get_gender() != omitGender:
                list_data.append(person.to_string() + "\n")
        if len(list_data) == 0:
            list_data.append("no person to choose")
        return list_data
