from flask import Flask, request, jsonify

app = Flask(__name__)


usuarios = []

@app.route("/info", methods=["GET"])
def info():
    return jsonify({

        "Actividad": "3",
        "app": "Sistema de Gestión",
        "Author": "Christian Giraud",
        "Numero de Estudiante": "R00569998",
        "description": "API para recibir y mostrar datos de usuarios"
    })

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    print(request.data) 
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser json"}), 415
    data = request.json
    print(data) 
    nombre = data.get("nombre")
    correo = data.get("correo")
    if not nombre or not correo:
        return jsonify({"error": "El nombre y el correo son requeridos"}), 400
    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    return jsonify(usuario), 201

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)