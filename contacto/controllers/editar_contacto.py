import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:
    # 1. Obtener los datos actuales del contacto para rellenar el formulario
    def GET(self, id_contacto):
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contactos WHERE id_contacto = ?", (id_contacto,))
        row = cursor.fetchone()
        conn.close()
        
        if not row: 
            return "Contacto no encontrado"
            
        contacto = web.storage({
            'id_contacto': row[0], 'nombre': row[1], 'primer_apellido': row[2],
            'segundo_apellido': row[3], 'email': row[4], 'telefono': row[5]
        })
        return render.editar_contacto(contacto)

    # 2. Bloquear por completo el guardado de cambios
    def POST(self, id_contacto):
        # Configuramos el estatus de error (puedes usar '405 Method Not Allowed' o '404 Not Found')
        web.ctx.status = '405 Method Not Allowed'
        
        # Este es el texto exacto que se pintará en la pantalla del navegador
        return "method not allowed"