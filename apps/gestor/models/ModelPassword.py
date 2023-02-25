from apps.gestor.models.entities.Password import Password


class ModelPassword:
    @classmethod
    def obtener_todos(cls, obj_conexion):
        try:
            with obj_conexion as conn:
                with conn.cursor() as cursor:
                    query = 'SELECT id, usuario,  PGP_SYM_DECRYPT(password::bytea, \'CLAVE_AES\'), url, nombre_sitio, ' \
                            'descripcion, CAST(fecha_creacion as date) FROM gestor_password WHERE baja=false'
                    cursor.execute(query)
                    registros = cursor.fetchall()

            listaDePassword = []
            for registro in registros:
                objPassword = Password(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                objPassword.fecha_creacion = registro[6]
                listaDePassword.append(objPassword)
            return listaDePassword
        except Exception as e:
            print(f'Error: {e}')
            return e

    @classmethod
    def insertar_password(cls, obj_conexion, obj_password):
        try:
            with obj_conexion as conn:
                with conn.cursor() as cursor:
                    query = f'INSERT INTO gestor_password (usuario, password, url, nombre_sitio, descripcion, baja) ' \
                            f'VALUES (%s, PGP_SYM_ENCRYPT(%s,\'CLAVE_AES\'), %s, %s, %s, %s)'
                    tuplaDeValores = (obj_password.usuario, obj_password.password, obj_password.url,
                                      obj_password.nombre_sitio, obj_password.descripcion, obj_password.baja)
                    cursor.execute(query, tuplaDeValores)

        except Exception as e:
            print(f'Error: {e}')
            return e

    @classmethod
    def obtener_uno(cls, obj_conexion, id):
        try:
            with obj_conexion as conn:
                with conn.cursor() as cursor:
                    query = f'SELECT id, usuario,  PGP_SYM_DECRYPT(password::bytea, \'CLAVE_AES\'), url, nombre_sitio, ' \
                            f'descripcion, CAST(fecha_creacion as date) FROM gestor_password WHERE baja=false and id={id}'
                    cursor.execute(query)
                    registro = cursor.fetchone()

            listaDePassword = []
            objPassword = Password(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
            objPassword.fecha_creacion = registro[6]
            listaDePassword.append(objPassword)
            return listaDePassword

        except Exception as e:
            print(f'Error: {e}')
            return Exception


    @classmethod
    def actualizar(cls, obj_conexion, obj_password):
        try:
            with obj_conexion as conn:
                with conn.cursor() as cursor:
                    query = f'UPDATE gestor_password SET usuario=%s, password=PGP_SYM_ENCRYPT(%s,\'CLAVE_AES\') , url=%s, ' \
                            f'nombre_sitio=%s, descripcion=%s WHERE id={obj_password.id}'
                    tuplaDeValores = (obj_password.usuario, obj_password.password, obj_password.url,
                                      obj_password.nombre_sitio, obj_password.descripcion)
                    cursor.execute(query, tuplaDeValores)

        except Exception as e:
            print(f'Error: {e}')
            return Exception


    @classmethod
    def eliminar(cls, obj_conexion, id):
        try:
            with obj_conexion as conn:
                with conn.cursor() as cursor:
                    query = f'UPDATE gestor_password SET baja=TRUE WHERE baja=FALSE and id={id}'
                    cursor.execute(query)

        except Exception as e:
            print(f'Error: {e}')
            return Exception



if __name__ == '__main__':
    password = Password(15, "Facebook", "Facebook456", None, 'password de face')
    # registro = PasswordDao.insertar_password(password)

    # print(PasswordDao.obterner_todos()[1].usuario)
    # print(ModelPassword.obtener_uno()
