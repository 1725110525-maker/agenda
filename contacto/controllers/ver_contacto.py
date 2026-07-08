import web
import sqlite3

render = web.template.render('views', base='layout')

class VerContacto:
    # Recibimos el id_contacto que viene de la URL
    def buscarContacto(self, id_contacto:int):
        try:
            # Conectamos a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            # Esto hace que los resultados se comporten como diccionarios
            cursor = conn.cursor()

            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            
            # Buscamos al contacto específico
            row = cursor.fetchone()
            contacto = {
                'id_contacto': row[0],
                'nombre':row[1],
                'primer_apellido':row[2],
                'segundo_apellido':row[3],
                'email':row[4],
                'telefono':row[5]
            }

            conn.close()

            return contacto
        except sqlite3.Error as error:
            print(f"ERROR verContactos 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR verContactos 101: {error.args}")
            return {}
        finally:
            conn.close()

    def GET(self,id_contacto):
        print(f"ID CONTACTO: {id_contacto}")
        datos = self.buscarContacto(id_contacto)
        print(datos)

        if not datos:
            return "Contacto no encontrado"
            
        # Convertimos el diccionario a un objeto 'Storage' 
        # para que en el HTML se pueda usar la sintaxis $contacto.nombre
        contacto = web.storage(datos)
        
        # Asegúrate de que tu archivo HTML se llame 'ver_contacto.html' y esté dentro de la carpeta 'views'
        return render.ver_contacto(contacto)