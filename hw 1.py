class person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"{self.fullname}, {self.age}, {self.is_married}")


class Student(person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def fresh(self):
        print(sum(self.marks) / len(self.marks))


class Teache(person):
    salary = 100

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def cash(self):
        if self.experience >= 3:
            sal = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return sal


t = Teache("Adi", 30, "not", True)
print(f"{t.fullname}, {t.age}, {t.is_married}, {t.salary}")
print(t.cash())


def create_students():
    s = Student("Aza", 18, "not", marks={
        "истроия": 4,
        "физра": 5,
        "алебра": 3
    })
    j = Student("jacks", 20, "yes", marks={
        "истроия": 5,
        "физра": 5,
        "алебра": 2
    })
    d = Student("Azi", 15, "not", marks={
        "истроия": 5,
        "физра": 2,
        "алебра": 5
    })

    k = [s, j, d]
    return k


a = create_students()
for i in a:
    s = []
    for marks in i.marks.values():
        s.append(marks)
    print(f"Name:{i.fullname}\n"
          f"Age:{i.age}\n"
          f"Marriage:{i.is_married}\n"
          f"Average:{sum(s) / len(s)}\n")