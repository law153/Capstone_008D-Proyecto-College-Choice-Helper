$(document).ready(function() {
    $("form").submit(function(e) {
        let clave = $("#id_new_password1").val();
        let clave2 = $("#id_new_password2").val();

        let msj = "";
        let error = false;

        // Validaciones
        if (!clave.trim()) {
            msj += "Debe ingresar una contraseña.<br>";
            error = true;
        } else {
            if (clave.length < 8 || clave.length > 20) {
                msj += "La contraseña debe tener entre 8 y 20 caracteres.<br>";
                error = true;
            }
            if (!/[A-Z]/.test(clave)) {
                msj += "Debe contener al menos una letra mayúscula.<br>";
                error = true;
            }
            if (!/[a-z]/.test(clave)) {
                msj += "Debe contener al menos una letra minúscula.<br>";
                error = true;
            }
            if (!/[0-9]/.test(clave)) {
                msj += "Debe contener al menos un número.<br>";
                error = true;
            }
            if (!/[\W_]/.test(clave)) {
                msj += "Debe contener al menos un carácter especial.<br>";
                error = true;
            }
        }

        // Confirmación de contraseña
        if (clave !== clave2) {
            msj += "Las contraseñas no coinciden.<br>";
            error = true;
        }

        // Mostrar error si hay
        if(error){
            $("#alerta").html(msj);
            e.preventDefault();

        }else{
            $("#alerta").html("");
        }
    });
});
