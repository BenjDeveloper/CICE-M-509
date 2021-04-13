import requests as req
import json
# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/877fa8f5-cd6c-4e44-9df5-0fb60944a841/download/covid19_tia_muni_y_distritos_s.json").json()
# with open("covid_2.json", "w") as file:
#     json.dump(response, file, indent=4)

import std
import matplotlib.pyplot as plt

with open("covid_2.json") as file:
    json_reader = json.load(file)
    data = json_reader["data"] 
    dates = sorted(set([date['fecha_informe']for date in data]))
    a = list(filter(lambda mun:mun['fecha_informe'] == '2021/04/06 11:56:00', data))

    def get_all(dataset, dateset):
        result = []
        for date in dateset:
            inner = 0
            for mun in dataset:
                if mun['fecha_informe'] == date:
                    try:
                        inner += mun['casos_confirmados_totales']
                    except KeyError:
                        inner += 0                        
            result.append(inner)
        return result

    y1 = get_all(data, dates)
    x1 = [num for num in range(0,len(y1))]

    test = std.Statistics(x1, y1)
    print(x1)
    print(y1)

    print(test.get_prediction(150) - 15000)
    print("r Pearson --> ", test.r_pearson)

    plt.plot(x1,y1)
    # plt.ylabel()
    plt.show()