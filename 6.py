class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        return f"""Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {round(self.mean(), 1)}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершённые курсы: {', '.join(self.finished_courses)}\n"""

    def mean(self):
        if len(self.grades) == 0:
            return 0
        allgrades = []
        for key in self.grades:
            allgrades.extend(self.grades[key])
        return sum(allgrades) / len(allgrades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.mean() == other.mean()
        return "Несравнимо"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.mean() < other.mean()  
        return "Несравнимо"

    def __le__(self, other):
        return self < other or self == other

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades and grade in range(11):
                lecturer.grades[course] += [grade]
            elif grade in range(11) and course in lecturer.courses_attached:
                lecturer.grades[course] = [grade]
            else:
                return 'Ошибка в оценке'
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    
    def mean(self):
        if len(self.grades) == 0:
            return 0
        allgrades = []
        for key in self.grades:
            allgrades.extend(self.grades[key])
        return sum(allgrades) / len(allgrades)

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.mean() == other.mean()         
        return "Несравнимо"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.mean() < other.mean()
        return "Несравнимо"
    
    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return f"""Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {round(self.mean(), 1)}\n"""


class Reviewer(Mentor):
    def __str__(self):
        return f"""Имя: {self.name}
        Фамилия: {self.surname}\n"""
    
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and grade in range(11):
                student.grades[course] += [grade]
            elif grade in range(11) and course in student.courses_in_progress:
                student.grades[course] = [grade]
            else:
                return 'Ошибка в оценке'
        else:
            return 'Ошибка'

#для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
#для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

# Задание 4
# представимся

# представим студентов
stud1 = Student('Ivanna', 'Ivanova', 'female')
stud2 = Student('Grzegorz', 'Brzęczyszczykiewicz', 'male')
stud1.finished_courses.append('Russian')
stud2.finished_courses.append('Polish')
stud1.courses_in_progress.append('Polish') 
stud2.courses_in_progress.append('Russian')
stud1.courses_in_progress.extend(['Python', 'History'])
stud2.courses_in_progress.extend(['Python', 'History'])
print(stud1, stud2)

# представим лекторов
lect1 = Lecturer('Georg', 'Kantor')
lect2 = Lecturer('Albert', 'Einstein') 
print(lect1, lect2)
lect1.courses_attached = ['History', 'Russian', 'Polish']
lect2.courses_attached = ['Python']

# представим рецензентов
rev1 = Reviewer('Winnie', 'the-Pooh')
rev2 = Reviewer('Sancho', 'Pansa')
print(rev1, rev2)
rev1.courses_attached = ['Polish', 'History', 'Python']
rev2.courses_attached = ['Polish', 'History', 'Russian']

# пооцениваем друг друга

# студенты пооценивали
stud1.rate_lect(lect1, 'Python', 3)
stud1.rate_lect(lect1, 'History', 10)
stud1.rate_lect(lect2, 'Python', 5)
stud2.rate_lect(lect1, 'History', 20)
stud2.rate_lect(lect1, 'Russian', 2)
stud2.rate_lect(lect2, 'Polish', 5)

# рецензенты пооценивали
rev1.rate_st(stud1, 'Physical Education', 10)
rev1.rate_st(stud1, 'Russian', 1)
rev1.rate_st(stud2, 'Russian', 22)
rev2.rate_st(stud2, 'Python', 9.5)
rev2.rate_st(stud2, 'Russian', 4)
rev2.rate_st(stud1, 'Russian', 1)

# посмотрим на оценки, сравним средние баллы
print(stud1.grades)
print(stud2.grades)
print(lect1.grades)
print(lect2.grades)

print(stud1.mean(), stud2.mean())
print(stud1 < stud2)
print(stud1 == stud2)
print(stud1 >= stud2)

print(lect1.mean(), lect2.mean())
print(lect1 >= lect2)
print(lect1 <= lect2)
print(lect1 < lect2)

print("\nСравним лектора и студента:")
print(stud1.mean(), lect2.mean())
print(stud1 >= lect2)
print(stud1 == lect2)
print(stud1 > lect2)
print(stud1 < lect2)

print(stud1, stud2)
print(lect1, lect2)

# реализуем 2 функции:

def hw_mean(*st_list, name):
    fin_list = []
    for person in st_list:
        for key in person.grades:
            if key == name:
                fin_list.extend(person.grades[key])
    if len(fin_list) == 0:
        return 0
    return sum(fin_list) / len(fin_list)

def lct_mean(*lect_list, name):
    fin_list = []
    for person in lect_list:
        for key in person.grades:
            if key == name:
                fin_list.extend(person.grades[key])
    if len(fin_list) == 0:
        return 0
    return sum(fin_list) / len(fin_list)

print(hw_mean(stud1, stud2, name='History'))
print(hw_mean(stud1, stud2, name='Python'))
print(lct_mean(lect1, lect2, name='Python'))
print(lct_mean(lect1, lect2, name='Russian'))

