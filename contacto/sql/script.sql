CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apelido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);
INSERT INTO contactos(nombre,primer_apellido,segundo_apelido,email,telefono)
VALUES
('dejah', 'thoris', 'barsonn', 'dejah@email.com', '11111111111'),
('john', 'carper', 'earth', 'john@email.com', '222222222');
SELECT * FROM contactos;