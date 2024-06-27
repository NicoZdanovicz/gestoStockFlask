from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from config import config
from flask_login import LoginManager, login_user, login_required, logout_user, logout_user, current_user

from models.ModelUser import ModelUser
from models.ModelProducto import ModelProducto
from models.entities.User import User, Register
from models.entities.Producto import Producto, Proveedor,  Categoria, Pedido
import mysql.connector


app = Flask(__name__)
app.config.from_object(config['development'])
db = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['usuario'],0, request.form['contraseña'])
        logged_user = ModelUser.login(db, user)

        if logged_user != None:
            if logged_user.contraseña:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Contraseña incorrecta')
        else:
            flash('Usuario no encontrado')
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/home')
@login_required
def home():

    try:
        pedido = ModelProducto.get_pedido(db, current_user.id)
        producto = ModelProducto.get_producto(db, current_user.id)
    except Exception as ex:
        flash('Error al obtener productos: {}'.format(ex))
        pedido = []
        producto = []

    productos=[]
    productos_mayor={}
    price = []
    cont = 0
  

    for prod in pedido:
        productos.append(prod)

    for produ in producto:
        price.append(produ)

    cantidadProductos = len(price)
    cantidadPedidos = len(productos)

    for prod in productos:
        
        if prod.cantidad >= 40:
            productos_mayor[cont] = [prod.producto, prod.categoria, prod.cantidad]
            cont += 1

    for i in range(cont):
        for prices in price:
            if productos_mayor[i][0] == prices.nombre:
                productos_mayor[i].append(prices.precio)
    
    

    return render_template('home.html', productos_mayor=productos_mayor, cantidadProductos=cantidadProductos, cantidadPedidos=cantidadPedidos)

@app.route('/datos-json', methods=['GET'])
@login_required
def obtener_datos_json():

    try:
        pedido = ModelProducto.get_pedido(db, current_user.id)
        producto = ModelProducto.get_producto(db, current_user.id)
    except Exception as ex:
        flash('Error al obtener productos: {}'.format(ex))
        pedido = []
        producto = []

    productos=[]
    productos_ingresos={}
    price = []
    cont = 0
    ventasPorCategoria = {}
    ingresosPorCategoria = {}

    for prod in pedido:
        productos.append(prod)

    for produ in producto:
        price.append(produ)

    for prod in productos:
        
        productos_ingresos[cont] = [prod.producto, prod.categoria, prod.cantidad]
        cont += 1

        if prod.categoria in ventasPorCategoria:
            ventasPorCategoria[prod.categoria] += prod.cantidad
        else:
            ventasPorCategoria[prod.categoria] = prod.cantidad
    
    for i in range(cont):
        for prices in price:
            if productos_ingresos[i][0] == prices.nombre:
                productos_ingresos[i].append(prices.precio)

    # Calcular ingresos por categoría
    for key, value in productos_ingresos.items():
        
        if len(value) < 4:
            productos_ingresos[key].append(0)
            
        categoria = value[1]  # índice 1 es la categoría
        cantidad_vendida = value[2]  # índice 2 es la cantidad vendida
        precio = value[3]  # índice 3 es el precio del producto

        ingreso_producto = cantidad_vendida * precio

        if categoria in ingresosPorCategoria:
            ingresosPorCategoria[categoria] += ingreso_producto
        else:
            ingresosPorCategoria[categoria] = ingreso_producto

    ingresosTotales = sum(ingresosPorCategoria.values())
    data = {
        'ventasPorCategoria': ventasPorCategoria,
        'ingresosPorCategoria': ingresosPorCategoria,
        'ingresosTotales': ingresosTotales
    }

    return jsonify(data)

@app.route('/productos', methods=['POST', 'GET'])
@login_required
def productos():
    
    if request.method == 'POST':
        if 'delete_id' in request.form: # Detecta si es una solicitud de borrar
            id = request.form['delete_id']
            try:
                ModelProducto.del_producto(db, id)
                flash('Producto eliminado con exito')
            except Exception as ex:
                flash('Error al eliminar producto: {}'.format(ex))
            return redirect('productos')
        
        elif 'edit_id' in request.form:  # Detecta si es una solicitud de edición
            id = request.form['edit_id']
            nombre = request.form['edit_nombre']
            cantidad = request.form['edit_cantidad']
            precio = request.form['edit_precio']
            proveedor = request.form['edit_proveedor']
            categoria = request.form['edit_categoria']
            img = request.form['edit_img']
            producto = Producto(id = id, nombre = nombre, cantidad = cantidad, precio = precio, proveedor = proveedor, categoria = categoria, idusuario = current_user.id , img = img)
            try:
                ModelProducto.update_producto(db, producto)
                flash('Producto actualizado con éxito')
            except Exception as ex:
                flash('Error al actualizar producto: {}'.format(ex))
            return redirect(url_for('productos'))

        else:                                    # Si no es ninguna de las anteriores, es una solicitud de cargar
            nombre = request.form['nombre']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            proveedor = request.form['proveedor']
            categoria = request.form['categoria']
            img = request.form['img']

            producto = Producto(0, nombre, cantidad, precio, proveedor, categoria, current_user.id, img)

            try:
                ModelProducto.producto(db, producto)
                flash('Producto Cargado con exito')
                
            except Exception as ex:
                flash('Error al registrar producto')
            return redirect('productos')
    
    try:
        producto = ModelProducto.get_producto(db, current_user.id)
        categoria = ModelProducto.get_categoria(db, current_user.id)
        proveedor = ModelProducto.get_proveedor(db, current_user.id)
    except Exception as ex:
        flash('Error al obtener productos: {}'.format(ex))
        producto = []
        categoria = [] 
        proveedor = []

    return render_template('productos.html', producto=producto, categoria=categoria, proveedor=proveedor)


