def get_populations(country_dict):
  population_dict = {
    '2023': int(country_dict['2023 population']),
    '2022': int(country_dict['2022 population']),
    '2020': int(country_dict['2020 population']),
    '2015': int(country_dict['2015 population']),
    '2010': int(country_dict['2010 population']),
    '2000': int(country_dict['2000 population']),
    '1990': int(country_dict['1990 population']),
    '1980': int(country_dict['1980 population']),
    '1970': int(country_dict['1970 population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def populations_by_country(data, country):
  result = list(filter(lambda item: item['country'] == country, data))
  return result
  
def get_world_percentages(data):
  world_percentages = {}
  for item in data:
    pais = item['cca3']
    porc = float(item['world percentage'].replace('%',''))
    world_percentages[pais] = porc
  
  return world_percentages
  