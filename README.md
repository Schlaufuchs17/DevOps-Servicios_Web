# Devops---Tarea-1
Se pide al alumno programar un servicio web. Este servicio web deberá escuchar en el puerto 12345 y expondrá dos endpoints:

    El primero recibe una cadena de caracteres, de longitud arbitraria, y la almacena en un fichero en disco.
    El segundo recibirá una única palabra (sin espacios). Se devolverá el número total de las cadenas del citado fichero que la contengan, sin tener en cuenta:
        Mayúsculas (CADENA == Cadena).
        Posibles acentos (avión == Avion).
        Múltiples apariciones en la misma cadena cuentan como una única.

Como requisito, el fichero donde se guardan los datos se debe persistir en disco y leerlo al arrancar el proceso. Si no existe, se creará vacío.

Si bien la elección del lenguaje de programación podría ser abierta, se exige que sea uno de los que se han mencionado hasta ahora:

    Java.
    Python.

Por sencillez, se recomienda usar Python, con el framework Flask (Enlaces a un sitio externo.). Pero es perfectamente posible usar el servicio Java expuesto en la lección para este ejercicio.
Ejemplo de llamadas
