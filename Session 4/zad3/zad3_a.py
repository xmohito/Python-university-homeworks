class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def calculate_salary_increase(self, percentage):
        increase_amount = self.salary * (percentage / 100)
        self.salary += increase_amount

    def update_personal_info(self, new_first_name, new_last_name):
        self.first_name = new_first_name
        self.last_name = new_last_name

    def display_employee_info(self):
        print(f"Name: {self.first_name}, Surname: {self.last_name}, Salary: {self.salary}")


employee1 = Employee("John", "Smith", 8000)
employee1.display_employee_info()


employee1.calculate_salary_increase(10)
employee1.update_personal_info("Tonny", "Sosa")
employee1.display_employee_info()