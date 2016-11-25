//Función que quitar un rol un usuario, siempre y cuando lo tenga
db.system.js.save(
{
  _id : "desasociar_usuario_rol" ,
  value : function (id_usuario, id_rol){ 
    var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
    //var permisos = rol["permisos"];
    var c = db.usuarios.find({$and:[{"_id" : ObjectId(id_usuario)},{"roles" : { $elemMatch : {"_id" : ObjectId(id_rol)}}}]}).count();
        
    if(c == 1){
      db.usuarios.update({ '_id': ObjectId(id_usuario) }, { $pull : {
          "roles" : {"_id" : ObjectId(id_rol)}
      } });
    }
    
  }
}
);