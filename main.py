
empleados = {}

def registrar_empleado():
    id_empleado = input("Ingrese ID del empleado: ")
    if id_empleado in empleados:
        print("Ya existe un empleado con ese ID.")
        return
    
    nombre = input("Ingrese nombre del empleado: ")
    correo = input("Ingrese correo del empleado: ")
    telefono = input("Ingrese teléfono del empleado: ")
    valor_hora = int(input("Ingrese el valor por hora: "))
    horas = int(input("Ingrese el número de horas trabajadas: "))
    cargo = input("Ingrese el cargo del empleado: ")

    empleados[id_empleado] = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "valor_hora": valor_hora,
        "horas": horas,
        "cargo": cargo
    }
    print("Empleado registrado correctamente.")

def ver_empleados():
    if not empleados:
        print(" No hay empleados registrados.")
        return
    print("\n--- Lista de empleados ---")
    for id_empleado, datos in empleados.items():
        salario = datos["valor_hora"] * datos["horas"]
        print(f"ID: {id_empleado} | Nombre: {datos['nombre']} | Cargo: {datos['cargo']} | Salario: {salario:,.2f}")

def total_nomina():
    total = sum(datos["valor_hora"] * datos["horas"] for datos in empleados.values())
    print(f"\n El total de la nómina es: ${total:,.2f}")

def eliminar_empleado():
    id_empleado = input("Ingrese el ID del empleado a eliminar: ")
    if id_empleado in empleados:
        del empleados[id_empleado]
        print(" Empleado eliminado correctamente.")
    else:
        print(" No existe un empleado con ese ID.")


while True:
    print("\n===== MENÚ NOMINA =====")
    print("1. Registrar empleado")
    print("2. Ver todos los empleados")
    print("3. Ver total nómina")
    print("4. Eliminar empleado por ID")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        ver_empleados()
    elif opcion == "3":
        total_nomina()
    elif opcion == "4":
        eliminar_empleado()
    elif opcion == "5":
        print(" Saliendo del sistema...")
        break
    else:
        print(" Opción inválida, intente de nuevo.")
