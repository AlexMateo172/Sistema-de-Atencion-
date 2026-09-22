import web
from controllers.index import fila

render = web.template.render("views")


class Atender:

    def GET(self):
        return render.atender(fila)

    def POST(self):

        if len(fila) > 0:
            fila.pop(0)

        return render.atender(fila)