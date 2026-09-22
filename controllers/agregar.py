import web
from controllers.index import fila

render = web.template.render("views")


class Agregar:

    def GET(self):
        return render.agregar()

    def POST(self):
        datos = web.input()

        estudiante = {
            "matricula": datos.matricula,
            "nombre": datos.nombre,
            "carrera": datos.carrera,
            "tramite": datos.tramite
        }

        fila.append(estudiante)

        return render.agregar()