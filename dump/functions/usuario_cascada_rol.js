//Función que actualiza en cascada los roles de los usuarios
db.system.js.save(
{
  _id : "usuario_cascada_rol" ,
  value : function (id_rol){ 
    var rol = db.roles.findOne({"_id" : ObjectId(id_rol)});
    var usuarios = db.usuarios.find({'roles._id': ObjectId(id_rol)});
    usuarios.forEach(
      function(usuario){
        //print(usuario.roles);
        var usuario_roles = usuario.roles;
        var temp_roles = [];
        usuario_roles.forEach(
          function(usuario_rol){
            if(usuario_rol["_id"].valueOf() == ObjectId(id_rol)){
              temp_roles.push(rol);
            }else{
              temp_roles.push(usuario_rol);    
            }
          }
        );
        usuario.roles = temp_roles;
        db.usuarios.update({_id : usuario["_id"]}, usuario, { upsert: true });
      }
    );
  }
}
);