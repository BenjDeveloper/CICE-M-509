import requests as req
import json
import std
import matplotlib.pyplot as plt

response = req.get("https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json").json()
with open("covid_3.json", "w") as file:
    json.dump(response, file, indent=4)


#? 1-De ser factible, modificar las propiedades del objeto statistics con algún built-in method
#? 2-Crear un json con los valores obtenidos en la request
#? 3-Establecer dos muestras una desde el inicio del dataset hasta 2005 inclusive y otra desde 2006 en adelante
#? 4-Obtener la proporción de todos los tipos de pareja
#? 5-Obtener la proporción año a año de parejas heterosexuales y parejas homosexuales
#? 6-Obtener valor B
#? 7-Considerar si es "aplicable" o no el estadístico de correlación "R" y en tal caso calcularlo
#? 8-Graficar el ejercicio 4 y ejercicio 5 (este último solo si es lineal)
#? 9-Es la diferencia del porcentaje de parejas homosexuales estadisticamente significativa?
#? 10-Con qué probabilidad?



with open("covid_3.json") as file:
    json_reader = json.load(file)
    data = json_reader["data"] 
    
#? 3-Establecer dos muestras una desde el inicio del dataset hasta 2005 inclusive y otra desde 2006 en adelante

    fecha_tope = '2010'
    a = list(filter(lambda par:par["inscripcion_a\u00f1o"] <= fecha_tope, data))
    b = list(filter(lambda par:par["inscripcion_a\u00f1o"] >= fecha_tope, data))
    a_n = sum(list(map(lambda par: int(par["num_inscripciones"]), a)))
    b_n = sum(list(map(lambda par: int(par["num_inscripciones"]), b)))
    
    # print(a_n)
    # print(b_n)
    # print(len(a))
    # print(len(b))

    #? 4-Obtener la proporción de todos los tipos de pareja   

    he_a = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'heterosexual' else 0, a)))
    hom_a = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'homosexual masculina' else 0, a)))
    hof_a = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'homosexual femenina' else 0, a)))
    
    porcentaje_heterosexual_a = he_a*100/a_n
    porcentaje_homosexual_masculina_a = hom_a*100/a_n
    porcentaje_homosexual_femenina_a = hof_a*100/a_n

    # print(f"El porcentaje de Heterosexuales en el grupo A es de: {porcentaje_heterosexual_a:.2f}%")
    # print(f"El porcentaje de Homosexuales masculinos en el grupo A es de: {porcentaje_homosexual_masculina_a:.2f}%")
    # print(f"El porcentaje de Homosexuales femeninos en el grupo A es de: {porcentaje_homosexual_femenina_a:.2f}%")


    he_b = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'heterosexual' else 0, b)))
    hom_b = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'homosexual masculina' else 0, b)))
    hof_b = sum(list(map(lambda par:int(par['num_inscripciones']) if par['pareja_tipo'] == 'homosexual femenina' else 0, b)))

    porcentaje_heterosexual_b = he_b*100/b_n
    porcentaje_homosexual_masculina_b = hom_b*100/b_n
    porcentaje_homosexual_femenina_b = hof_b*100/b_n

    # print(f"El porcentaje de Heterosexuales en el grupo B es de: {porcentaje_heterosexual_b:.2f}%")
    # print(f"El porcentaje de Homosexuales masculinos en el grupo B es de: {porcentaje_homosexual_masculina_b:.2f}%")
    # print(f"El porcentaje de Homosexuales femeninos en el grupo B es de: {porcentaje_homosexual_femenina_b:.2f}%")

    # print(he_a)
    # print(hom_a)
    # print(hof_a)
    # print(he_b) 

    # labels = 'Heterosexual', 'Homosexual Masculino', 'Homosexual Femenino'
    # sizes = [porcentaje_heterosexual_a, porcentaje_homosexual_masculina_a, porcentaje_homosexual_femenina_a]
    # explode = (0, 0.1, 0)

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode= explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')

    # plt.show()


    #? 5-Obtener la proporción año a año de parejas heterosexuales y parejas homosexuales

    dates = sorted(set(map(lambda par: par['inscripcion_año'], data)))

    def by_year(given_list):
        dates = sorted(set(map(lambda par: par['inscripcion_año'], given_list)))
        hetero_list = []
        homomas_list = []
        homofem_list = []
        for year in dates:
            hetero = sum(list(map(lambda par:int(par['num_inscripciones']) if par['inscripcion_año'] == year and par['pareja_tipo'] == 'heterosexual' else 0, given_list)))
            homomas = sum(list(map(lambda par:int(par['num_inscripciones']) if par['inscripcion_año'] == year and par['pareja_tipo'] == 'homosexual masculina' else 0, given_list)))
            homofem = sum(list(map(lambda par:int(par['num_inscripciones']) if par['inscripcion_año'] == year and par['pareja_tipo'] == 'homosexual femenina' else 0, given_list)))
            hetero_list.append((hetero, year))
            homomas_list.append((homomas, year))
            homofem_list.append((homofem, year))
        # print(hetero_list, homomas_list, homofem_list)
        return hetero_list, homomas_list, homofem_list

    hetero_list2010, homomas_list2010, homofem_list2010 = by_year(a)
    hetero_list_total, homomas_list_total, homofem_list_total = by_year(data)

    # print(homomas_list2010)

    hetero_y = list(map(lambda par: par[0],hetero_list_total))
    homomas_y = list(map(lambda par: par[0], homomas_list_total))
    homofem_y = list(map(lambda par: par[0], homofem_list_total))    
    years_x = list(map(lambda par: par[1], hetero_list_total))


    print(hetero_y)

    


    # plt.plot(years_x,hetero_y,'y--', label= 'Heterosexual')
    # plt.plot(years_x,homomas_y,'m--', label= 'Homosexual masculino')
    # plt.plot(years_x,homofem_y,'b--', label= 'Homosexual femenino')
    # # plt.ylabel()
    # plt.legend()
    # plt.show()

    



    # def heterosexual_year_a(a):
    #     result = []
    #     dates = sorted(set([date["inscripcion_a\u00f1o"]for date in a]))
    #     for date in dates:
    #         inner = 0
    #         for par in a:
    #             if par["inscripcion_a\u00f1o"] == date:
    #                 if par["pareja_tipo"] == 'heterosexual':
    #                     inner +=1
    #         result.append(inner)
    #     return result

    # # print(heterosexual_year_a(a))

    # def heterosexual_year_b(b):
    #     result = []
    #     dates = sorted(set([date["inscripcion_a\u00f1o"]for date in b]))
    #     for date in dates:
    #         inner = 0
    #         for par in b:
    #             if par["inscripcion_a\u00f1o"] == date:
    #                 if par["pareja_tipo"] == 'heterosexual':
    #                     inner +=1
    #         result.append(inner)
    #     return result

    # # print(heterosexual_year_b(b))

    # by_year(a)
    # hetero_a, homomas_a, homofem_a = divide(a)
    # hetero_b, homomas_b, homofem_b = divide(b)

    # print((homomas_a + homofem_a)/a_n)
    # print((homomas_b + homofem_b)/b_n)





