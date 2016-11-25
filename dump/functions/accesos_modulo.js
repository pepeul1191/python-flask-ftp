//Función almacenada que genera un sólo documento que tiene los datos de la descripción del módulo, su lista de subtitulos (anidado) y los items de los subtitulos (anidado) recibiendo como parámetro el nombre del módulo. La coleción 'menus' tiene la estructura de árbol. 
db.system.js.save(
   {
     _id : "accesos_modulo" ,
     value : function (nombre_modulo){ 
       var menu = db.menus.find({"nombre" : nombre_modulo});
       var id_modulo = menu[0]["_id"].valueOf();
       var descripcion_modulo = menu[0]["descripcion"];
       var subtitulos = db.menus.find({"parent" : id_modulo});
       var array_subtitulos = [];
                
       subtitulos.forEach(
          function(subtitulo){
             var nombre_subtitulo = subtitulo["nombre"];
             var icono_subtitulo = subtitulo["icono"];
             var id_subtitulo = subtitulo["_id"].valueOf();
             var items = db.menus.find({"parent" : id_subtitulo});
             var items_array = [];
                              
             items.forEach(
                function(item){
                   var nombre_item = item["nombre"];
                   var url_item = item["url"];
                   var doc_item = {nombre : nombre_item, url: url_item}
                   items_array.push(doc_item);
                }
             );
                                  
             array_subtitulos.push(
                {nombre : nombre_subtitulo, icono : icono_subtitulo, items : items_array}
             );
          }
       );
         
       return {descripcion : descripcion_modulo, subtitulos : array_subtitulos};
     }
   }
);