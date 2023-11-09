equipos={922610128901:['Maria F','',''],922610128902:['Miguel A','',''],922610128903:['Kevin L','',''],922610128904:['Santiago T','',''],922610128905:['Mathew G','',''],922610128906:['Maria P','',''],922610128907:['Kevin E','',''],922610128908:['Adriana L','',''],922610128909:['Sebastian P','',''],922610128910:['Sandra M','',''],9226101289:['Cristian A','',''],922610128912:['Matias G','',''],922610128913:['Kevin H','',''],922610128914:['Juan D','',''],922610128915:['Sebastian T','',''],922610128916:['Laura E','','']}

def dispositivos(clave, indice, valor):
  if clave in equipos:
      equipos[clave][indice] = valor
def novedad(clave, indice, valor):
 if clave in equipos:
     equipos[clave][indice] = valor
     print("\nNovedad actualizada :) ")
def recuperarId(valor):
  for clave, lista in equipos.items():
      if lista[0] == valor:
          return f"\nSu id es {clave}"
  return None
  
def menu():
  while True:
    print("Bienvenido al menu principal \n1.Para registrar un nuevo computador \n2.Para Registrar dispositivos a un equipo existente \n3.Para agregar una novedad \n4.Para eliminar una novedad \n5.Para eliminar un equipo \n6.Para consultar un equipo \n7.Para salir." )
    opc=input("\nDigite una opcion para continuar: ")
    if opc=="1":
      while True:
        print("\nHola, bienvenido al registro de computadores, ingrese el id del equipo y nombre del encargado")
        id=int(input("Digite el id del equipo: "))
        nombre=input("Digite el nombre del encargado: ")
        equipos[id]=[nombre,"",""]
        print(f"\nBien, equipo registrado señor/a {nombre}, Ahora ingresa que dispositivos tiene en su computador y si cuenta con alguna novedad")
        dispo1=input("Cuenta con cargador s/n: ").lower
        dispo2=input("Cuenta con mouse s/n: ").lower
        if dispo1 == "s" and dispo2 == "s":
          dispositivos(id, 1, "cargador y mouse")
        elif dispo1 == "s" and dispo2 == "n":
           dispositivos(id, 1, "cargador")
        elif dispo1 == "n" and dispo2 == "s":
           dispositivos(id, 1, "mouse")
        else:
           dispositivos(id, 1, "Sin dispositivos")
        preg=input(f"El equipo {id} cuenta con alguna novedad s/n: ").lower
        if preg == "s":
          desc=input("Describa su novedad: ").title
          novedad(id, 2, desc)
        elif preg == "n":
          break  
    elif opc=="2":
      while True:
        print("Hola, bienvenido al registro de dispositivos, ingrese el id del equipo")
        id=int(input("Digite el id del equipo: "))
        if id in equipos:
          dispo1=input("Cuenta con cargador s/n: ").lower
          dispo2=input("Cuenta con mouse s/n: ").lower
          if dispo1 == "s" and dispo2 == "s":
            dispositivos(id, 1, "cargador y mouse")
          elif dispo1 == "s" and dispo2 == "n":
             dispositivos(id, 1, "cargador")
          elif dispo1 == "n" and dispo2 == "s":
             dispositivos(id, 1, "mouse")
          else:
             dispositivos(id, 1, "Sin dispositivos")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido").title
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="3":
      while True:
        print("Hola, bienvenido al registro de novedades, ingrese el id del equipo")
        id=int(input("Digite el id del equipo: "))
        if id in equipos:
          desc=input("Describa su novedad: ").title
          novedad(id, 2, desc)
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido").title
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="4":
      while True:
        print("Hola, bienvenido al eliminador de novedades, ingrese el id del equipo")
        id=int(input("Digite el id del equipo: "))
        if id in equipos:
          novedad(id, 2, "")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido").title
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="5":
      while True:
        print("Hola, bienvenido al menu para eliminar un equipo, ingrese el id del equipo")
        id=int(input("Digite el id del equipo: "))
        if id in equipos:
          del equipos[id]
          print("Equipo eliminado con exito")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido").title
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="6":
      while True:
        print("Hola, Bienvenido al menu de consultas, busca un equipo por su id")
        id=int(input("Digite el id del equipo: "))
        if id in equipos:
          print(equipos[id])
          print("Equipo encontrado con exito")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido").title
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="7":
        break
    else:
      print("Elegir una opcion valida")

print("Bienvenido al sistema General del sena")
opcG=int(input("Elige una opcion: \n1.Entrar en el Gestor de equipos \n2.Coming soon \n3.Salir\nDigite aqui: "))
if opcG==1:
    menu()
elif opcG==2:
    print("Coming soon")
elif opcG==3:
    print("Gracias por usar el sistema")
else:
    print("Elegir una opcion valida")