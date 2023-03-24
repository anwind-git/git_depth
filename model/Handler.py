import pickle
from model import Person, FamilyTree


class Handler:
    def save(self):
        f = open("dynasty.txt", "wb")
        for i in FamilyTree.humanList:
            pickle.dump(i, f)
        f.close()

    def read(self):
        f = open("dynasty.txt", "rb")
        d = pickle.load(f)
        print(d)
        f.close()
