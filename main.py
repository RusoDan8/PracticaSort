nombre = ""
puesto = ""
salario = 0.0
empleados = [[1, 'juan',"Gerente", 300.0], [2, 'pedro',"Abogado",200.0], [3, 'maria',"Secretaria",100.0]]

def agregarEmpleado():

    print("Lista inicial:", empleados)
    nombre = input("Ingrese el nombre del nuevo empleado: ")
    ultimo_id = empleados[-1][0]
    nuevo_empleado = [ultimo_id + 1, nombre]
    empleados.append(nuevo_empleado)

def listaEmpleados():
    print("Lista actualizada:", empleados)
def buscarEmpleado():
    nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
    for empleado in empleados:
        if empleado[1] == nombre_buscar:
            print(f"Empleado encontrado: ID: {empleado[0]}, Nombre: {empleado[1]}")
            return

def main():
    opcion = ''
    while opcion != '4':
        opcion = input("Ingrese 1 para agregar un empleado o 2 para ver la lista de empleados, 3 buscar empleado: ")
        if opcion == '1':
                agregarEmpleado()

        elif opcion == '2':
                listaEmpleados()
        elif opcion == '3':
                buscarEmpleado()
        elif opcion == '4':
                print("Saliendo del programa.")
        else:
                print("Opción no válida. Por favor ingrese 1 o 2.")


main()
