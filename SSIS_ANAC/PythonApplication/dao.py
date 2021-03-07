import pyodbc

class DataAccessObject():

    # O construtor obtém a connection string com o banco de dados SQL Server
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=ANAC;UID=sa;PWD=123456')
        self.cursor = self.conn.cursor()



    # Esse método obtém todas as cidades, estados e paises da dim_regiao
    def get_cidades(self, dao):
        self.cursor.execute('spr_get_dim_regiao')

        return self.cursor



    # O método atualiza com a latitude e longitude considerando o código da cidade
    def put_lat_lon(self, codigo_cidade, latitude_cidade, longitude_cidade):
        try:
            self.cursor.execute(f'spr_update_dim_regiao {codigo_cidade}, {latitude_cidade}, {longitude_cidade}')
            self.cursor.commit()
        except:
            print('Não foi possível salvar a latitude e longitude!')

