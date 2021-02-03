
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.employee import Employee
from package.department import Department
from package.managaError import ManageError
import pickle

def main():
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
    employee_data = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]
    with open("data.txt", "wb") as f:
        pickle.dump(employee_data, f)
    """
    emp_test1 = Employee('Kalaella','davos','F-010105-M','davos@gmail.com','deRitio',60000,'14PM')
    emp_test2 = Employee('Sagmo','Galandrigar','M-101019-O','gala@gmail.com','SgmGa',300000,'15AM')
    
    with open("data.txt", "rb") as f:
        employee_get_data = pickle.load(f)
    
    check_list = []
    for i in employee_get_data:
        check_list.append(i.__dict__)
    if emp_test2.__dict__ not in check_list:
        raise ManageError(emp_test2.__dict__['name'])
    else:
        obj = Department('HHRR', '917000222',employee_get_data)
    
    return obj.employee_report()

main()
