$(document).ready(function(){

    $("#cambiarClave").submit(function(e){

        /*Variables*/
 
        var clave = $("#contrasena").val();

        let msj = "";
        let enviar = false;

        msj = "";

        /*Validaciones clave*/

        if(clave.trim().length === 0){
            
            msj += "Debe llenar este campo";
            enviar = true;

        } else{


            if(clave.trim().length < 8 || clave.trim().length > 20){
                msj += "La clave debe ser entre 8 y 20 caracteres<br>";
                enviar = true;
            }

            if(!tieneMayus(clave)){
                msj += "La clave debe contener al menos una mayuscula<br>";
                enviar = true;
            }

            if(!tieneMinus(clave)){
                msj += "La clave debe contener al menos una minuscula<br>";
                enviar = true;
            }

            if(!tieneNum(clave)){
                msj += "La clave debe contener al menos un número<br>";
                enviar = true;
            }

            if(!tieneEsp(clave)){
                msj += "La clave debe contener al menos un caracter especial<br>";
                enviar = true;
            }

        }
        
        if(enviar){
            $("#alerta").html(msj);
            e.preventDefault();

        }else{
            $("#alerta").html("");
        }

        
    });

    function tieneMayus(palabra){
        if(palabra.match(/[A-Z]/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneMinus(palabra){
        if(palabra.match(/[a-z]/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneNum(palabra){
        if(palabra.match(/[0-9]/)) {
            return true;
        } else{
            return false;
        }
    }

    function tieneEsp(palabra){
        if(palabra.match(/\W/)) {
            return true;
        } else{
            return false;
        }
    }

});
