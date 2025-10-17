from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
STUDENTS = [
    {"id": 1, "name": "Ana Rivera",   "final_grade": 92},
    {"id": 2, "name": "Luis Torres",  "final_grade": 81},
    {"id": 3, "name": "María López",  "final_grade": 88},
    {"id": 4, "name": "Pedro Santos", "final_grade": 73},
]

# Lista de notas finales
GRADES = [s["final_grade"] for s in STUDENTS]

def average(nums):
    return round(sum(nums) / len(nums), 2) if nums else 0.0

# Rutas
@app.route("/")
def index():
    context = {
        "page_title": "Inicio",
        "students_count": len(STUDENTS),
        "avg_grade": average(GRADES),
    }
    return render_template("index.html", **context)

@app.route("/students")
def students():
        # Tabla de estudiantes con nota final
    return render_template("students.html",
                           page_title="Estudiantes",
                           students=STUDENTS)

@app.route("/grades")
def grades():
        # Lista/resumen de notas
    context = {
        "page_title": "Notas",
        "grades": GRADES,
        "avg": average(GRADES),
        "maxg": max(GRADES) if GRADES else 0,
        "ming": min(GRADES) if GRADES else 0,
        "count": len(GRADES),
    }
    return render_template("grades.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
