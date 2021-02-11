


#6.- Create a class Department with the next attributes:
#    name:str
#    telephone number: str
from .employee import Employee

class Department:
    average = 0
    employee_dic = {}
    def __init__(self, name, telephone_number, employee_list=None):
        self.name = name
        self.telephone_number = telephone_number
        self.employee_list = employee_list
        if employee_list != None:
            for i in self.employee_list:
                self.employee_dic[i.__dict__['name']] = i.__dict__['salary']
        else:
            pass

    def average_salary(self):
        salary_list = list(self.employee_dic.values())
        length = len(salary_list)
        self.average = sum(salary_list) / length
        return f"The mean salary is {self.average}"

    def employee_report(self):
        salary = list(self.employee_dic.values())
        salary.sort()
        salary.reverse()
        print('Employee', '\t', 'Salary')
        print('.....','\t\t','....')
        for k in salary:
            name = list(self.employee_dic.keys())[list(self.employee_dic.values()).index(k)]
            if len(name) > 6:
                print(name, '\t', k)
            else:
                print(name, '\t\t', k)
        print('======================')
        return 'this is the employee report'
        

    def __str__(self):
        return f" The average salary of this department: {self.average}"




























