# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.



# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class ClassRoom:
    def __init__(self, class_room):
        self.class_room = class_room

class Person:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def get_ini_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.father_name[0].upper())


class Student(Person):
    def __init__(self, name, surname, father_name, class_room, father, mother):
        Person.__init__(self, name, surname, father_name)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_ini_name(), self.mother.get_ini_name()

class Teacher(Person):
    def __init__(self, name, surname, father_name, classes, subject):
        Person.__init__(self, name, surname, father_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes

# задаем данные


class_rooms = ['5А', '6А', '7А', '8А', '9А']

parents = [Person("Иван", "Петров", "Александрович"),
           Person("Татьяна", "Петрова", "Александровна"),
           Person("Игорь", "Сидоров", "Александрович"),
           Person("Оксана", "Сидорова", "Александровна"),
           Person("Виталий", "Иванов", "Александрович"),
           Person("Милана", "Иванова", "Александровна")]

students = [Student("Александр", "Иванов", "Витальевич", class_rooms[2], parents[4], parents[5]),
            Student("Александра", "Иванова", "Витальевна", class_rooms[0], parents[4], parents[5]),
            Student("Петр", "Сидоров", 'Игоревич', class_rooms[1], parents[2], parents[3]),
            Student("Октябрина", "Сидорова", 'Игоревна', class_rooms[3], parents[2], parents[3]),
            Student("Иван", "Петров", 'Иванович', class_rooms[4], parents[0], parents[1]),
            Student("Илона", "Петрова", 'Ивановна', class_rooms[2], parents[0], parents[1])]

teachers = [Teacher("Феофан", "Грек", "Батькович", [class_rooms[0], class_rooms[1]], 'Русский язык'),
            Teacher("Андрей", "Зырянов", "Александрович", [class_rooms[2], class_rooms[1]], 'История'),
            Teacher("Ульянв", "Харитонова", "Яковлевна", [class_rooms[3], class_rooms[4]], 'Литература')]

        # 1. Получить полный список всех классов школы
print('Полный список всех классов школы: ')
print('class_rooms ', class_rooms)

        # 2. Получить список всех учеников в указанном классе
        #  (каждый ученик отображается в формате "Фамилия И.О.")
print("Список всех учеников в указанном классе: ")
for num, student in enumerate(students, start=1):
    print("{}) {} класс: {}".format(num, student.get_ini_name(), student.class_room))

    # 3. Получить список всех предметов указанного ученика
    #  (Ученик --> Класс --> Учителя --> Предметы)

student = students[0]
t_list = [val for val in teachers if student.get_class_room() in val.get_classes()]
t_names = [val.get_ini_name() for val in t_list]
subj = [val.get_subject() for val in teachers]
print(student.get_ini_name() + ' --> ' + student.get_class_room() + ' --> ' + ' '.join(map(str, t_names)) + '--> ' + ' '.join(map(str, subj)))

    # 4. Узнать ФИО родителей указанного ученика
st_parents = student.get_parents()
print('Родители ученика ', student.get_ini_name(), ' ', st_parents)

    # 5. Получить список всех Учителей, преподающих в указанном классе
print('Учителя, преподающие в классе:')
for num, teacher in enumerate(teachers, start=1):
    print("{}) {} класс: {}".format(num, teacher.get_ini_name(), teacher.classes))
