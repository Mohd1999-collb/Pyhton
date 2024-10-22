class Employee:
    def __init__(self, salary, increament):
        self.salary = salary
        self.increament = increament

    @property
    def salaryAfterIncreament(self):
        return self.increament;

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, value):
        if self.salary < 1000 :
            self.increament = value
        elif self.salary  > 1000 :
            self.increament = value + 500
        else :
            self.increament = value + 1000


e = Employee(1100, 200)
e.salaryAfterIncreament = 500
print(e.increament)