
from package.persona import Persona
from package.usuario import Usuario
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia
from pathlib import Path
import csv


def main():

    # yo = Persona('Isabel', 'Repetto', '12-02-1991', '56432865P', "Tailor's Court")
    # print(f'Dia: {yo.getDia()}')
    # print(f'Mes: {yo.getMes()}')
    # print(f'Año: {yo.getAño()}')
    
    # yo.setDia(22)
    # print(f'\nDatos de Persona despues de modificar la fecha de nacimiento:\n{yo}')

    # yo = Usuario('isargp@gmail.com', 'clavecita', False)
    # print(f"Validacion: {yo.validacion('isargp@gmail.com', 'clavecita')}\n")

    
    departamento_programacion = Departamento('Programación Python', '911652637')
    departamento_matematicas = Departamento('Matemáticas', '773284936')
    departamento_diseño = Departamento('Diseño gráfico', '266493817')

    cice = Gerencia('CICE')

    path_prog = Path('C:/Users/Isabel/Documents/PYTHON/MPP/UNIDAD 7/CICE-M-509/empl_programacion.csv')
    path_mat = Path('C:/Users/Isabel/Documents/PYTHON/MPP/UNIDAD 7/CICE-M-509/empl_matematicas.csv')
    path_dis = Path('C:/Users/Isabel/Documents/PYTHON/MPP/UNIDAD 7/CICE-M-509/empl_diseño.csv')

    cargas_pendientes = {departamento_programacion:path_prog,departamento_matematicas:path_mat,departamento_diseño:path_dis}

    cice.carga_empleados(cargas_pendientes)

    cice.muestra_departamentos()

    cice.muestra_empleados()

    # print(f'Media: {departamento_programacion.media_salarial():.2f}\n')
    # print(f'Reporte salarial del departamento "{departamento_programacion.nombre}" ordenado de mayor a menor salario:\n{departamento_programacion.reporte_salarios()}')
    
    # runing = True

    # while runing:
    #     cice.menu_principal()

    #     input('pulse una tecla para continuar')

main()