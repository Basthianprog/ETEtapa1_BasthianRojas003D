//validar formulario

function validacion()
{
    //variables
    nom= document.getElementById('nom').value;
    ape= document.getElementById('ape').value;
    var s="no"

    //Validar si cuadro texto nombre esta vacio
    if(nom == null || nom.length==0 || /^\s+$/.test(nom))
    {
        alert('Error... debe ingresar un nombre');
        document.getElementById('nom').value="";
        document.datos.nombre.focus();
        return false;
    }

    //Validar si cuadro texto apellido esta vacio
    if(ape == null || ape.length==0 || /^\s+$/.test(ape))
    {
        alert('Error... debe ingresar un apellido');
        document.getElementById('ape').value="";
        document.datos.apellido.focus();
        return false;
    }

    //validar si se ha seleccionado las opciones si/no
    for(var i=0;i<document.datos.respuesta.length;i++)
    {
        if(document.datos.respuesta[i].checked){
            s="si"
        }
    }

    if(s=="no"){
        alert('Debe seleccionar si o no')
        return false;
    }
    
    return true;
}