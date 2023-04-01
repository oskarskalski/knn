import pandas as pd
import matplotlib.pyplot as plt

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
    x = a['x'] - b['x']
    y = a['y'] - b['y']
    return (x**2 + y**2)**(1/2)


def classify_object(arr):
    pass

def calculate_percent_of_domination(arr):
    objects = {}
    sum = len(arr)
    for i in arr:
        obj_class = i[0]['class']
        if obj_class not in objects:
            objects[obj_class] = [1]
        else:
            objects[obj_class].append(1)
    results = {}
    for i in objects:
        results[i] = len(objects[i])/sum
    print(results)
    return max(results, key=lambda k: results[k])
    
def average_wage(arr):
    max(arr, key=lambda k: arr[k])

def main():
    chart = {}
    object = {
        'x': 4,
        'y': 5.5
    }
    results = knn(object, 150)
    print(calculate_percent_of_domination(results))
    for i in results:
        obj_class = i[0]['class']
        if obj_class not in chart:
            chart[obj_class] = {
                'x': [],
                'y': []
            }
        chart[obj_class]['x'].append(i[0]['x'])
        chart[obj_class]['y'].append(i[0]['y'])

    for key in chart:
        x = chart[key]['x']
        y = chart[key]['y']
        plt.plot(x, y, 'o')
    
    plt.plot(object['x'], object['y'], 'o')

    plt.show()


main()