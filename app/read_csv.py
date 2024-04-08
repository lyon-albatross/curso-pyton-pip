import csv

def read_csv(path):
  with open(path,'r') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    data = []
    
    for row in reader:
      iterable = zip(header, row)
      pais_dict = {key: value for key, value in iterable}
      data.append(pais_dict)
    
    return data

if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(len(data))
  print(data[0])
  