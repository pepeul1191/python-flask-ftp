//Función que quitar un permiso a un usuario, siempre y cuando lo tenga
db.system.js.save(
{
  _id : "desasociar_usuario_permiso" ,
  value : function (id_usuario, id_permiso){ 
    var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
    //var permisos = rol["permisos"];
    var c = db.usuarios.find({$and:[{"_id" : ObjectId(id_usuario)},{"permisos" : { $elemMatch : {"_id" : ObjectId(id_permiso)}}}]}).count();
        
    if(c == 1){
      db.usuarios.update({ '_id': ObjectId(id_usuario) }, { $pull : {
          "permisos" : {"_id" : ObjectId(id_permiso)}
      } });
    }
    
  }
}
);