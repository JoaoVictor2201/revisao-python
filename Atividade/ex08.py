import requests

def fetchCountry(country):
  url = f'https://restcountries.com/v3.1/name/{country}'
  response = requests.get(url)
  data = response.json()[0]

  print(f'Nome do país: {data['name']['common']}')

  countryLangs = list(data.get('languages').values())
  print(f"Linguagens: {', '.join(countryLangs)}")
  
  print(f'Região: {data['region']}')
  print(f'Sub-Região: {data.get('subregion', 'Não disponivel')}')
  print(f'Capital: {data['capital'][0]}')

  currencies = data['currencies']
  if currencies:
    currency = list(currencies.keys())[0]
    currencyInfo = currencies[currency]
    print(f"Sigla da Moeda: {currency}")
    print(f"Nome da Moeda: {currencyInfo.get('name', 'Não disponível')}")
    print(f"Símbolo da Moeda: {currencyInfo.get('symbol', 'Não disponível')}")
  else:
    print("Informações de moeda indisponíveis")

  borders = data['borders']
  print(f"Fronteiras: {', '.join(borders)}")

print('=== Informações sobre Países ===')
country = input('Insira o nome de um país: ')
fetchCountry(country)