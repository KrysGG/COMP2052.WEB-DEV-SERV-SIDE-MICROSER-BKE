from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a mi API"

@app.route("/info", methods=["GET"])
def info():
    return {
        "Actividad": "2",
        "Author": "Christian Giraud",
        "Info de app": "App de Gestionar Nota Final de Estudiuantes"
    }

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    return f"Hola, {nombre}!"

#############################################
# Json para GET
# {
#  "nombre": "caca" ,
# }
############################################

if __name__ == "__main__":
    app.run(debug=True)