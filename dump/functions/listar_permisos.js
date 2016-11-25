//Función que lista los permisos de un rol especifico como tambien los permisos que no tiene.
db.system.js.save(
   {
     _id : "listar_permisos" ,
     value : function (id_rol){ 
       var permisos = db.permisos.find(); permisos.sort({"nombre":1})
       var rol = db.roles.find({"_id" : ObjectId(id_rol)});
       var rol_permisos = rol[0]["permisos"];
       var rpta = [];
       
       if(rol_permisos.length > 0){
         permisos.forEach(
           function(permiso){
             var existe = false;
             rol_permisos.forEach(
               function(rol_permiso){
                 if(rol_permiso["_id"].valueOf() === permiso["_id"].valueOf()){
                   existe = true;
                 }
               }
             )
             permiso["existe"] = existe;
             rpta.push(permiso);
           }
         )
       }else{
         permisos.forEach(
           function(permiso){
             permiso["existe"] = false;
             rpta.push(permiso);
           }
         )
       }
       
       return rpta;
     }
   }
);