import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:

    def buscarContacto(self, id_contacto: int):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            
            if row:
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
            else:
                contacto = {}
                
            conn.close()
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR editarContacto 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR editarContacto 101: {error.args}")
            return {}
        finally:
            try: conn.close()
            except: pass

    def actualizarContacto(self, id_contacto: int, datos: dict):
        """Ejecuta el UPDATE con los nuevos datos en la base de datos."""
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta SQL para actualizar los campos
            query = """
                UPDATE contactos 
                SET nombre = ?, primer_apellido = ?, segundo_apellido = ?, email = ?, telefono = ? 
                WHERE id_contacto = ?
            """
            
            # Pasamos los nuevos valores en orden junto con el id_contacto al final
            cursor.execute(query, (
                datos.get('nombre'),
                datos.get('primer_apellido'),
                datos.get('segundo_apellido'),
                datos.get('email'),
                datos.get('telefono'),
                id_contacto
            ))
            
            # ¡No olvides el commit para guardar los cambios!
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR editarContacto 200: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR editarContacto 201: {error.args}")
            return False
        finally:
            try: conn.close()
            except: pass

    def GET(self, id_contacto):
        """Muestra el formulario de edición con los datos actuales."""
        print(f"GET - EDITAR ID_CONTACTO: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        
        # Le pasamos el diccionario 'contacto' a la vista para rellenar los inputs
        return render.editar_contacto(contacto)

    def POST(self, id_contacto):
        """Recibe los datos del formulario y los procesa."""
        print(f"POST - ACTUALIZANDO ID_CONTACTO: {id_contacto}")
        
        # web.input() recupera los datos que viajan desde los <input> del formulario HTML
        datos_formulario = web.input()
        
        # Mandamos actualizar pasándole el ID y los datos recibidos
        actualizado = self.actualizarContacto(id_contacto, datos_formulario)
        print(f"¿Actualizado con éxito?: {actualizado}")
        
        # Redireccionamos a la lista principal tras guardar los cambios
        raise web.seeother('/')