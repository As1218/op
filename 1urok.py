# """ Абстракция """


# class Vehicle: 
#     def start_engine(self):
#         pass
    
#     def stop_engine(self):
#         pass 
    
#     def drivee(self):
#         pass 
    
# class Car(Vehicle)  :
#     def start_engine(self) :
#         return "двигатель автомобиле заведен"    
    
#     def stop_engine(self):
#         return "Двигатель автомобиля не заведен"
    
#     def drivee(self):
#         return "автомобиль едет"
    
# class Bycycle(Vehicle):
#     def start_engine(self):
#         return "у велосипеда нет двигатель"

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return 0

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.2

class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * (0.5 * self.hours_worked)

def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"Calculated Salary: {salary}")
    
full_time_employee = FullTimeEmployee("Alice", 3000)
part_time_employee = PartTimeEmployee("Bob", 2000, 20)
process_salary(full_time_employee)
process_salary(part_time_employee)


$ git config --global user.name "As1218"
$ git config --global user.email asadillo1218@gmail.com