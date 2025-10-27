##Pregunta 1
#cristian = {"Acción", "Fantasía", "Documental", "Comedia", "Ciencia ficción"}
#antonio = {"Biografía", "Comedia", "Documental", "Drama", "Infantil", "Musical"}
#TgcOA=cristian | antonio #todos que estan
#yy=cristian & antonio #solo los que intersectan, estan en ambos
#print(TgcOA)
#print(yy)

#Pregunta 2
#dict = {}
## Uso una tupla como llave
#dict[(2, 5)] = "Python"
## Vuelvo a usar la misma tupla como llave
#dict[(2, 5)] = "Javascript"
#print(dict[(2, 5)])

#Pregunta3
#semana = {'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'}
#feriados = ['Jueves', 'Sabado']
#for día in feriados:
#    semana.discard(día)
#dias_restantes = len(semana)
#print(dias_restantes)

#Pregunta 4
#Explicación técnica:
#Sets y diccionarios en Python se implementan sobre tablas hash, lo que permite que las operaciones de búsqueda,
#inserción y eliminación tengan una complejidad promedio de O(1).
#En cambio, las estructuras secuenciales como listas o tuplas necesitan recorrer los elementos uno por uno para buscar
#un valor → complejidad O(n).
#
#Por qué no las otras:
#
#a. ❌ No generan un “orden óptimo” automáticamente; los set ni siquiera garantizan orden.
#b. ❌ Las listas y tuplas también pueden almacenar distintos tipos de datos.
#c. ❌ No tienen mayor capacidad de elementos que las secuenciales; el límite depende de la memoria, no del
#tipo de estructura.
#👉 En resumen: el gran beneficio real es la eficiencia en la búsqueda.

#Pregunta 5
#¿Cuál opción define correctamente la acción de agregar elementos (que no sean sets) a un set ya creado,
#el cual se encuentra en la variable “conjunto”? Pregunta 5Respuesta a. conjunto.add(elemento) b. conjunto.
#append(elemento) c. conjunto[elemento] = elemento d. conjunto = conjunto + elemento

#respuesta
#a. conjunto.add(elemento)

#Pregunta 6
#¿Cuál de las siguientes afirmaciones es siempre correcta cuando recorremos los elementos de un
#set o conjunto?
#
#Pregunta 6Respuesta
#ESTA ES LA RESPUESTA: a.Cada elemento será visitado exactamente una vez.
#b.Los elementos serán visitados en el orden que fueron ingresados.
#c.Cada elemento será visitado exactamente la cantidad de veces que haya sido ingresado al set previamente.
#d.Nunca podemos asegurar el orden en que serán visitados los elementos, ni cuantas veces será visitado
# cada uno.

#Pregunta 7
#cristian = {"Acción", "Fantasía", "Documental", "Comedia", "Ciencia ficción"}
#antonio = {"Biografía", "Comedia", "Documental", "Drama", "Infantil", "Musical"}
##De las siguientes alternativas, marque la que permite responder la consulta: “Todos los géneros
## que le gustan a Cristian, pero no a Antonio”:
#respuesta=cristian - antonio
#print(respuesta)

#Pregunta 8
#De los siguientes valores, ¿cuales pueden ser una llave de un diccionario?
#
#En Python, una llave de diccionario debe ser inmutable y hashable.
#Analicemos cada caso:
#
#I. "Junio" ✅
#Los str son inmutables y hashables → válido.
#
#II. [10, "Julio"] ❌
#Una lista es mutable → no puede ser llave.
#
#III. (10, "Junio") ✅
#Una tupla es inmutable y hashable (mientras sus elementos lo sean, y en este caso sí lo son:
#int y str) → válido.
#
#IV. (10, ["Junio", "Julio"]) ❌
#Aunque la estructura externa es una tupla, dentro contiene una lista (mutable) → no es hashable →
#inválido.
#
#✅ Correcto: I y III
#👉 Respuesta: d. I y III

#Pregunta 9

#¿En qué caso ocurre el error de tipo KeyError? Pregunta 9
#
#a. Cuando ya no quedan más llaves disponibles para usar en un diccionario.
#b. Cuando se trata de acceder a un diccionario usando una llave que no existe en este. RESPUESTA CORRECTA
#c. Cuando tratamos de usar un valor no hasheable como llave en un diccionario.
#d. Cuando tratamos de agregar un par llave-valor a un set o conjunto.

#PREGUNTA 10
#¿Cuál de las siguientes opciones representa un código que revisa si un valor V está en un diccionario dict?
#I.
#if V in dict:
#    return True
#II. for valor in dict:
#    if valor == V:
#        return True
#III. for valor in dict.values():
#    if valor == V:
#        return True
#
#Respuestab. Solo III ✅ ya que pregunta por valor

