from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self,id,first_name,last_name,email,created_at,updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        self.updated_at =updated_at

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def obtenerListaUsuarios (cls):
        query = "SELECT * from users ;"
        resultado = connectToMySQL ("users_db").query_db (query)
        listaUsuarios = []
        for usuario in resultado:
            listaUsuarios.append (Usuario (usuario["id"],usuario["first_name"],usuario["last_name"], usuario ["email"], usuario["created_at"], usuario['updated_at']))
        return listaUsuarios


    @classmethod
    def agregarUsuario (cls, nuevoUsuario):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s, %(last_name)s,%(email)s);"
        resultado = connectToMySQL ("users_db").query_db (query,nuevoUsuario)
        return resultado

    @classmethod
    def obternerDatosUsuario(cls,usuario):
        query = "SELECT * FROM users WHERE id =%(id)s;"
        resultado = connectToMySQL ("users_db").query_db (query, usuario)
        return resultado[0]


    @classmethod
    def update(cls,usuarioAEditar):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_db" ).query_db( query, usuarioAEditar )
        return resultado       
        
    @classmethod
    def eliminarUsuario(cls, usuario):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL ("users_db").query_db (query,usuario)