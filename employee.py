class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52 #theres 52 weeks in a year, it calculates the estimated paycheck for a week.
    
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, weekly_hours, hourly_rate):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate 
    
    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, first_name, last_name, salary, sales_num, com_rate):
        super().__init__(first_name, last_name, salary)
        self.sales_num = sales_num 
        self.com_rate = com_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary + total_commission
        