//Función que agrega los nombres de usuario repetidos
db.system.js.save(
{
  _id : "nombre_repetido" ,
  value : function (_id_usuario, nombre_usuario){ 
    var usuarios = db.usuarios.find({"usuario" : nombre_usuario});
    var repetido = [];
    var rpta = "actualizar";
    var pasadas = 0;
    usuarios.forEach(
      function(usuario){
        pasadas = pasadas + 1;
        rpta = "repetido";
        if (usuario["_id"].valueOf() == _id_usuario){
          //si no coinciden es que el nombre ya esta tomado por otro usuario, caso contrario pertenece al mismo
          rpta = "nada";
        }
      }
    )
    if (pasadas == 0){ rpta = "crear" }
    
    return rpta;
  }
}
);