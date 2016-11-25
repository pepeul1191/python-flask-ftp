//Función que lista los roles de un usuario especifico como tambien los roles que no tiene.
db.system.js.save(
   {
     _id : "listar_roles_usuario" ,
     value : function (id_usuario){ 
       var roles = db.roles.find(); roles.sort({"nombre":1})
       var usuario = db.usuarios.find({"_id" : ObjectId(id_usuario)});
       var usuario_roles= usuario[0]["roles"];
       var rpta = [];
       
       if(usuario_roles.length > 0){
         roles.forEach(
           function(rol){
             var existe = false;
             usuario_roles.forEach(
               function(usuario_rol){
                 if(usuario_rol["_id"].valueOf() === rol["_id"].valueOf()){
                   existe = true;
                 }
               }
             )
             rol["existe"] = existe;
             rpta.push(rol);
           }
         )
       }else{
         roles.forEach(
           function(rol){
             rol["existe"] = false;
             rpta.push(rol);
           }
         )
       }
       
       return rpta;
     }
   }
);