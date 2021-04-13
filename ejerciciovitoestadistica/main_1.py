import requests as req
import json
response = req.get("https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json").json()
with open("covid.json", "w") as file:
    json.dump(response, file)
import std
#import matplotlib.pyplot as plt

with open("covid.json") as file:
    json_reader = json.load(file)
    data = json_reader["data"] 
    # result = set([mun["municipio_distrito"] for mun in data]) # 199
    def get_tia(parse):
        result = 0
        for mun in parse:
            try:
                result += mun["casos_confirmados_totales"]
            except KeyError:
                result += 0
        return result
    # first_tia = get_tia(data[-200:-1])
    # last_tia = get_tia(data[0:199])
    # print(last_tia)
    def get_all(dataset):
        result = []
        dates = sorted(set([date['fecha_informe']for date in data])) #sorted ---> ordena los elementos de una lista, set..
        for date in dates:
            inner = 0
            for mun in dataset:
                if mun['fecha_informe'] == date:
                    try:
                        inner += mun['casos_confirmados_totales']
                    except KeyError:
                        inner += 0
            result.append(inner)
        return result
        
    y = get_all(data)
    #y.reverse()
    # print(len(y))
    
    x = [num for num in range(1,128)]
    #print(x)
    #print(y)

    test = std.Statistics(x, y)
    #print(test.y[0])
    print(test.get_prediction(150) - 15000)
    print("r Pearson --> ", test.r_pearson)

    
    #plt.plot(x,y)
    #plt.ylabel(y)
    #plt.show()

    # def get_all_date(dataset, offset, limit = None):
    #     dates = set([date["fecha_informe"] for date in dataset])
    #     result = 0
    #     for date in dates[offset:None]:

    # def get_all_date(dataset, offset, limit = None):
    #     dates = set([date["fecha_informe"] for date in dataset])
    #     result = 0
    #     for date in dates[offset:limit]: