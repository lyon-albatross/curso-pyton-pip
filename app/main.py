import read_csv
import charts
import utils

def run1():
  data = read_csv.read_csv('./data.csv')
  country = input('Type Country => ')
  result = utils.populations_by_country(data, country)

  if len(result) > 0:
    labels, values = utils.get_populations(result[0])
    # print(labels, values)
    charts.generar_bar_chart(country, labels, values)

def run2():
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item: item['continent'] == 'South America', data))
  
  labels = [item["cca3"] for item in data]
  values = [float(item["world percentage"].replace('%','')) for item in data]
  charts.generar_pie_chart(labels, values)
  # print(regs)
  
if __name__ == '__main__':
  run1()

