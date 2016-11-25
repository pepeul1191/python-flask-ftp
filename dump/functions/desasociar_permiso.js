//Función que quitar un permiso a un rol, siempre y cuando lo tenga
db.system.js.save(
{
  _id : "desasociar_permiso" ,
  value : function (id_rol, id_permiso){ 
    var rol = db.roles.find({"_id" : ObjectId(id_rol)});
    var permisos = rol["permisos"];
    var c = db.roles.find({$and:[{"_id" : ObjectId(id_rol)},{"permisos" : { $elemMatch : {"_id" : ObjectId(id_permiso)}}}]}).count();
        
    if(c == 1){
      db.roles.update({ '_id': ObjectId(id_rol) }, { $pull : {
          "permisos" : {"_id" : ObjectId(id_permiso)}
      } });
    }
    
  }
}
);