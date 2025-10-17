$(document).ready(function(){

    $("#form_agregarInsti").submit(function(e){

        /*Variables*/
 
        var nombre = $("#nombre_insti").val();
        var comuna = $("#comuna_insti").val();
        var gratuidad = $("input[name='gratuidad']:checked").val();
        var web = $("#web_insti").val();

        let msj = "";
        let enviar = false;

        msj = "";

        /*Validaciones clave*/

        if( (nombre.trim().length === 0) || (comuna.trim().length === 0) || (web.trim().length === 0) || gratuidad === undefined ){
            
            msj += "Debe llenar todos los campos.";
            enviar = true;

        }
        
        if(enviar){
            $("#alerta").html(msj);
            e.preventDefault();

        }else{
            $("#alerta").html("");
        }

        
    });

});
