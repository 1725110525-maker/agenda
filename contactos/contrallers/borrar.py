import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def eliminarContacto(self, id_contacto: int):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
   
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            
            # Guarda los cambios en la base de datos (¡Crucial para DELETE/UPDATE/INSERT!)
            conn.commit()
            
            # Cierra la conexión a la base de datos
            conn.close()
            return True
            
        except sqlite3.Error as error:
            print(f"ERROR borrarContacto 100: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR borrarContacto 101: {error.args}")
            return False
        finally:
            # Nos aseguramos de cerrar la conexión si quedó abierta
            try:
                conn.close()
            except:
                pass

    def POST(self, id_contacto):
        print(f"ID_CONTACTO A ELIMINAR: {id_contacto}")
        
        # Ejecuta la eliminación
        eliminado = self.eliminarContacto(id_contacto)
        print(f"¿Eliminado con éxito?: {eliminado}")

        # Redirecciona a la página principal de la agenda o lista de contactos
        raise web.seeother('/')