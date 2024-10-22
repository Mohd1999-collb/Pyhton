import math

class Student : 
    # Class attributes or properties
    name = 'Mohan'
    age = 20
    city = 'Rampura'
    salary = 25000

    def __init__(self, name, age, city, salary) :
        self.name = name
        self.age = age
        self.city = city
        self.salary = salary

    def getInfo(self):
        print(f'The student name is {self.name} and age is {self.age} and city is {self.city} and salary is {self.salary}')

    @staticmethod
    def greet():
        print("Good Morning Talib Bhai........")



class Calculator :

    def square(self, n):
        return n**2

    def cube(self, n):
        return math.pow(n, 3)

    def squareRoot(self, n):
        return math.sqrt(n)



st = Student("Rani", 20, "Kanpur", 5000);

# Instance attributes ---> Instance attributes take more preference over class attributes during initialization and retrieval
st.name = 'ShyamDas'


st.getInfo()  #  Student.getInfo(st) is work similar to as st.getInfo()
st.greet()
# Student.getInfo(st)
print(st.name, st.age, st.city, st.salary);

cal = Calculator()
print(cal.square(5))
print(int(cal.cube(5)))
print(int(cal.squareRoot(25)))


