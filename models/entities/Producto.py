class Producto():
    def __init__(self, id, nombre, cantidad, precio, proveedor, categoria, idusuario, img) -> None:
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.proveedor = proveedor
        self.categoria = categoria
        self.img = img
        self.idusuario = idusuario

class Proveedor():
    def __init__(self, id, nombre, telefono, correo, idusuario) -> None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.idusuario = idusuario

class Categoria():
    def __init__(self, id, nombre, idusuario) -> None:
        self.id = id
        self.nombre = nombre
        self.idusuario = idusuario

class Pedido():
    def __init__(self,id, nombre, correo, telefono, categoria, proveedor, producto, cantidad, idusuario) -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.categoria = categoria
        self.proveedor = proveedor
        self.producto = producto
        self.cantidad = cantidad
        self.idusuario = idusuario