@app.route('/categorias', methods=['POST', 'GET'])
@login_required
def categorias():
    if request.method == 'POST':
        if 'delete_id' in request.form: # Detecta si es una solicitud de borrar
            id = request.form['delete_id']
            try:
                ModelProducto.del_categoria(db, id)
                flash('Categoria eliminada con exito')
            except Exception as ex:
                flash('Error al eliminar categoria: {}'.format(ex))
            return redirect('categorias')

        elif 'edit_id' in request.form:  # Detecta si es una solicitud de edición
            id = request.form['edit_id']
            nombre = request.form['edit_nombre']
            categoria = Categoria(id=id, nombre=nombre, idusuario=current_user.id)
            try:
                ModelProducto.update_categoria(db, categoria)
                flash('Categoría actualizada con éxito')
            except Exception as ex:
                flash('Error al actualizar categoría: {}'.format(ex))
            return redirect(url_for('categorias'))

        else:                                   # Si no es ninguna de las anteriores, es una solicitud de cargar
            nombre = request.form['nombre']
            categoria = Categoria(0,nombre, current_user.id)

            try:
                ModelProducto.categoria(db, categoria)
                flash('Categoria Cargado con exito')
                
            except Exception as ex:
                flash('Error al registrar categoria')
            return redirect('categorias')
    
    try:
        categoria = ModelProducto.get_categoria(db, current_user.id)
    except Exception as ex:
        flash('Error al obtener categoria: {}'.format(ex))
        categoria = []

    return render_template('categorias.html', categoria=categoria)


@app.route('/proveedores', methods=['POST', 'GET'])
@login_required
def proveedores():
    if request.method == 'POST':
        if 'delete_id' in request.form:
            id = request.form['delete_id']
            try:
                ModelProducto.del_proveedor(db, id)
                flash('Proveedor eliminado con exito')
            except Exception as ex:
                flash('Error al eliminar proveedor: {}'.format(ex))
            return redirect('proveedores')
        
        elif 'edit_id' in request.form:  # Detecta si es una solicitud de edición
            id = request.form['edit_id']
            nombre = request.form['edit_nombre']
            telefono = request.form['edit_telefono']
            correo = request.form['edit_correo']
            proveedor = Proveedor(id=id, nombre=nombre, telefono=telefono, correo=correo, idusuario=current_user.id)
            try:
                ModelProducto.update_proveedor(db, proveedor)
                flash('Proveedor actualizado con éxito')
            except Exception as ex:
                flash('Error al actualizar proveedor: {}'.format(ex))
            return redirect(url_for('proveedores'))

        else:                                   # Si no es ninguna de las anteriores, es una solicitud de cargar
            nombre = request.form['nombre']
            telefono = request.form['telefono']
            correo = request.form['correo']

            proveedor = Proveedor(0, nombre, telefono, correo, current_user.id)

            try:
                ModelProducto.proveedor(db, proveedor)
                flash('Proveedor Cargado con exito')
                
            except Exception as ex:
                flash('Error al registrar proveedor')
            return redirect('proveedores')
    
    try:
        proveedor = ModelProducto.get_proveedor(db, current_user.id)
    except Exception as ex:
        flash('Error al obtener proveedores: {}'.format(ex))
        proveedor = []

    return render_template('proveedores.html', proveedor=proveedor)


@app.route('/pedidos', methods=['POST', 'GET'])
@login_required
def pedidos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        categoria = request.form['categoria']
        proveedor = request.form['proveedor']
        producto = request.form['producto']
        cantidad = request.form['cantidad']

        pedido = Pedido(0, nombre, correo, telefono, categoria, proveedor, producto, cantidad, current_user.id)

        try:
            ModelProducto.pedido(db, pedido)
            flash('Pedido Cargado con exito')
            return redirect('pedidos')
        except Exception as ex:
            flash('Error al registrar pedido')
            return render_template('pedidos.html')
    

    return render_template('pedidos.html')

@app.route('/pedidos-json', methods=['GET'])
@login_required
def obtener_datos_pedidos():
    try:
        proveedor = ModelProducto.get_proveedor(db, current_user.id)
        categoria = ModelProducto.get_categoria(db, current_user.id)
        producto = ModelProducto.get_producto(db, current_user.id)

        productos_json = {}
        for p in producto:
            if p.nombre in productos_json:
                # Si el producto ya existe en el diccionario, agregar la información adicional
                productos_json[p.nombre].append({'categoria': p.categoria, 'precio': p.precio, 'proveedor': p.proveedor})
            else:
                # Si es la primera vez que se encuentra el producto, crear una nueva entrada
                productos_json[p.nombre] = [{'categoria': p.categoria, 'precio': p.precio, 'proveedor': p.proveedor}]


        
        proveedores_json = {i: p.nombre for i, p in enumerate(proveedor)}
        
        categorias_json = {i: c.nombre for i, c in enumerate(categoria)}

        data = {
            'proveedores_json': proveedores_json,
            'categorias_json': categorias_json,
            'productos_json': productos_json
        }

        return jsonify(data)
    
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

 

@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        user = Register(usuario, correo, contraseña)

        try:
            ModelUser.registro(db, user)
            return redirect(url_for('login'))
        except Exception as ex:
            flash("Usuario o Correo ya registrado")
            return render_template('registro.html')
    return render_template('registro.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>La pagina a la que intentas acceder no existe</h1> ", 404

if __name__ == '__main__':
    
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()