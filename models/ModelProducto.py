from .entities.Producto import Producto, Proveedor,  Categoria, Pedido

class ModelProducto():

    @classmethod
    def producto(self, db, producto):
        try:
            cursor = db.cursor()
            sql = """INSERT INTO productos (nombre, cantidad, precio, proveedor, categoria, idusuario, img ) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (producto.nombre, producto.cantidad, producto.precio, producto.proveedor, producto.categoria, producto.idusuario, producto.img))
            db.commit()
            return producto
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_producto(self, db, id):
        try:
            cursor = db.cursor()
            sql = """ SELECT id, nombre, cantidad, precio, proveedor, categoria, idusuario, img FROM productos WHERE idusuario = %s"""
            cursor.execute(sql, (id,))
            rows = cursor.fetchall()
            producto = []

            for row in rows:
                producto.append(Producto(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            return producto
            
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod   
    def del_producto(self, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_producto(self, db, producto):
        try:
            cursor = db.cursor()
            sql = """UPDATE productos SET nombre = %s, cantidad= %s, precio = %s, proveedor = %s, categoria = %s, img = %s WHERE id = %s"""
            cursor.execute(sql, (producto.nombre, producto.cantidad, producto.precio, producto.proveedor, producto.categoria, producto.img, producto.id))
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def proveedor(self, db, proveedor):
        try:
            cursor = db.cursor()
            sql = """INSERT INTO proveedores (nombre, telefono, correo, idusuario) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (proveedor.nombre, proveedor.telefono, proveedor.correo, proveedor.idusuario))
            db.commit()
            return proveedor
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_proveedor(self, db, id):
        try:
            cursor = db.cursor()
            sql = """ SELECT id, nombre, telefono, correo, idusuario FROM proveedores WHERE idusuario = %s"""
            cursor.execute(sql, (id,))
            rows = cursor.fetchall()
            proveedor = []

            for row in rows:
                proveedor.append(Proveedor(row[0], row[1], row[2], row[3], row[4]))
            return proveedor
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod   
    def del_proveedor(self, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM proveedores WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_proveedor(self, db, proveedor):
        try:
            cursor = db.cursor()
            sql = """UPDATE proveedores SET nombre = %s, telefono = %s, correo = %s WHERE id = %s"""
            cursor.execute(sql, (proveedor.nombre, proveedor.telefono, proveedor.correo, proveedor.id))
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def categoria(self, db, categoria):
        try:
            cursor = db.cursor()
            sql = """INSERT INTO categorias (nombre, idusuario) 
                     VALUES (%s, %s)"""
            cursor.execute(sql, (categoria.nombre, categoria.idusuario))
            db.commit()
            return categoria
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_categoria(self, db, id):
        try:
            cursor = db.cursor()
            sql = """ SELECT id, nombre, idusuario FROM categorias WHERE idusuario = %s"""
            cursor.execute(sql, (id,))
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
            cursor = db.cursor()
            sql = "DELETE FROM categorias WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_categoria(self, db, categoria):
        try:
            cursor = db.cursor()
            sql = """UPDATE categorias SET nombre = %s WHERE id = %s"""
            cursor.execute(sql, (categoria.nombre, categoria.id))
            db.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def pedido(self, db, pedido):
        try:
            cursor = db.cursor()
            sql = """INSERT INTO pedidos (nombre, correo, telefono, categoria, proveedor, producto, cantidad, idusuario) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (pedido.nombre, pedido.correo, pedido.telefono, pedido.categoria, pedido.proveedor, pedido.producto, pedido.cantidad, pedido.idusuario))
            db.commit()
            return pedido
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_pedido(self, db, id):
        try:
            cursor = db.cursor()
            sql = """ SELECT id, nombre, correo, telefono, categoria, proveedor, producto, cantidad, idusuario FROM pedidos WHERE idusuario = %s"""
            cursor.execute(sql, (id,))
            rows = cursor.fetchall()
            pedido = []

            for row in rows:
                pedido.append(Pedido(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            return pedido
            
        except Exception as ex:
            raise Exception(ex)

        