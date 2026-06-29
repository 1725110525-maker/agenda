import web

urls = (
    '/', 'index_contactos',
    '/lista_contactos', 'lista_contactos',
    '/ver_contactos', 'ver_contactos',
    '/insertar_contactos', 'insertar_contactos',
    '/editar_contactos', 'editar_contactos',
    '/borrar_contactos', 'borrar_contactos'
)

app = web.application(urls, globals())
render = web.template.render('views/') 

class index_contactos:
    def GET(self):
        return render.index_contactos()

class lista_contactos:
    def GET(self):
        return render.lista_contactos()

class ver_contactos:
    def GET(self):
        return render.ver_contactos()

class insertar_contactos:
    def GET(self):
        return render.insertar_contactos()
    def POST(self):
        raise web.seeother('/lista_contactos')

class editar_contactos:
    def GET(self):
        return render.editar_contactos()
    def POST(self):
        raise web.seeother('/lista_contactos')

class borrar_contactos:
    def GET(self):
        return render.borrar_contactos()
    def POST(self):
        raise web.seeother('/lista_contactos')

if __name__ == "__main__":
    app.run()