import matplotlib.pyplot as plot
import csv
import re


def read_csv(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      countryDict = {key: value for key, value in iterable}
      data.append(countryDict)
    return data

def obtenerValoresDifPoblacional(data, country):
  dictPoblacional = {}
  for item in data:
    if country == item['Country/Territory']:
      keys = item.keys()
      patron = re.compile('([0-9]+) (Population)')
      for row in keys:
        if patron.search(row):
          dictPoblacional[row] = int(item[row])

  print(dictPoblacional)
  return dictPoblacional.keys(), dictPoblacional.values()

def graficarPoblacion(rows, columns):
  fig, ax = plot.subplots()
  ax.bar(rows, columns)
  plot.show()

def obtenerValoresPorcPoblacional(data):
  dictPorcentajes = {
    item['Country/Territory']: item['World Population Percentage']
    for item in data
  }
  return dictPorcentajes.keys(), dictPorcentajes.values()


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  rows, columns = obtenerValoresPorcPoblacional(data)
  graficarPoblacion(rows, columns)

