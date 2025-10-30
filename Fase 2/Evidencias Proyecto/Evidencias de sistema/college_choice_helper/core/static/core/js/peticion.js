$(document).ready(function(){

    $("#crear-peticion").submit(function(e){

        /* Variables */

        var asunto = $("#asunto").val();
        var asunto_msj = $("#mensaje").val();
        let msj = "";
        let enviar = false;

        msj = "";


        /* Validaciones del asunto*/
        if(asunto.trim().length === 0){
            msj += "Debe llenar este campo<br>";
            enviar = true;
        }else{

            if(asunto.trim().length < 4 || asunto.trim().length > 12){
                msj += "El asunto debe contener entre 4 y 50 caracteres<br>";
                enviar = true;
            }

            if(!tieneMayus(asunto)){
                msj += "El asunto debe contener al menos una mayúscula<br>";
                enviar = true;
            }

            if(!tieneMinus(asunto)){
                msj += "El asunto debe contener al menos una minúscula<br>";
                enviar = true;
            }

            
        }

        if(enviar){
            $("#alerta").html(msj);
            e.preventDefault();

        }else{
            $("#alerta").html("");
        }

        msj="";

        /* Fin validaciones del asunto */

        /* Validaciones del asunto_msj*/
        if(asunto_msj.trim().length === 0){
            msj += "Debe llenar este campo<br>";
            enviar = true;
            
        }else{

            if(asunto_msj.trim().length < 4 || asunto_msj.trim().length > 300){
                msj += "El mensaje debe contener entre 4 y 300 caracteres<br>";
                enviar = true;
            }

            if(!tieneMayus(asunto_msj)){
                msj += "El mensaje debe contener al menos una mayúscula<br>";
                enviar = true;
            }

            if(!tieneMinus(asunto_msj)){
                msj += "El asunto debe contener al menos una minúscula<br>";
                enviar = true;
            }
        }

        /* Fin validaciones del asunto_msj */

        if(enviar){
            $("#alerta2").html(msj);
            e.preventDefault();

        }else{
            $("#alerta2").html("");
        }

        msj=""
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
});