
class Password:
    def __init__(self, id, usuario, password, url, titulo, descripcion):
        self._id = id
        self._usuario = usuario
        self._password = password
        self._url = url
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_creacion = None


    def to_json(self):
        return {
            "id":self.id,
            "usuario":self.usuario,
            "password": self.password,
            "url": self.url,
            "titulo":self.titulo,
            "descripcion": self.descripcion,
            "fecha_creacion": self.fecha_creacion
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

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


