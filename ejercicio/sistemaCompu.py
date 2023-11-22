from datetime import date
from datetime import datetime

fecha= datetime.now() 

equipos={1:['Maria F','','',''],2:['Miguel A','','',''],3:['Kevin L','','',''],4:['Santiago T','','',''],5:['Mathew G','','',''],6:['Maria P','','',''],7:['Kevin E','','',''],8:['Adriana L','','',''],9:['Sebastian P','','',''],10:['Sandra M','','',''],11:['Cristian A','','',''],12:['Matias G','','',''],13:['Kevin H','','',''],14:['Juan D','','',''],15:['Sebastian T','','',''],16:['Laura E','','','']}

def ambiente(clave, indice, valor):
  if clave in equipos:
      equipos[clave][indice] = "Ambiente: "+ valor

def dispositivos(clave, indice, valor):
  if clave in equipos:
      equipos[clave][indice] = "Dispositivos: "+ valor
def novedad(clave, indice, valor):
 if clave in equipos:
     equipos[clave][indice] = "Novedad: " + valor
     print("\nNovedad actualizada :) \n")
def recuperarId(valor):
  for clave, lista in equipos.items():
      if lista[0] == valor:
          return print(f"\nSu id es {clave}")
  return None
def menu():
  while True:
    print("Bienvenido al menu principal \n1.Registrar un nuevo computador \n2.Registrar dispositivos o actualizar a un equipo existente \n3.Agregar o actualizar una novedad \n4.Eliminar una novedad \n5.Eliminar un equipo \n6.Agregar el ambiente al que pertenece un equipo \n7.Consultar un equipo \n8. Salir" )
    opc=input("\nDigite una opcion para continuar: ")
    if opc=="1":
      while True:
        print("\nHola, bienvenido al registro de computadores, ingrese el id del equipo y nombre del encargado")
        id=int(input("Digite el id del equipo o (0 para finalizar): "))
        if id == 0:
           break
        nombre=input("Digite el nombre del encargado: ")
        if id in equipos:
           print ("Ya existe el id del equipo")
        elif id not in equipos:
          equipos[id]=[nombre,"",""]
          print(f"\nBien, equipo registrado señor/a {nombre}, Ahora ingresa a que ambiente pertenece, que dispositivos tiene en su computador y si cuenta con alguna novedad")

          ambient = int(input("Digite el numero del ambiente al que pertenece: "))
          ambiente(id, 3, ambient)
          print("Ambiente agregado")
          dispo1=input("Cuenta con cargador s/n: ").lower()
          dispo2=input("Cuenta con mouse s/n: ").lower()

          if dispo1 == "s" and dispo2 == "s":
            dispositivos(id, 1, "cargador y mouse")
          elif dispo1 == "s" and dispo2 == "n":
            dispositivos(id, 1, "cargador")
          elif dispo1 == "n" and dispo2 == "s":
            dispositivos(id, 1, "mouse")
          else:
            dispositivos(id, 1, "Sin dispositivos")
          while dispo1 and dispo2 != None:
            preg=input(f"El equipo {id} cuenta con alguna novedad s/n: ").lower()
            if preg == "s":
                desc=input("Describa su novedad: ").title()
                novedad(id, 2, str(fecha) +" "+desc)
                break
            elif preg == "n":
                break  
          
    elif opc=="2":
      while True:
        print("\nHola, bienvenido al registro de dispositivos, ingrese el id del equipo")
        id=int(input("Digite el id del equipo (0 para finalizar): "))
        if id == 0:
           break
        if id in equipos:
          dispo1=input("Cuenta con cargador s/n: ").lower()
          dispo2=input("Cuenta con mouse s/n: ").lower()
          if dispo1 == "s" and dispo2 == "s":
            dispositivos(id, 1, "cargador y mouse")
          elif dispo1 == "s" and dispo2 == "n":
             dispositivos(id, 1, "cargador")
          elif dispo1 == "n" and dispo2 == "s":
             dispositivos(id, 1, "mouse")
          else:
             dispositivos(id, 1, "Sin dispositivos")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido \n").title()
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="3":
      while True:
        print("\nHola, bienvenido al registro de novedades, ingrese el id del equipo")
        id=int(input("Digite el id del equipo (0 para finalizar): "))
        if id == 0:
           break
        if id in equipos:
          desc=input("Describa su novedad: ").title()
          novedad(id, 2, str(fecha) +" "+desc)
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido \n").title()
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="4":
      while True:
        print("\nHola, bienvenido al eliminador de novedades, ingrese el id del equipo")
        id=int(input("Digite el id del equipo (0 para finalizar): "))
        if id == 0:
           break
        if id in equipos:
          novedad(id, 2, str(fecha) + " Novedad Eliminada")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido \n").title()
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="5":
      while True:
        print("\nHola, bienvenido al menu para eliminar un equipo, ingrese el id del equipo")
        id=int(input("Digite el id del equipo (0 para finalizar): "))
        if id == 0:
           break
        if id in equipos:
          del equipos[id]
          print("Equipo eliminado con exito")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido \n").title()
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc =="6":
       print("\nHola, Bienvenido al agregador de ambientes, busca un equipo por su id")
       id=int(input("Digite el id del equipo (0 para finalizar): "))
       if id == 0:
           break
       if id in equipos:
          n=input("Escriba el numero del ambiente: ")
          ambiente(id, 3, n)
    elif opc=="7":
      while True:
        print("\nHola, Bienvenido al menu de consultas, busca un equipo por su id")
        id=int(input("Digite el id del equipo (0 para finalizar): "))
        if id == 0:
           break
        if id in equipos:
          print(f"Equipo {id}\nEncargado:")
          for i in equipos[id]:
            print (i)
          print("Equipo encontrado con exito")
        else:
          preg=input(f"El equipo {id} no existe, ingrese el nombre del tutor para restablecer su id o salir para finalizar: \nRecuerde escribir el nombre seguido de un espacio y la inicial del segundo nombre o apellido \n").title()
          recuperarId(preg)
          if preg == "Salir":
             break
    elif opc=="8":
        break
    else:
      print("Elegir una opcion valida")

while True:
  print("Bienvenido al sistema General del sena")
  opcG=int(input("Elige una opcion: \n1.Entrar en el Gestor de equipos \n2.Coming soon \n3.Salir\nDigite aqui: "))
  if opcG==1:
      menu()
  elif opcG==2:
      print("Coming soon")
  elif opcG==3:
      print("Gracias por usar el sistema")
      break
  else:
      print("Elegir una opcion valida")