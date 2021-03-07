import requests
import json
import random
from requests.api import request
from pprint import pprint
from dao import DataAccessObject
from time import sleep

dao = DataAccessObject()

# Lista global
lista_cabecalho = []


def obtem_cidades():
    cursor = dao.get_cidades(dao)
    lista_cidades = []

    # Percorre todas as linhas do pyodbc.row e obtém o código_cidade, cidade e pais
    for row in cursor:
        lista_cidades.append([row[0], row[1], row[3]])

    return lista_cidades        



def executa_url(lista_cidade):
    global lista_cabecalho
    
    # Iterar sobre a URL e passar a cidade e o pais, mas excutar o SLEEP para não sobrecarregar a API
    codigo_cidade = lista_cidade[0]
    cidade = lista_cidade[1]
    pais = lista_cidade[2]
    # Lista com as cidades e paises
    lista_cabecalho.append([codigo_cidade, cidade, pais])
    # Adicionei o sleep para que o tempo de chamadas da API não sejam iguais, evitando bloqueio e sobrecarga da api
    #sleep(random.randint(3,5))
    url = f'https://nominatim.openstreetmap.org/search.php?city={cidade}&country={pais}&polygon_geojson=1&limit=1&format=jsonv2'

    try:
        # Obtém os registros da Cidade
        resultado_get = requests.get(url)
        # Retorna uma lista com os itens da Cidade
        lista = resultado_get.json()
        # Caso passando Cidade e Pais não seja encontrado a latitude/longitude, passo somente a cidade
        if lista:
            return lista
        else:
            url = f'https://nominatim.openstreetmap.org/search.php?city={cidade}&polygon_geojson=1&limit=1&format=jsonv2'
            resultado_get = requests.get(url)
            return resultado_get.json()
    except:
        return print(f'Não foi possível localizar a cidade: {cidade} / {pais}')



def obtem_dados_api():
    # Adicionar a rotina para obter todas as cidades do arquivo de Voos da Anac
    lista_cidade = obtem_cidades()
    # A função map irá iterar sobre todos os itens da lista_cidade e passara item a item para a função executa_url
    itens = list(map(executa_url, lista_cidade))

    try:
        # Encontra na lista a latitude e longitude
        for cabecalho, item in zip(lista_cabecalho, itens):
            codigo_cidade = cabecalho[0]
            latitude_cidade = item[0]['lat']
            longitude_cidade = item[0]['lon']

            # Grava no banco de dados
            dao.put_lat_lon(codigo_cidade, latitude_cidade, longitude_cidade)
    except:
        pass




if __name__ == '__main__':
    obtem_dados_api()
