from .entities.Producto import Producto, Proveedor,  Categoria

class ModelProducto():

    @classmethod
    def producto(self, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO productos (nombre, cantidad, precio, proveedor, categoria, img) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (producto.nombre, producto.cantidad, producto.precio, producto.proveedor, producto.categoria, producto.img))
            db.connection.commit()
            return producto
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_producto(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, nombre, cantidad, precio, proveedor, categoria, img FROM productos"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            producto = []

            for row in rows:
                producto.append(Producto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return producto
            
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod   
    def del_producto(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_producto(self, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE productos SET nombre = %s, cantidad= %s, precio = %s, proveedor = %s, categoria = %s, img = %s WHERE id = %s"""
            cursor.execute(sql, (producto.nombre, producto.cantidad, producto.precio, producto.proveedor, producto.categoria, producto.img, producto.id))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def proveedor(self, db, proveedor):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO proveedores (nombre, telefono, correo) 
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (proveedor.nombre, proveedor.telefono, proveedor.correo))
            db.connection.commit()
            return proveedor
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_proveedor(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, nombre, telefono, correo FROM proveedores"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            proveedor = []

            for row in rows:
                proveedor.append(Proveedor(row[0], row[1], row[2], row[3]))
            return proveedor
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod   
    def del_proveedor(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM proveedores WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_proveedor(self, db, proveedor):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE proveedores SET nombre = %s, telefono = %s, correo = %s WHERE id = %s"""
            cursor.execute(sql, (proveedor.nombre, proveedor.telefono, proveedor.correo, proveedor.id))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def categoria(self, db, categoria):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO categorias (nombre, proveedor) 
                     VALUES (%s, %s)"""
            cursor.execute(sql, (categoria.nombre, categoria.proveedor))
            db.connection.commit()
            return categoria
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_categoria(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, nombre, proveedor FROM categorias"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            categoria = []

            for row in rows:
                categoria.append(Categoria(row[0],row[1], row[2]))
            return categoria
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod   
    def del_categoria(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM categorias WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_categoria(self, db, categoria):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE categorias SET nombre = %s, proveedor = %s WHERE id = %s"""
            cursor.execute(sql, (categoria.nombre, categoria.proveedor, categoria.id))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def pedido(self, db, pedido):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO pedidos (nombre, correo, telefono, categoria, proveedor, producto, cantidad) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (pedido.nombre, pedido.correo, pedido.telefono, pedido.categoria, pedido.proveedor, pedido.producto, pedido.cantidad))
            db.connection.commit()
            return pedido
        
        except Exception as ex:
            raise Exception(ex)
        

        