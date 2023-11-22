# Importar fecha para el registro y creacion de variable de la fecha en que se realiza la operacion
from datetime import datetime
fecha= datetime.now()
# Creacion de lista GLOBAL para almacenar cada instancia
listaRegistro = []

#Clase equipo con metodo constructor para iniciar los atributos clave, dispositivos, novedad y ambiente
class Equipos:
   def __init__(self, clave, dispositivos, novedad, ambiente):
       self.clave = clave
       self.dispositivos = dispositivos
       self.novedad = novedad
       self.ambiente = ambiente
#subclase persona que ehreda atributos del metodo constructor, y s añaden 2 propios
class Persona(Equipos):
    def __init__(self, clave, name, apellido, dispositivos, novedad, ambiente):
       super().__init__(clave, dispositivos, novedad, ambiente)
       self.name = name
       self.apellido = apellido
#metodos de la subclase persona, este es para hacer funciones entorno a la clase y no a la instancia
#El @classmethod indica que el siguiente metodo sera para una clase, y en la clase siguiente se le pone de atributo "cls", aunque puede ir otra cosa, es lo que identificara al metodo al ser llamada, algo asi como cuando hacemos un for y predeterminadamente dejamos una variable "I"

    @classmethod
    #Metodo para obtener los datos de registro de un equipos desde 0
    def obtenerDatosPersona(cls):
        while True:
            clave = input("Ingrese el id del equipo o 0 para finalizar: ")
            if clave == "0":
                break
            name = input("Ingrese el nombre del encargado: ")
            apellido = input("Ingrese el apellido del encargado: ")
            #Se llama el metodo clase de registro de dispositivos
            dispositivos = cls.registrarDispositivos()
            novedad = input("Ingrese la novedad o 0 para seguir: ")
            if novedad == "0":
                novedad = "Ninguna"
            novedad = str(fecha) + " " +novedad
            ambiente = input("Ingrese el ambiente: ")
            if clave != "0":
                return cls(clave, name, apellido, dispositivos, novedad, ambiente)
    #Metodo para registrar los dispositivos, estos se agregan en el metodo anterior
    @classmethod
    def registrarDispositivos(cls):
        while True:
            dispoPreg = input("Cuenta con mouse? (s/n): ").lower()
            dispoPreg2 = input("Cuenta con cargador? (s/n): ").lower()
            if dispoPreg == "s" and dispoPreg2 == "s":
                return "cargador y mouse"
            elif dispoPreg == "s" and dispoPreg2 == "n":
                return "Mouse"
            elif dispoPreg == "n" and dispoPreg2 == "s":
                return "cargador"
            else:
                return "Sin dispositivos"
   #Metodo para registrar nuevos o actualizar los dispositivos de un equipo registrado
    @classmethod
    def actualizarDispositivos(cls):
        claveEquipo = input("Ingrese el id del equipo al que desea agregar o actualizar dispositivos: ")
        for persona in listaRegistro:
            if persona.clave == claveEquipo:
                #Se actualiza llama el metodo de registro de equipos para luego almacenarlo en el atributo dispositivo del id encontrado
                nuevosDispositivos = cls.registrarDispositivos()
                persona.dispositivos = nuevosDispositivos
                print("Dispositivos actualizados correctamente.")
                return
        print("Equipo no encontrado.")
    #Metodo de actualizacion de novedades, al igual que el anterior este busca el id del equipo en la lista, y por ultimo hace una pregunta donde se almacenara la novedad, esta de concatena con la fecha actual para el reporte
    @classmethod
    def actualizarNovedad(cls):
       claveEquipo = input("Ingrese el id del equipo al que desea agregar o actualizar la novedad: ")
       for persona in listaRegistro:
           if persona.clave == claveEquipo:
               nuevaNovedad = input("Ingrese la nueva novedad: ")
               persona.novedad = str(fecha) + " "+nuevaNovedad
               print("Novedad actualizada correctamente.")
               return
       print("Equipo no encontrado.")
    #En est se busca el equipo para hacer la eliminacion de la lista, con el remove, donde remueve a la instancia de la clase persona con el id (atributo) encontrado
    @classmethod
    def eliminarEquipo(cls):
         claveEquipo = input("Ingrese el id del equipo que desea eliminar: ")
         for persona in listaRegistro:
             if persona.clave == claveEquipo:
                 listaRegistro.remove(persona)
                 print("Equipo eliminado correctamente.")
                 return
         print("Equipo no encontrado.")
    #Metodo que a partir del id encontrado, agrega el ambiente o actualizacion a un equipo existente, funciona igual que los otros metodos,donde el valor sera incrustado en el atributo de esa instancia
    @classmethod
    def agregarAmbiente(cls):
         claveEquipo = input("Ingrese el id del equipo al que desea agregar el ambiente: ")
         for persona in listaRegistro:
             if persona.clave == claveEquipo:
                 nuevoAmbiente = input("Ingrese el nuevo numero de ambiente: ")
                 persona.ambiente = nuevoAmbiente
                 print("Ambiente actualizado correctamente.")
                 return
         print("Equipo no encontrado.")
    #Por ultimo este metodo trae todos los valores de la instancia persona encontrada en el registro :)
    @classmethod
    def consultarEquipo(cls):
         claveEquipo = input("Ingrese el id del equipo que desea consultar: ")
         for persona in listaRegistro:
             if persona.clave == claveEquipo:
                 print(f"\nDatos del equipo {claveEquipo}:")
                 print(f"Nombre del encargado: {persona.name} {persona.apellido}")
                 print(f"Dispositivos: {persona.dispositivos}")
                 print(f"Novedad: {persona.novedad}")
                 print(f"Ambiente: {persona.ambiente}")
                 return
         print("Equipo no encontrado.")

