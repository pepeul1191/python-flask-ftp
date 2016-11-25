//Función que agrega un permiso a un rol, siempre y cuando no lo tenga
db.system.js.save(
{
  _id : "asociar_permiso" ,
  value : function (id_rol, id_permiso){ 
    var rol = db.roles.find({"_id" : ObjectId(id_rol)});
    var permisos = rol["permisos"];
    var c = db.roles.find({$and:[{"_id" : ObjectId(id_rol)},{"permisos" : { $elemMatch : {"_id" : ObjectId(id_permiso)}}}]}).count();
        
    if(c == 0){
      var permiso_nuevo = db.permisos.findOne({"_id" : ObjectId(id_permiso)});
      db.roles.update({ '_id': ObjectId(id_rol) }, { $push : {
          "permisos" : permiso_nuevo
      } });
    }
    
  }
}
);