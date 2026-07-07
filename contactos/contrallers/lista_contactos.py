import web
import sqlite3

# Agregamos '../' para salir de la carpeta controllers
render = web.template.render('../views', base='layout')

class ListaContactos:

    def obtenerContactos(self):
        conn = None # Inicializamos en None para evitar errores en el finally
        try:
            # Agregamos '../' para buscar la base de datos en la raíz
            conn = sqlite3.connect('../sql/agenda.db')
            cursor = conn.cursor()
            
            query = "SELECT * FROM contactos;"
            cursor.execute(query)
            
            contactos = []
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                contactos.append(contacto)

            conn.close()
            return contactos
            
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []
        finally:
            # Solo intentamos cerrar si conn fue creada exitosamente
            if conn:
                conn.close()

    def GET(self):
        contactos = self.obtenerContactos()
        return render.lista_contactos(contactos)