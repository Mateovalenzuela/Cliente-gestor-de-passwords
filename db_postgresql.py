import psycopg2


class Conexion:

    @classmethod
    def obtener_conexion(cls):
        try:
            conn = psycopg2.connect(
                host='localhost', database='test_gestor_de_passwords',
                user='postgres', password='admin123')

            print("Conexion exitosa")
            return conn
        except Exception as e:
            print(e)
