
class Password:
    def __init__(self, id, usuario, password, url="", nombre_sitio="",descripcion=""):
        self._id = id
        self._usuario = usuario
        self._password = password
        self._url = url
        self._nombre_sitio = nombre_sitio
        self._descripcion = descripcion
        self._fecha_creacion = None
        self._baja = False

    @property
    def id(self):
        return self._id

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def nombre_sitio(self):
        return self._nombre_sitio

    @nombre_sitio.setter
    def nombre_sitio(self, nombre_sitio):
        self._nombre_sitio = nombre_sitio

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def baja(self):
        return self._baja

    @baja.setter
    def baja(self, baja: bool):
        self._baja = baja



