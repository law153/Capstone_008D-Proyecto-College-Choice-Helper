$(document).ready(function(){

    $("#form_agregarCarrera").submit(function(e){

        /*Variables*/
 
        var nombre = $("#nombre_carrera").val();
        var costo = $("#costo").val();
        var puntaje = $("#puntaje").val();

        let msj = "";
        let enviar = false;

        msj = "";

        /*Validaciones clave*/

        if( (nombre.trim().length === 0)){
            
            msj += "Debe ingresar un nombre a la carrera.<br>";
            enviar = true;

        }

        if( (costo <= 0)){
            
            msj += "El costo no puede ser menor o igual a 0.<br>";
            enviar = true;

        }

        if( ( puntaje < 100 || puntaje > 1000) ){
            
            msj += "Ingrese un puntaje entre 100 y 1000.<br>";
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
