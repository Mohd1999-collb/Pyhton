class Employee :

    employee = "Mahesh"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee_info(self, m=0):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Value of m is : {m}")


class User :

    user = "Sagar"
    def __init__(self, name, age, salary, role):
        self.role = role
        super().__init__(name, age, salary)

    def display_user_info(self):
        print(f"Role: {self.role}")
# Multiple Inheritance
class Company(User, Employee):
    company = "Oex Technologies"

    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary, role)

    def display_company_info(self):
        self.display_employee_info(25000)
        self.display_user_info()


# Create objects

com = Company("Ram", 25, 100000, "Manager")
com.display_company_info()
print(com.company, com.user, com.employee)


class Animal:
    a = "Dog"
    def __init__(self, n):
        self.n = n

    @classmethod
    def showAnimal(cls):
        print(f"Animal name {cls.a}")

    # Getter of age
    @property 
    def age(self):
        return self.animalAge
    
    # Setter of age
    @age.setter 
    def age (self,value):
        self.animalAge = value

    # Operator overloading
    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n
    


obj = Animal(15)
obj1 = Animal(20)
obj.a = "Cat"
obj.showAnimal()
obj.age = 25
print(obj + obj1)
print(obj1 - obj)
print(obj.animalAge)


class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        print(f"Magnitude of 2dVector is : {self.x}x + {self.y}y")

class ThreeDVector(TwoDVector) :
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def magnitude(self):
        super().magnitude()  # Call to TwoDVector's magnitude method
        print(f"Magnitude of 3dVector is : {self.x}x + {self.y}y + {self.z}z")

vector = ThreeDVector(4, 5, 6)
vector.magnitude();