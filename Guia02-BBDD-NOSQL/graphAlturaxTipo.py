from pymongo import MongoClient
import json

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 28017)
db = client['pokeapi']  # Nombre de la base de datos
collection = db['pokemon']  # Nombre de la colección

pipeline = [
    {"$unwind": "$types"},
    {"$group": {"_id": "$types.type.name", "avg_height": {"$avg": "$height"}}}
]


result = list(collection.aggregate(pipeline))
for doc in result:
    print(doc)

#print('Ls suma es '  + str(sum([doc["count"] for doc in result])))
# Preparar los datos para el gráfico

#data = [{"type": doc["_id"], "count": doc["count"]} for doc in result]
#data = [{"type": doc["_id"], "avg_hp": doc["avg_hp"], "avg_attack": doc["avg_attack"], "avg_defense": doc["avg_defense"]} for doc in result]

#data = [{"generation": doc["generation"], "num_types": doc["num_types"]} for doc in result]

data = [{"type": doc["_id"], "avg_height": doc["avg_height"]} for doc in result]

# Convertir los datos a formato JSON
data_json = json.dumps(data)

# Crear un archivo HTML para mostrar el gráfico utilizando D3.js
# Crear un archivo HTML para mostrar el gráfico utilizando D3.js
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokémon Types</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <h1>Pokémon Types</h1>
    <div id="chart"></div>
    <script>
        const data = {};

        const margin = {{ "top": 20, "right": 30, "bottom": 40, "left": 90 }};
        const width = 600 - margin.left - margin.right;
        const height = 400 - margin.top - margin.bottom;

        const svg = d3.select("#chart")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        const x = d3.scaleBand()
            .domain(data.map(d => d.type))
            .range([0, width])
            .padding(0.1);

        // Modificar la escala y para que refleje el rango de alturas
        const y = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.avg_height) * 1.1])  // Multiplicar por 1.1 para agregar un poco de espacio en la parte superior del gráfico
            .range([height, 0]);


        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .selectAll("text")
            .attr("transform", "rotate(-45)")
            .style("text-anchor", "end");

        svg.append("g")
            .call(d3.axisLeft(y));

        svg.selectAll(".bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", d => x(d.type))
            .attr("y", d => y(d.avg_height))
            .attr("width", x.bandwidth())
            .attr("height", d => height - y(d.avg_height));
    </script>
</body>
</html>
""".format(data_json)



# Guardar el contenido HTML en un archivo
with open("pokemon_typesXaltura.html", "w") as file:
    file.write(html_content)

print("El archivo HTML con el gráfico de barras se ha generado exitosamente.")
