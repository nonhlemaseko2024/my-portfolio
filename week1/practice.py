# Practice - OOP Exercise 1
# Nonhle Maseko

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    
    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        #print(f"R{self.salary:,}")
        print(f"{self.name} at {self.department} department earns R{self.salary:,}")

    def get_annual_salary(self):
        annual = self.salary * 12
        return annual

employee1 = Employee("Nonhle Maseko", "Data Engineering", 45000)
employee2 = Employee("Melo Mkhatshwa", "Cloud Infrastructure", 52000)
employee3 = Employee("Lethu Maseko", "BI and Analytics", 38000)
employee1.get_details()
employee2.get_details()
employee3.get_details()
#annual = employee1.get_annual_salary()
#annual = employee2.get_annual_salary()
#annual = employee3.get_annual_salary()
print(f"Annual salary: R{employee1.get_annual_salary():,}")
print(f"Annual salary: R{employee2.get_annual_salary():,}")
print(f"Annual salary: R{employee3.get_annual_salary():,}")