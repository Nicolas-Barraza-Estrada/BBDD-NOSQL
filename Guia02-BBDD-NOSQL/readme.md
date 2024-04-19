# Guia 02## Requisitos

- Python 3.6 o superior
- MongoDB
- Libreria requests ('pip install requests')
- Libreria pymongo ('pip install pymongo')
- Libreria json (incluida en python)

## Descarga o Importación de la Base de Datos

1. En el archivo ***mongo_connection.py*** modifique en la linea 7 el puerto de su base de dato:   
 ```client = MongoClient('localhost', 28017)```
2. Opcionalmente, puede crear la base de datos e importar la colección `pokeapi.pokemon.json` ,y modifique las lineas 8 y 9 según corresponda.  
  `db = cliente["pokeapi"]`  
  `coleccion = db["pokemon"]`   
- **Sin embargo, al ejecutar el comando `pokeApi.py`, pymongo crearan la base de datos y una colección vacia si esta no existe, luego procedera a descargar los 1302 pokemon.**

## Uso de pokemon_por_tipo.py

1. Ejecute el programa con el comando `python3 pokemon_por_tipo.py` en su terminal o `python pokemon_por_tipo.py` si esta en windows.
2. Esto generara un archivo html que puede visualizar desde el navegador, el html contiene el grafico de la cantidad pokemon que hay por cada tipo. Este grafico no diferencia por tipos primario o secundario, e incluye los 1025 pokemon registrados con id en la popkedex, 147 formas regionales y 277 variantes causadas por objetos, estaciones, cambios de estadisticas, etc. 
3. El grafico contiene los siguientes datos:  
water: 186  
normal: 158  
grass: 152  
flying: 149  
psychic: 136  
electric: 110  
dragon: 107  
bug: 104  
fire: 103  
rock: 102  
poison: 102  
fighting: 100  
dark: 94  
ground: 93   
ghost: 92  
steel: 91  
fairy: 83  
ice: 66  
Ls suma es 2028 (debido a que hay solapamiento entre pokemon de un solo tipo y aquellos que poseen mas de uno)

## Uso de altura_por_tipo.py

1. Ejecute el programa con el comando `python3 altura_por_tipo.py` en su terminal o `python altura_por_tipo.py` si esta en windows.
2. Este grafico mostrara el promedio de altura por cada tipo de pokemon, conteniendo los siguientes datos:  
grass: 16.82236842105263  
ice: 18.272727272727273  
ghost: 14.728260869565217  
bug: 19.528846153846153  
poison: 33.705882352941174  
steel: 27.75824175824176  
normal: 15.664556962025317  
fairy: 19.40963855421687  
water: 22.758064516129032  
ground: 19.322580645161292  
fighting: 22.6  
psychic: 16.205882352941178  
flying: 16.59731543624161  
rock: 18.019607843137255  
dragon: 43.373831775700936  
electric: 16.490909090909092  
dark: 20.06382978723404  
fire: 28.990291262135923  
Se puede apreciar que los pokemon tipo dragon, por su propia naturaleza, tienen a ser mucho mas grande que el resto de tipo pokemon, miediendo en promedio 4.3 metros.