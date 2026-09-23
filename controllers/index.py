import web

render = web.template.render("views")

fila = []


class Index:

    def GET(self):
        return render.index(fila)