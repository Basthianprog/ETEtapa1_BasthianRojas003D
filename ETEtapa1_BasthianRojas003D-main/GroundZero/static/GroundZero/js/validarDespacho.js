//funcion validar formulario
function validacion()
{
    //variables
    reg= document.getElementById('region').value;
    com= document.getElementById('com').value;
    dic= document.getElementById('direccion').value;
    numdic= document.getElementById('numero').value;
    num= document.getElementById('telefono').value;
    nom= document.getElementById('nom').value;
    var s="no"

    //validar si no se ha seleccionado región
    if (reg == null || reg == 0)
    {
        alert('Seleccione una región');
        document.datos.region.focus();
        return false;
    }

    //validar si cuadro texto comuna esta vacio
    if(com == null || com.length==0 || /^\s+$/.test(com))
    {
        alert('Error... debe ingresar una comuna');
        document.getElementById('com').value="";
        document.datos.comuna.focus();
        return false;
    }

    //validar si cuadro texto dirección esta vacio
    if(dic == null || dic.length==0 || /^\s+$/.test(dic))
    {
        alert('Error... debe ingresar una dirección');
        document.getElementById('direccion').value="";
        document.datos.dic.focus();
        return false;
    }

    //validar si cuadro texto número dirección esta vacio
    if(isNaN(numdic) || numdic.length == 0)
    {
        alert('Error... debe ingresar un numero dirección válida');
        document.getElementById('numero').value="";
        document.datos.numdic.focus();
        return false;
    }

    //validar número telefónico
    if(!(/^\d{9}$/.test(num)) )
    {
        alert('Error...debe ingresar un teléfono válido');
        document.getElementById('telefono').value="";
        document.datos.fono.focus();
        return false;
    }
    
    //validar si cuadro texto nombre persona quien recibe esta vacio
    if(nom == null || nom.length==0 || /^\s+$/.test(nom))
    {
        alert('Error... debe ingresar un nombre');
        document.getElementById('nom').value="";
        document.datos.nombre.focus();
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