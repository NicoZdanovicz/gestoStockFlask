const editarProveedor=()=>{
    alert("No implementado")
   }
   const deleteProveedor=()=>{
       alert("No implementado")
   }

   const boton_agregar = document.querySelector('.boton_agregar');
   const formLinks_categ = document.querySelector('.formulario');
   const boton_quitar = document.querySelector('.boton_quitar');
   boton_agregar.addEventListener('click', () => {
       formLinks_categ.classList.toggle('activar_form'); // Alternar la clase 'active' en el contenedor de enlaces
   });
   boton_quitar.addEventListener('click', (event) => {
    event.preventDefault();
    event.stopPropagation(); // Detener la propagación del evento click
    formLinks_categ.classList.toggle('activar_form'); // Alternar la clase 'activar_form' en el formulario
});
   
   function validacion() {
       // Obtener los valores de los campos de entrada
       var categoria = document.getElementById("nombre").value;
       var seleccion_prov = document.getElementById("proveedor").selectedIndex;
       // Inicializar una variable de estado para controlar si hay errores
       var hayError = false;
   
       // Limpiar mensajes de error anteriores
       document.getElementById("mensaje-categoria").innerHTML = "";
       document.getElementById("mensaje-seleccion-prov").innerHTML = "";
    
   
   
       // Validar el nombre
       if (categoria == null || categoria.length == 0) {
           document.getElementById("mensaje-categoria").innerHTML = "⚠️ El campo nombre es obligatorio";
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

function mostrarFormularioEdicion(id, nombre, proveedor) {
    document.getElementById('edit_id').value = id;
    document.getElementById('edit_nombre').value = nombre;
    document.getElementById('edit_proveedor').value = proveedor;
    document.getElementById('formularioEdicion').style.display = 'block';
}
function ocultarFormularioEdicion() {
    document.getElementById('formularioEdicion').style.display = 'none';
}