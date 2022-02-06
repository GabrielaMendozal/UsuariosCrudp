from flask import Flask, render_template, request , redirect
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario

@app.route("/", methods = ["GET"])
def inicio():
    return redirect ("/users")

@app.route("/users", methods = ["GET"])
def desplegarListaUsuarios():
    return render_template("user.html", usuarios = Usuario.obtenerListaUsuarios())

@app.route ("/user/new")
def desplegarRegistro():
    return render_template("new.html")

@app.route ("/user/create", methods = ["POST"])
def registrarUsuario():
    nuevoUsuario = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    } 

    if nuevoUsuario["first_name"] == "" or nuevoUsuario["last_name"] == "" or nuevoUsuario["email"] == "":
        return redirect( '/user/new' )
    
    resultado = Usuario.agregarUsuario( nuevoUsuario )
    # ToDo: Validar resultado que nos arroja 0
    if type( resultado ) is int and resultado == 0:
        return redirect( '/users' )
    else:
        return redirect( '/user/new' )


@app.route("/user/edit/<int:id>",methods = ["GET"])
def desplegarEditarUsuario(id):
    data = {"id" : id}
    return render_template ("edit.html", usuario= Usuario.obternerDatosUsuario(data))


@app.route('/user/edit/<int:id>',methods=['POST'])
def editarUsuario(id):
    usuarioAEditar = {
        "id": id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    resultado = Usuario.update( usuarioAEditar )
    
    #Validar que el usuario editado sea el de la sesion
    return redirect( '/users' )


@app.route("/user/show/<int:id>")
def show(id):
    data = {"id" : id}
    return render_template ("show.html",usuario = Usuario.obternerDatosUsuario(data))

@app.route ("/user/delete/<int:id>")
def eliminarAUsuario(id):
    data = {"id" : id}
    Usuario.eliminarUsuario(data)
    return redirect ('/users')