#Esta funcion sera para llamarse en el programa principal en el caso de que hayan mas sub programas o menus, pero directamente puede ser esta el programa principal
def menu():
   #En este bucle se muestran las opciones que hay para realizar
   while True:
       print("\nBienvenido al menu principal \n1.Registrar un nuevo computador \n2.Registrar dispositivos o actualizar informacion\n3.Agregar o actualizar una novedad \n4.Eliminar un equipo \n5.Agregar el ambiente al que pertenece un equipo \n6.Consultar un equipo \n7.Salir" )

       #Cada opcion es igual a las demas, son un texto print acompañadas de un metodo de la clase persona, y como cada metodo tiene su "menu" se haran las operaciones en estos, el unico en cambiar es la opcion 1, donde al realizar el registro, el metodo de clase retorna la instancia, y ese valor retornado se usa para agregarlo a la lista :)

       opc = input("\nDigite una opcion para continuar: ")
       if opc == "1":
            print("\nHola, bienvenido al registro de computadores")
            personaRegistro = Persona.obtenerDatosPersona()
            listaRegistro.append(personaRegistro)
             
       elif opc == "2":
           print("\nHola, bienvenido al actualizador de dispositivos")
           Persona.actualizarDispositivos()
         
       elif opc == "3":
           print("\nHola, bienvenido al actualizador de novedades")
           Persona.actualizarNovedad()
         
       elif opc == "4":
           print("\nHola, bienvenido al eliminador de equipos")
           Persona.eliminarEquipo()
         
       elif opc == "5":
           print("\nHola, bienvenido al actulizador de ambientes")
           Persona.agregarAmbiente()
         
       elif opc == "6":
           print("\nHola, bienvenido a lugar de registro, consulta tu equipo ")
           Persona.consultarEquipo()
         
       elif opc == "7":
           print("Saliendo del programa. ¡Hasta luego!")
           break
       else:
           print("Opción no válida. Por favor, seleccione una opción válida.")
#Se llama la funcion al programa principal e iniciar la ejecucion de este
menu()
