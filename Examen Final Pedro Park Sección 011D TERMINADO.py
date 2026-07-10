

planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159900, 2],
    'F006': [18990, 15]
}

def leer_opcion():

    try:
        opcion = int(input("Ingrese una opción (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None

def buscar_code(codigo):

    if codigo in inscripciones:
        return True
    return False

def validar_code(codigo):

    if codigo.strip() == "" or buscar_code(codigo):
        return False
    return True

def validar_nom(nombre):
    if nombre.strip() == "":
        return False
    return True

def validar_tipo(tipo):
    if tipo in ['mensual', 'trimestral', 'anual']:
        return True
    return False

def validar_dura(duracion):
    if duracion > 0:
        return True
    return False

def validar_horario(horario):
    if horario.strip() == "":
        return False
    return True

def validar_p(precio):
    if precio > 0:
        return True
    return False

def validar_cupos(cupos):
    if cupos >= 0:
        return True
    return False

def cupos_tipo(tipo_buscar):
    total_de_cupos = 0
    tipo_buscar = tipo_buscar.lower()
    
    for codigo, datos_plan in planes.items():
        tipo_plan = datos_plan[1]
        
        if tipo_plan == tipo_buscar:
            datos_inscripcion = inscripciones[codigo]
            cupos = datos_inscripcion[1]
            total_de_cupos = total_de_cupos + cupos
            
    print(f"\nTotal de cupos disponibles para planes de tipo '{tipo_buscar}': {total_de_cupos}")

def busqueda_precio(p_min, p_max):
    resultados_busqueda = []
    
    for codigo, datos_inscripcion in inscripciones.items():
        precio = datos_inscripcion[0]
        cupos = datos_inscripcion[1]

        if p_min <= precio <= p_max and cupos > 0:
            datos_de_plan = planes[codigo]
            nombre_plan = datos_de_plan[0]

            formato = f"{nombre_plan}-{codigo}"
            resultados_busqueda.append(formato)
            
    if len(resultados_busqueda) == 0:
        print("No hay planes en ese rango de precios.")
    else:

        resultados_busqueda.sort()
        print("\nPlanes encontrados (ordenados alfabéticamente):")
        for plan in resultados_busqueda:
            print(f"- {plan}")

def actualizar_precio(codigo, nuevo_p):
    if buscar_code(codigo):
        inscripciones[codigo][0] = nuevo_p
        return True
    return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]
    print("¡Plan registrado con éxito!")

def eliminar_plan(codigo):
    if buscar_code(codigo):
        del planes[codigo]
        del inscripciones[codigo]
        return True
    return False

while True:
    print("\n============= MENÚ PRINCIPAL ============= \n1. Cupos por tipo de plan \n2. Búsqueda de planes por rango de precio \n3. Actualizar precio de plan \n4. Agregar plan \n5. Eliminar plan \n6. Salir \n==========================================")
    
    op = leer_opcion()
    
    if op == 1:
        tipo = input("Ingrese el tipo de plan (mensual, trimestral, anual): ")
        cupos_tipo(tipo)
        
    elif op == 2:
        try:
            p_min = int(input("Ingrese el precio mínimo: "))
            p_max = int(input("Ingrese el precio máximo: "))
            
            if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max)
            else:
                print("\nError: Los valores deben ser mayores a cero y el mínimo menor o igual al máximo.")
        except ValueError:
            print("Debe ingresar valores enteros")
            
    elif op == 3:
        while True:
            codigo = input("Ingrese el código del plan a modificar: ").upper()
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio mensual: "))
                if nuevo_precio > 0:
                    resultado = actualizar_precio(codigo, nuevo_precio)
                    if resultado == True:
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("\nError: El precio debe ser un entero positivo.")
            except ValueError:
                print("\nError: El precio debe ser un número entero.")
                
            resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
            if resp == 'n':
                break
                
    elif op == 4:
        print("\n--- Formulario para Agregar Nuevo Plan ---")
        codigo = input("Código: ").upper()
        if not validar_code(codigo):
            print("\nError: Código vacío o ya existente en el sistema.")
            continue
            
        nombre = input("Nombre del plan: ")
        if not validar_nom(nombre):
            print("\nError: El nombre no puede estar vacío.")
            continue
            
        tipo = input("Tipo (mensual, trimestral, anual): ").lower()
        if not validar_tipo(tipo):
            print("\nError: Tipo inválido.")
            continue
            
        try:
            duracion = int(input("Duración en meses: "))
            if not validar_dura(duracion):
                print("\nError: La duración debe ser mayor a 0.")
                continue
        except ValueError:
            print("\nError: Debe ingresar un número entero.")
            continue
            
        piscina_input = input("¿Incluye piscina? (s/n): ").lower()
        if piscina_input == 's':
            acceso_piscina = True
        elif piscina_input == 'n':
            acceso_piscina = False
        else:
            print("Error: Debe ingresar 's' o 'n'.")
            continue
            
        clases_input = input("¿Incluye clases grupales? (s/n): ").lower()
        if clases_input == 's':
            incluye_clases = True
        elif clases_input == 'n':
            incluye_clases = False
        else:
            print("\nError: Debe ingresar 's' o 'n'.")
            continue
            
        horario = input("Horario (libre, mañana, tarde, noche): ")
        if not validar_horario(horario):
            print("\nError: El horario no puede estar vacío.")
            continue
            
        try:
            precio = int(input("Precio mensual: "))
            if not validar_p(precio):
                print("\nError: El precio debe ser mayor a 0.")
                continue
        except ValueError:
            print("\nError: Debe ingresar un número entero.")
            continue
            
        try:
            cupos = int(input("Cantidad de cupos: "))
            if not validar_cupos(cupos):
                print("\nError: Los cupos deben ser mayores o iguales a 0.")
                continue
        except ValueError:
            print("\nError: Debe ingresar un número entero.")
            continue
            
        agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos)
        
    elif op == 5:
        print("\n--- Eliminar Plan de Membresía ---")
        codigo = input("Ingrese el código del plan que desea eliminar: ").upper()
        fue_eliminado = eliminar_plan(codigo)
        
        if fue_eliminado == True:
            print(f"\n¡El plan {codigo} ha sido eliminado con éxito del sistema!")
        else:
            print("\nError: El código de plan ingresado no existe.")
        
    elif op == 6:
        print("\n¡Gracias por usar FitPass!")
        break