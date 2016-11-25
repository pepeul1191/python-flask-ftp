//Función que lista los permisos adicionales de un usuario especifico como tambien los permisos adicionales que no tiene.
db.system.js.save(
   {
     _id : "listar_permisos_usuario" ,
     value : function (id_usuario){ 
       var permisos = db.permisos.find(); permisos.sort({"nombre":1})
       var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
       var usuario_permisos = usuario[0]["permisos"];
       var rpta = [];
       
       if(usuario_permisos.length > 0){
         permisos.forEach(
           function(permiso){
             var existe = false;
             usuario_permisos.forEach(
               function(usuario_permiso){
                 if(usuario_permiso["_id"].valueOf() === permiso["_id"].valueOf()){
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