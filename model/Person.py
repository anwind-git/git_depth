
from model import Gender, FamilyTree


class Person:
    def __init__(self, id, name=None, middle_name=None, age=None, gender=None, father=None, mother=None, spouse=None, children=None):
        self.set_data(id, name, middle_name, age, gender, father, mother, spouse, children)


    def set_data(self, id, name=None, middle_name=None, age=None, gender=None, father=None, mother=None, spouse=None, children=None):
        self.id = id
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.gender = gender
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.children = children

    def get_data(self):
        print(self.id, self.name, self.middle_name, "Год рождения:", self.age, "Пол:", self.gender, "Отец:",
              self.father,
              "Мать:", self.mother, "Супруг(а):", self.spouse, "Дети:", self.children)


FamilyTree.add(Person(1, "Михаил", "Федорович", 1596, Gender.male(), None, None, "Евдокия Лукьяновна Стрешнева", "Алексей Михайлович"))
FamilyTree.add(Person(2, "Евдокия", "Лукьяновна (Стрешнева)", 1608, Gender.female(), None, None, "Михаил Федорович", "Алексей Михайлович"))
FamilyTree.add(Person(3, "Алексей", "Михайлович", 1629, Gender.male(), "Михаил Федорович", "Евдокия Лукьяновна (Стрешнева)", "Мария Ильинична Милославская, Наталья Кирилловна Нарышкина", None))
FamilyTree.add(Person(4, "Мария", "Ильинична (Милославская)", 1625, Gender.female(), None, None, "Алексей Михайлович", None))
