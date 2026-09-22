import web

urls = (
    '/', 'controllers.index.Index',
    '/agregar', 'controllers.index.Agregar',
    '/atender', 'controllers.index.Atender'
)

app = web.application(urls, globals())

render = web.template.render('views')

if __name__ == "__main__":
    app.run()