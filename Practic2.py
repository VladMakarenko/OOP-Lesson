class Employee:
    def __init__(self, first_name, last_name, email, phone, ZP):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.ZP = ZP

    @staticmethod
    def work():
        return "I come to the office"


    def check_salary(self, day):
        ZP_day = self.ZP * day
        return ZP_day


class Recruiter(Employee):
    position = "Recruiter"

    def __str__(self):
        return f'{self.position}: {self.first_name, self.last_name}'

    @staticmethod
    def work():
        return "I come to the office and start hiring"


class Programmer(Employee):
    position = "Programmer"

    def __str__(self):
        return f'{self.position}: {self.first_name, self.last_name}'

    @staticmethod
    def work():
        return "I come to the office and start coding"



a = Recruiter("Ivanov", "Ivan", "asd@gmail", "911", 1000)
b = Programmer("Petrov", "Petr", "adasdasda@gmail", "102", 1000)

print(b.check_salary(10))
print(a.check_salary(10))

print(a.work())

print(b.work())