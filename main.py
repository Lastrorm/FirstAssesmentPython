from flask import Flask, request, render_template
from clases.Asignaturas import *

app = Flask(__name__, template_folder='html')


@app.route("/")
def asignaturas():
    return render_template("start_asignaturas.html")


@app.route("/asignaturas", methods=['POST'])
def mostrar_asignaturas():
    # Obtener la asignatura seleccionada por el usuario

    if request.form["asignatura"] == "matematicas":
        asignatura_ingresada = Matematicas(request.form["asignatura"], request.form["profesor"], request.form["nivel"])
    elif request.form["asignatura"] == "ciencias":
        asignatura_ingresada = Ciencias(request.form["asignatura"], request.form["profesor"], request.form["laboratorio"])
    else:
        asignatura_ingresada = Historia(request.form["asignatura"], request.form["profesor"], request.form["epoca"])

    # Insertar el código aquí



    # Renderizar la página de asignaturas con la asignatura seleccionada
    return render_template("asignaturas.html", asignatura=asignatura_ingresada)


if __name__ == '__main__':
    app.run(debug=True)