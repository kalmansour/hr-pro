from datetime import date

class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    
    def get_working_years(self):
        return date.today().year - self.employment_year
    
    def __str__(self):
        return f"Name: {self.name},Age: {self.age}, Salary: {self.salary}, Employement Year: {self.employment_year}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    
    def get_working_years(self):
        return date.today().year - self.employment_year
    
    def get_bonus(self):
        bonus = self.bonus_percentage * self.salary
        return bonus
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age}, Salary: {self.salary}, Employement Year: {self.employment_year}, Bonus Percentage: {self.bonus_percentage}"
        
def main():
    employees = []
    managers = []
    print('Welcome to HR Pro 2022')
    while True:
        print("Options:\n1. Show Employees \n2. Show Managers\n3. Add An Employee\n4. Add A Manager\n5. Exit")
        hr_option = int(input("What would you like to do?:"))
        print('-----------------')
        if hr_option == 5:
            break
        elif hr_option == 1:
            print(employees)
        elif hr_option == 2:
            print(managers)
        elif hr_option == 3:
            name = input("Name:")
            age = int(input("Age:"))
            salary= int(input("Salary:"))
            employment_year = int(input("Employment_year:"))
            x = Employee(name, age, salary, employment_year)
            employees.append(x.__str__())
            print('Employee added succesfully\n')
        elif hr_option == 4:
            name = input("Name:")
            age = int(input("Age:"))
            salary= int(input("Salary:"))
            employment_year = int(input("Employment year:"))
            bonus_percentage = int(input("Bonus percentage:"))
            y = Manager(name, age, salary, employment_year,bonus_percentage)
            managers.append(y.__str__())
            print('Manager added succesfully\n')
        else:
            print('invalid number choice')


if __name__ == '__main__':
	main()
