app = Flask(__name__) # Creamos una instancia de flask #
api = Api(app) #Creamos la API #
PORT = 12345
host="127.0.0.1" #He querido dejar el mismo que en el enunciado #
import uvicorn
from fastapi import FastAPI
from pathlib import Path

@app.post("Tarea_1")
def add(string):
    dataBase = open("registro.txt", "a")
    dataBase.write(string + "\n")
    dataBase.close()
    return {"Respuesta":"Proceso creado correctamente"}

@app.get("/")
def read_root():
    return {"Tarea completada"}
if __name__ == "__main__":
    uvicorn.run(app)

import pickle # Con pickle guardamos la informacion de la cadena en un archivo externo #
todo = ['calcular_longitud_cadena']
pickle_file = file('archivo_pickle', 'w')
pickle.dump(todo, pickle_file)

import pickle # Restauramos desde el archivo el pickle #
pickle_file = file('archivo_pickle')
todo = pickle.load(pickle_file)
print(todo)

@app.get("/consulta")
def buscar(string):
    file = Path('registro.txt')
    file.touch(exist_ok=True)
    dataBase = open("registro.txt").read().splitlines()
    a,b = 'AEIOU','ÁÉÍÓÚ', 'aeiou', 'áéíóú' # Asi la aplicacion discrimina entre mayusculas, minusculas y tildes #
    i = 0
    trans = str.maketrans(a,b)
    for line in dataBase:
	    new_line = line.lower()
	    new_line = new_line.translate(trans)
	    if (string in new_line):
		    i += 1 
    print(i)
    return {"numero" : i} # No le he puesto la tilde a numero porque no se si lo esta cogiendo bien #