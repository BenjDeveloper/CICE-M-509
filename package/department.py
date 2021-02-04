


#6.- Create a class Department with the next attributes:
#    name:str
#    telephone number: str
from .employee import Employee

class Department:
    average = 0
    employee_dic = {}
    def __init__(self, name, telephone_number, employee_list):
        self.name = name
        self.telephone_number = telephone_number
        self.employee_list = employee_list
        #self.employee_dic = [i.__dict__['name'] = i.__dict__['salary'] for i in employee_list]
        for i in self.employee_list:
            self.employee_dic[i.__dict__['name']] = i.__dict__['salary']


    
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

"""
emp1 = Employee('Ava','Lord','F-010101-M','ava@gmail.com','AVALORD',35000,'10PM')
emp2 = Employee('Beast','Gard','M-101010-O','beas@gmail.com','bestCard',30000,'09PM')
emp3 = Employee('Cargan','Vex','M-101011-O','car@gmail.com','carGan',40000,'10AM')
emp4 = Employee('Della','Sart','F-010102-M','della@gmail.com','deSart',60000,'10PM')
emp5 = Employee('Ember','War','F-010103-M','ember@gmail.com','wArem',20000,'10AM')
emp6 = Employee('Eternity','Vargard','F-010104-M','bart@gmail.com','AkirIdIOn',30000,'11AM')
emp7 = Employee('Barbatos','Vex','M-101012-O','true@gmail.com','VeritY',39000,'09AM')
emp8 = Employee('Drax','Berigan','M-101013-O','berg@gmail.com','Eternium',55000,'11AM')
emp9 = Employee('Kalaella','davos','F-010105-M','davos@gmail.com','deRitio',60000,'14PM')
emp10 = Employee('Balika','Versus','F-010106-M','vers@gmail.com','Warrior',25000,'15AM')

obj = Department('HHRR', '917000222',[emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10])

print(obj.average_salary())
print(obj.employee_report())
"""





























