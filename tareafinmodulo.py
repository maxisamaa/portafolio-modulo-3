
tarea=[]
def agregarTarea(lista):
    tarea=input("introduzca descripcion tarea")
    lista.append(tarea)
    print("tarea anadida correctamente")
    print("la tarea anadida es :",tarea)
    print(f'la tarea se almaceno en la posicion {len(lista)}')
def verTarea(lista):
    if lista==False: # no hay elementos en la lista
        print("la lista esta vacia")
    else:
        print(f'hay {len(lista)} tareas incompletas')
        for indice,tarea in enumerate(lista):    
            print(f'{indice+1}-{tarea}')
def completarTareas(lista):
    verTarea(lista)
    completada=int(input("ingrese  el indice de la tarea completada"))
    if completada>0 and completada<=len(lista):
        if "completada" in lista[completada-1]:
            print("la tarea indicada ya esta actualemente completada")
        else:
            lista[completada-1]=lista[completada-1]+"(completada)"
            print(f"se marco la tarea {lista[completada-1][:-12]} como completada")
    else:
        print("opcion invalida") 
def eliminarTareas(lista):
    verTarea(lista)
    eliminada=int(input("que tarea desea eliminar?"))
    if lista==False:
        print("no hay tareas que eliminar")
    else:
        if eliminada>0 and eliminada<=len(lista):
           del lista[eliminada-1]
        else:
            print("ingrese caracter valido")
            print("se elimino la tarea.")


# CICLO PRINCIPAL

contador = 0
while True:
    print("\n--- Ordena tus tareas!---\n")
    print("1. agregar tarea")
    print("2. ver tareas ")
    print("3.marcar tarea como completada")
    print("4.eliminar tarea")
    print("5. Salir\n")

    opcion = input("Selecciona una opción (1-5): ") # por defecto es string

    if opcion == "5":
        print("\n Gracias por usar la calculadora. ¡Hasta luego!\n")
        break
    elif opcion == "1":
        agregarTarea(tarea)
    elif opcion == "2":
        verTarea(tarea)
    elif opcion == "3":
        completarTareas(tarea)
    elif opcion == "4":
        eliminarTareas(tarea)
    else:
        print("Opción inválida. Intenta nuevamente.")
    
    contador += 1
    print(f"Has usado la calculadora {contador} vez/veces.")


