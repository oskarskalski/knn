import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def knn(object_to_classify, k):
    results = []
    df = pd.read_csv('bezdekIris.csv')
    for index, row in df.iterrows():
        object = {
            'x': row.get('sepal_width'),
            'y': row.get('sepal_length'),
            'class': row.get('class')
        }
        results.append((object, calculateDistance(object, object_to_classify)))
    sorted_list = sorted(results, key=lambda x: x[1])
    return sorted_list[:k]



def calculateDistance(a, b):
    x = abs(a['x'] - b['x'])
    y = abs(a['y'] - b['y'])
    return x**2 + y**2



object = {
    'x': 4,
    'y': 5.5
}

results = knn(object, 50)
chart = {

}

for i in results:
    obj_class = i[0]['class']
    if obj_class not in chart:
        chart[obj_class] = {
            'x': [],
            'y': []
        }
    chart[obj_class]['x'].append(i[0]['x'])
    chart[obj_class]['y'].append(i[0]['y'])

print(chart)
for key in chart:
    x = chart[key]['x']
    y = chart[key]['y']
    plt.plot(x, y, 'o')

plt.plot(object['x'], object['y'], 'o')

plt.show()