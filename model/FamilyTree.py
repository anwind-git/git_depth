humanList = []


def add(Person):
    humanList.append(f"{Person.id} {Person.name} {Person.middle_name} Год рождения: {Person.age} Пол: {Person.gender} "
                   f"Отец: {Person.father} Мать: {Person.mother} Супруг(а): {Person.spouse} Дети: {Person.children}")


def openList():
    for i in humanList:
        print(i)
