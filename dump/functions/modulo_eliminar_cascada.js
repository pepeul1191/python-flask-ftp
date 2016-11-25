//Función que elimina en cascada los subtitulos y los items de dichos subtitulos, como también el módulo, siendo el parámetro el _id del módulo a eliminar. La coleción 'menus' tiene la estructura de árbol. 
db.system.js.save(
   {
     _id : "modulo_eliminar_cascada" ,
     value : function (id_modulo){ 
       var subtitulos = db.menus.find({"parent" : id_modulo});
       
       subtitulos.forEach(
         function(subtitulo){
           var id_subtitulo = subtitulo["_id"].valueOf();
           var items = db.menus.find({"parent" : id_subtitulo});
           
           items.forEach(
             function(item){
               db.menus.remove({"_id" : item["_id"]});
             }
           );
             
           db.menus.remove({"_id" : subtitulo["_id"]});
         }
       );
         
       db.menus.remove({"_id" : ObjectId(id_modulo)});
     }
   }
);