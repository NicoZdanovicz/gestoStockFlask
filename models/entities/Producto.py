class Producto():
    def __init__(self, id, nombre, cantidad, precio, proveedor, categoria, img) -> None:
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.proveedor = proveedor
        self.categoria = categoria
        self.img = img

class Proveedor():
    def __init__(self, id, nombre, telefono, correo) -> None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Categoria():
    def __init__(self, id, nombre, proveedor) -> None:
        self.id = id
        self.nombre = nombre
        self.proveedor = proveedor

class Pedido():
    def __init__(self, nombre, correo, telefono, categoria, proveedor, producto, cantidad) -> None:
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.categoria = categoria
        self.proveedor = proveedor
        self.producto = producto
        self.cantidad = cantidad
