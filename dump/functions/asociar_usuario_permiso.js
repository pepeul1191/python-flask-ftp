//Función que agrega un permiso a un usuario, siempre y cuando no lo tenga
db.system.js.save(
{
  _id : "asociar_usuario_permiso" ,
  value : function (id_usuario, id_permiso){ 
    var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
    //var usuario_roles = usuario["roles"];
    var c = db.usuarios.find({$and:[{"_id" : ObjectId(id_usuario)},{"permisos" : { $elemMatch : {"_id" : ObjectId(id_permiso)}}}]}).count();
        
    if(c == 0){
      var permiso_nuevo = db.permisos.findOne({"_id" : ObjectId(id_permiso)});
      db.usuarios.update({ '_id': ObjectId(id_usuario) }, { $push : {
          "permisos" : permiso_nuevo
      } });
    }
    
  }
}
);