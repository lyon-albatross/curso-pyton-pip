import matplotlib.pyplot as plt

def generar_bar_chart(country, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{country}_bar.png")
  plt.close()

def generar_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig("pie.png")
  plt.close()

if __name__ == '__main__':
  labels = ['Enero','Febrero','Marzo']
  values = [20,278,333]
  #generar_bar_chart(labels, values)
  generar_pie_chart(labels, values)
  
