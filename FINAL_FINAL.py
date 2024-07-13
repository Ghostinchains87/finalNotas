import csv

def obtener_fichero_calificaciones():
    lista = []
    with open(r"F:\DUOC\FUNDAMENTOS DE PROGRAMACION/notas_alumnos.csv","r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos =0
        for linea in lector_csv:
            if pos !=0:
                curso = linea[0].strip()
                rut = linea[1].replace(' ','')
                nombre = linea[2].strip()
                nota1 = float(linea[3].replace(',','.'))
                nota2 = float(linea[4].replace(',','.'))
                nota3 = float(linea[5].replace(',','.'))
                lista.append({
                    "curso": curso,
                    "rut": rut,
                    "nombre": nombre,
                    "nota1": nota1,
                    "nota2": nota2,
                    "nota3": nota3,
                    "promedio" : round((nota1+nota2+nota3)/3,1)
                })
            else:
                pos = 1
        return lista

def burbuja(arreglo):
  longitud =len(arreglo)
  for i in range(longitud):
    for indice_actual in range(longitud -1):
      indice_siguiente_elemnto = indice_actual + 1
      if arreglo[indice_actual]["promedio"] < arreglo[indice_siguiente_elemnto]["promedio"]:
        arreglo[indice_siguiente_elemnto], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemnto]

def menu_principal():
    opcion = ''
    while opcion!= '6':
        print('Seleccione una opción:')
        print('1) Consultar Notas y promedio de un alumno dado su rut')
        print('2) Visualizar alumno con promedio de notas menor a 4.0')
        print('3) Visualizar alumno con promedio de notas menor a 4.0 de un curso')
        print('4) Generar archivo alumnos con sus notas y promedios de un curso')
        print('5) Generar archivo alumnos con mayores promedios (5 alumnos) por curso')
        print('6) Salir')

        opcion = input('Opción: ')

        match opcion:
            case '1':
                visualizar_notas_rut()
            case '2':
                visualizar_alumnos_menor4()
            case '3':
                visualizar_alumnos_4_curso()
            case '4':
                generar_archivo()
            case '5':
                generar_alumnos_top_curso()
            case '6':
                salir()
            case _:
                print('Opción incorrecta, vuelva a intentarlo.')

def visualizar_notas_rut():
    lista = obtener_fichero_calificaciones()
    rut_Ingreso = input("Ingrese el rut del alumno ").strip()
    for alumnos in lista:
        if rut_Ingreso == alumnos['rut']:
            print(f"Alumno {alumnos['nombre']} : nota1 {alumnos['nota1']}  nota2 {alumnos['nota2']}  nota3 {alumnos['nota3']}  promedio {alumnos['promedio']}")
    input()        

def visualizar_alumnos_menor4():
    lista = obtener_fichero_calificaciones()
    rut_Ingreso = input("Ingrese el rut del alumno: ").strip()
    rut_encontrado = False
    for alumnos in lista:
        if alumnos['rut'] == rut_Ingreso and alumnos['promedio'] < 4:
            print(f"Curso {alumnos['curso']} Alumno {alumnos['nombre']} :  promedio {alumnos['promedio']}")
            rut_encontrado = True
    if not rut_encontrado:
        print("RUT no encontrado en la lista de alumnos.")
    input()

def visualizar_alumnos_4_curso():
    lista = obtener_fichero_calificaciones()
    valido = False
    while not valido:
        curso = input("Ingrese curso a visualizar: ").strip()
        cursos_existentes = [alumno['curso'] for alumno in lista]
        if curso in cursos_existentes:
            valido = True
            print(f"Alumnos del curso {curso} con promedio menor a 4:")
            for alumno in lista:
                if alumno['curso'] == curso and alumno['promedio'] < 4:
                    print(f"  {alumno['nombre']}: promedio {alumno['promedio']}")
        else:
            print("Curso no válido")
    input("Presione Enter para continuar...")

def generar_archivo():
    lista = obtener_fichero_calificaciones()
    curso_ingreso = input("Ingrese curso ").strip()
    with open('Salida.csv','w', newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")    
        escritor_csv.writerow(['Curso','Nombre','Nota1','Nota2','Nota3','Promedio'])
        for alumnos in lista:
            lista_imp=[]
            if alumnos['curso'] == curso_ingreso:
                lista_imp.append(alumnos['curso'])
                lista_imp.append(alumnos['nombre'])
                lista_imp.append(alumnos['nota1'])
                lista_imp.append(alumnos['nota2'])
                lista_imp.append(alumnos['nota3'])
                lista_imp.append(alumnos['promedio'])
                escritor_csv.writerow(lista_imp)
    input()

def generar_alumnos_top_curso():
    lista = obtener_fichero_calificaciones()
    curso_ingreso = input("Ingrese curso ").strip()
    burbuja(lista)
    
    # Crear lista temporal para almacenar promedios
    promedios = []
    
    # Recorrer lista y agregar promedios a la lista temporal
    for alumno in lista:
        if alumno['curso'] == curso_ingreso:
            promedios.append(alumno['promedio'])
    
    # Ordenar lista temporal de promedios en orden descendente
    promedios.sort(reverse=True)
    
    # Tomar los 5 primeros elementos de la lista ordenada
    top_promedios = promedios[:5]
    
    # Crear lista para almacenar los 5 mejores alumnos
    top_alumnos = []
    
    # Recorrer lista original y agregar los 5 mejores alumnos a la lista
    for alumno in lista:
        if alumno['curso'] == curso_ingreso and alumno['promedio'] in top_promedios:
            top_alumnos.append(alumno)
    
    with open('Salida.csv','w', newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")    
        escritor_csv.writerow(['Curso','Nombre','Nota1','Nota2','Nota3','Promedio'])
        for alumno in top_alumnos:
            lista_imp = []
            lista_imp.append(alumno['curso'])
            lista_imp.append(alumno['nombre'])
            lista_imp.append(alumno['nota1'])
            lista_imp.append(alumno['nota2'])
            lista_imp.append(alumno['nota3'])
            lista_imp.append(alumno['promedio'])
            escritor_csv.writerow(lista_imp)
    
    input()

def salir():
    print('Saliendo')

menu_principal()