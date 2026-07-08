import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:
    def GET(self, id_contacto):
        conn = sqlite3.connect('sql/agenda.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id_contacto, nombre, primer_apellido FROM contactos WHERE id_contacto = ?", (id_contacto,))
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return "Contacto no encontrado"
            
        contacto = web.storage({'id_contacto': row[0], 'nombre': row[1], 'primer_apellido': row[2]})
        return render.borrar_contacto(contacto)

    # Bloquear por completo la eliminación
    def POST(self, id_contacto):
        # Levantamos el error de método no permitido nativo de web.py
        raise web.nomethod()