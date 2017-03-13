# encoding: utf-8

require "sqlite3"

def insertar_todos
    file = File.new('extensiones.txt', 'r')
    while (line = file.gets)
        line_array = line.split('::')
        extension = line_array[0][1..-1]
        mime = line_array[1].strip

        begin
            db = SQLite3::Database.open "db_archivos.db"
            db.execute('INSERT INTO extensiones (mime, extension) VALUES (?,?)', [mime, extension])
        rescue SQLite3::Exception => e 
            puts "Exception occurred"
            puts e
        ensure
            db.close if db
        end
    end
end

insertar_todos