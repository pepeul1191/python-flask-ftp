//Función que elimina en cascada los items de un subtitulo, como también el subtitulo, siendo el parámetro el _id del subtitulo a eliminar. La coleción 'menus' tiene la estructura de árbol. 
db.system.js.save(
   {
     _id : "subtitulo_eliminar_cascada" ,
     value : function (id_subtitulo){ 
       var items = db.menus.find({"parent" : id_subtitulo});
       
       items.forEach(
         function(item){
           db.menus.remove({"_id" : item["_id"]});
         }
       );
             
       db.menus.remove({"_id" : ObjectId(id_subtitulo)});
     }
   }
);