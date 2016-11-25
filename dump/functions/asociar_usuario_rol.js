//Función que agrega un rol a un usuario, siempre y cuando no lo tenga
db.system.js.save(
{
  _id : "asociar_usuario_rol" ,
  value : function (id_usuario, id_rol){ 
    var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
    //var usuario_roles = usuario["roles"];
    var c = db.usuarios.find({$and:[{"_id" : ObjectId(id_usuario)},{"roles" : { $elemMatch : {"_id" : ObjectId(id_rol)}}}]}).count();
        
    if(c == 0){
      var rol_nuevo = db.roles.findOne({"_id" : ObjectId(id_rol)});
      db.usuarios.update({ '_id': ObjectId(id_usuario) }, { $push : {
          "roles" : rol_nuevo
      } });
    }
    
  }
}
);