producto = [[1, "mangos"]]
print(producto)

def addProduct():
    nombre = input("Ingrese el nombre del producto: ")
    if not producto:
        ultimo_id=1
    else:
        ultimo_id = producto[-1][0] + 1
    nuevo_producto = [ultimo_id, nombre]
    producto.append(nuevo_producto)
    print("Producto registrado exitosamente.")

def ListaProductos():
    print("Como desea buscar los productos?")
    print("1- orden alfabetico (a)")
    print("2- orden inverso (b)")
    print("3- orden por ID (c)")
    opcion = input("Seleccione una opción: ")
    if opcion == 'a':
        productos_ordenados = sorted(producto, key=lambda x: x[1])
        print(productos_ordenados)
    elif opcion == 'b':
        productos_ordenados = sorted(producto, key=lambda x: x[1], reverse=True)
        print(productos_ordenados)
    elif opcion == 'c':
        productos_ordenados = sorted(producto, key=lambda x: x[0])
        print(productos_ordenados)
    else:
        print("Opción no válida. Mostrando en orden original.")
        productos_ordenados = producto
def modificarProducto():
    nombreProdcuto =  input("Ingrese el nombre del producto a modificar: ")
    for prod in producto:
        if prod[1] == nombreProdcuto:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            prod[1] = nuevo_nombre
            print("Producto modificado exitosamente.")
            return
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Buscar Producto")
        print("4. Modificar Producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            addProduct()
        elif opcion == '2':
            ListaProductos()
        elif opcion == '3':
            buscarProducto()
        elif opcion == '4':
            modificarProducto()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
def buscarProducto():
    nombreProdcuto =  input("Ingrese el nombre del producto a buscar: ")
    for prod in producto:
        if prod[1] == nombreProdcuto:
            print(f"Producto encontrado: ID: {prod[0]}, Nombre: {prod[1]}")
            return


main()


