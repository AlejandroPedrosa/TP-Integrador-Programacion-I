def crear_arbol(valor):
    return [valor, [], []]

def insertar_izquierda(nodo, nuevo_valor):
    subarbol_izq = nodo[1]
    if subarbol_izq:
        nodo[1] = [nuevo_valor, subarbol_izq, []]
    else:
        nodo[1] = [nuevo_valor, [], []]

def insertar_derecha(nodo, nuevo_valor):
    subarbol_der = nodo[2]
    if subarbol_der:
        nodo[2] = [nuevo_valor, [], subarbol_der]
    else:
        nodo[2] = [nuevo_valor, [], []]

def imprimir_arbol_rotado(arbol, nivel=0):
    if arbol:
        imprimir_arbol_rotado(arbol[2], nivel + 1)
        print('   ' * nivel + str(arbol[0]))
        imprimir_arbol_rotado(arbol[1], nivel + 1)

def es_hoja(nodo):
    return nodo[1] == [] and nodo[2] == []

def listar_hojas(arbol, hojas=None):
    if hojas is None:
        hojas = []
    if arbol:
        if es_hoja(arbol):
            hojas.append(arbol[0])
        else:
            listar_hojas(arbol[1], hojas)
            listar_hojas(arbol[2], hojas)
    return hojas

#Recorrido preorden
def recorrido_preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        recorrido_preorden(arbol[1])
        recorrido_preorden(arbol[2])

#Recorrido inorden
def recorrido_inorden(arbol):
    if arbol:
        recorrido_inorden(arbol[1])
        print(arbol[0], end=' ')
        recorrido_inorden(arbol[2])

#Recorrido postorden
def recorrido_postorden(arbol):
    if arbol:
        recorrido_postorden(arbol[1])
        recorrido_postorden(arbol[2])
        print(arbol[0], end=' ')


# Construcción interactiva del árbol de roles dentro de una empresa
print("Vamos a crear una jerarquía corporativa por roles.")
empresa = crear_arbol(input("Ingrese el rol principal (ej: CEO): "))

# Primer nivel
insertar_izquierda(empresa, input(f"Ingrese el rol subordinado izquierdo del {empresa[0]} (ej: Directora de Finanzas): "))
insertar_derecha(empresa, input(f"Ingrese el rol subordinado derecho del {empresa[0]} (ej: Director de Tecnologia (CTO)): "))

# Segundo nivel
insertar_izquierda(empresa[1], input(f"Ingrese el rol subordinado izquierdo del {empresa[1][0]} (ej: Analista Contable): "))
insertar_derecha(empresa[1], input(f"Ingrese el rol subordinado derecho del {empresa[1][0]} (ej: Responsable de Auditoria): "))

# Segundo nivel
insertar_izquierda(empresa[2], input(f"Ingrese el rol subordinado izquierdo del {empresa[2][0]} (ej: Líder Backend): "))
insertar_derecha(empresa[2], input(f"Ingrese el rol subordinado derecho del {empresa[2][0]} (ej: Líder Frontend): "))

# Tercer nivel 
insertar_izquierda(empresa[2][1], input(f"Ingrese el rol subordinado izquierdo del {empresa[2][1][0]} (ej: Backend Jr.): "))
insertar_derecha(empresa[2][2], input(f"Ingrese el rol subordinado derecho del {empresa[2][2][0]} (ej: Frontend Jr.): "))

# Imprimir jerarquía rotada 90 grados
print("Estructura organizacional (vista rotada 90°):")
imprimir_arbol_rotado(empresa)

# Mostrar empleados sin subordinados
print("\nEmpleados sin subordinados (nodos hoja):")
print(", ".join(listar_hojas(empresa)))

# Mostrar recorrido preorden
print("\nRecorrido preorden: raíz - izquierda - derecha")
recorrido_preorden(empresa)

# Mostrar recorrido inorden
print("\nRecorrido inorden: izquierda - raíz - derecha")
recorrido_inorden(empresa)

# Mostrar recorrido postorden
print("\nRecorrido postorden: izquierda - derecha - raíz")
recorrido_postorden(empresa)
