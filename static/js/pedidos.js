function validacion() {
    // Obtener los valores de los campos de entrada
    var nombre = document.getElementById("nombre").value;
    var correo = document.getElementById("correo").value;
    var seleccion = document.getElementById("categoria").selectedIndex;
    var seleccion_prod = document.getElementById("producto").selectedIndex;
    var seleccion_prov = document.getElementById("proveedor").selectedIndex;
    var cantidad = document.getElementById("cantidad").value;
    var telefono = document.getElementById("telefono").value;


    // Inicializar una variable de estado para controlar si hay errores
    var hayError = false;

    // Limpiar mensajes de error anteriores
    document.getElementById("mensaje-nombre").innerHTML = "";
    document.getElementById("mensaje-correo").innerHTML = "";
    document.getElementById("mensaje-seleccion-prov").innerHTML = "";
    document.getElementById("mensaje-seleccion").innerHTML = "";
    document.getElementById("mensaje-cantidad").innerHTML = "";
    document.getElementById("mensaje-telefono").innerHTML = "";
    document.getElementById("mensaje-seleccion-prod").innerHTML = "";

    // Validar el nombre
    if (nombre == null || nombre.length == 0) {
        document.getElementById("mensaje-nombre").innerHTML = "⚠️ El campo nombre y apellido es obligatorio";
        hayError = true;
    }

    // Validar el correo
    if (correo == null || correo.length == 0) {
        document.getElementById("mensaje-correo").innerHTML = "⚠️ El campo correo es obligatorio";
        hayError = true;
    } else if (!/^[0-9a-zA-Z._.-]+@[0-9a-zA-Z._.-]+\.[a-zA-Z]{2,6}$/.test(correo)) {
        document.getElementById("mensaje-correo").innerHTML = "⚠️ Debe escribir un correo válido";
        hayError = true;
    }


    //Validar seleccion de productod
    if(seleccion == null || seleccion == 0){
        document.getElementById("mensaje-seleccion").innerHTML = "⚠️ Tenes que seleccionar alguna opcion";
        hayError = true;
    }

    
    //Validar seleccion de productod
    if(seleccion_prod == null || seleccion_prod == 0){
        document.getElementById("mensaje-seleccion-prod").innerHTML = "⚠️ Tenes que seleccionar alguna opcion";
        hayError = true;
    }


    
    //Validar seleccion de productod
    if(seleccion_prov == null || seleccion_prov == 0){
        document.getElementById("mensaje-seleccion-prov").innerHTML = "⚠️ Tenes que seleccionar alguna opcion";
        hayError = true;
    }


    //Validar la cantidad de productos
    if (cantidad == null || cantidad.length == 0) {
        document.getElementById("mensaje-cantidad").innerHTML = "⚠️ El campo cantidad es obligatorio";
        hayError = true;
    }

    //Validar el telefono
    if(isNaN(telefono)){
        document.getElementById("mensaje-telefono").innerHTML = "⚠️ El telefono tiene que ser un numero";
        hayError = true;
    }

    // Devolver false si hay algún error para evitar el envío del formulario
    return !hayError;
}
setTimeout(function() {
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        alert.style.opacity = "0";
        setTimeout(function() { alert.style.display = "none"; }, 800);
    });
}, 3000);

document.addEventListener('DOMContentLoaded', function() {
    
    fetch('/pedidos-json')
    .then(response => response.json())
    .then(data => {

        const productos = data.productos_json;
        const proveedores = data.proveedores_json;
        const categorias = data.categorias_json;

        const selectProveedor = document.getElementById('proveedor');
        const selectCategoria = document.getElementById('categoria');
        const selectProducto = document.getElementById('producto');

        console.log('Productos:', productos);
        console.log('Proveedores:', proveedores);
        console.log('Categorias:', categorias);

        // Limpiar selects antes de agregar opciones
        selectProveedor.innerHTML = '<option value="">Seleccione un Proveedor</option>';
        selectCategoria.innerHTML = '<option value="">Seleccione una Categoria</option>';
        selectProducto.innerHTML = '<option value="">Seleccione un Producto</option>';

        // Cargar opciones de proveedores
        Object.values(proveedores).forEach(proveedor => {
            const option = document.createElement('option');
            option.value = proveedor;
            option.text = proveedor;
            selectProveedor.appendChild(option);
        });
            
        selectCategoria.innerHTML = '<option value="">Seleccione una Categoria</option>';
    
        // Cargar opciones de categorías
        Object.values(categorias).forEach(categoria => {
        const option = document.createElement('option');
        option.value = categoria;
        option.text = categoria;
        selectCategoria.appendChild(option);
        });
    
        // Limpiar productos cuando se cambia el proveedor
        selectProducto.innerHTML = '<option value="">Seleccione un Producto</option>';
      
        
        
        // Función para filtrar productos basados en el proveedor y la categoría seleccionados
        window.filtrarProductos = function() {
            const proveedorSeleccionado = selectProveedor.value;
            const categoriaSeleccionada = selectCategoria.value;
            selectProducto.innerHTML = '<option value="">Seleccione un Producto</option>';
        
            // Obtener los productos que coinciden con el proveedor y la categoría seleccionados
            Object.keys(productos).forEach(prod => {
                productos[prod].forEach(item => {
                    if (item.proveedor === proveedorSeleccionado && item.categoria === categoriaSeleccionada) {
                        const option = document.createElement('option');
                        option.value = prod;
                        option.text = prod;
                        selectProducto.appendChild(option);
                    }
                });
            });
        };
        
        
        

    })
    .catch(error => console.error('Error al cargar datos:', error));
});