// Contenedor de productos

const boton_agregar = document.querySelector('.boton_agregar');
const boton_quitar = document.querySelector('.boton_quitar');
const formLinks_prod = document.querySelector('.formulario');


boton_agregar.addEventListener('click', () => {
    formLinks_prod.classList.toggle('activar_form'); // Alternar la clase 'active' en el contenedor de enlaces
});
boton_quitar.addEventListener('click', (event) => {
    event.preventDefault();
    event.stopPropagation(); // Detener la propagación del evento click
    formLinks_prod.classList.toggle('activar_form'); // Alternar la clase 'activar_form' en el formulario
});


/*-------------------------------------------------*/
function validacion() {
    // Obtener los valores de los campos de entrada
    var nombre = document.getElementById("nombre").value;
    var cantidad = document.getElementById("cantidad").value;
    var precio = document.getElementById("precio").value;
    var seleccion_prod = document.getElementById("categoria").selectedIndex;
    var seleccion_prov = document.getElementById("proveedor").selectedIndex;
    

    // Inicializar una variable de estado para controlar si hay errores
    var hayError = false;

    // Limpiar mensajes de error anteriores
    document.getElementById("mensaje-nombre").innerHTML = "";
    document.getElementById("mensaje-cantidad").innerHTML = "";
    document.getElementById("mensaje-precio").innerHTML = "";
    document.getElementById("mensaje-seleccion-cat").innerHTML = "";
    document.getElementById("mensaje-seleccion-prov").innerHTML = "";

    // Validar el nombre
    if (nombre == null || nombre.length == 0) {
        document.getElementById("mensaje-nombre").innerHTML = "⚠️ El campo nombre es obligatorio";
        hayError = true;
    }

     //Validar la cantidad de productos
     if (cantidad == null || cantidad.length == 0) {
        document.getElementById("mensaje-cantidad").innerHTML = "⚠️ El campo cantidad es obligatorio";
        hayError = true;
    }


    // Validar el precio
    if (precio == null || precio.length == 0) {
        document.getElementById("mensaje-precio").innerHTML = "⚠️ El campo precio es obligatorio";
        hayError = true;
    }

    //Validar seleccion de productod
    if(seleccion_prod == null || seleccion_prod == 0){
        document.getElementById("mensaje-seleccion-cat").innerHTML = "⚠️ Tenes que seleccionar alguna opcion";
        hayError = true;
    }

    //Validar seleccion de proveedor
    if(seleccion_prov == null || seleccion_prov == 0){
        document.getElementById("mensaje-seleccion-prov").innerHTML = "⚠️ Tenes que seleccionar alguna opcion";
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

function mostrarFormularioEdicion(id, nombre, cantidad, precio, proveedor, categoria, img) {
    document.getElementById('edit_id').value = id;
    document.getElementById('edit_nombre').value = nombre;
    document.getElementById('edit_cantidad').value = cantidad;
    document.getElementById('edit_precio').value = precio;
    document.getElementById('edit_proveedor').value = proveedor;
    document.getElementById('edit_categoria').value = categoria;
    document.getElementById('edit_img').value = img;
    document.getElementById('formularioEdicion').style.display = 'block';
}
function ocultarFormularioEdicion() {
    document.getElementById('formularioEdicion').style.display = 'none';
}