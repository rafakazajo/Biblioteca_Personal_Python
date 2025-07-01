import datetime #importa datos como fecha actual
import json #Importa para poder caragar y guardar datos en archivos
import os #Lo uso para comprobar si el archivo

class Libro():
    def __init__(self, nombre, autor, fecha_añadido = None, fecha_terminado = None, completado = False):
        self.nombre = nombre
        self.autor = autor
        if fecha_añadido:
            self.fecha_añadido = fecha_añadido
        else:
            self.fecha_añadido = datetime.date.today().isoformat()
        self.fecha_terminado = fecha_terminado
        self.completado = completado

    def marcar_completado(self):
        if not self.completado:
            self.completado = True
            self.fecha_terminado = datetime.date.today().isoformat() #Es la fecha actual pasada a formato ISO
            print("El libro se ha marcado como completado")
            print("")
        else:
            print("El libro ya estaba marcado como completado")
            print("")

    def __str__(self):
        if self.completado:
            estado = "Completado"
        else:
            estado = "Pendiente"
            fecha_finalizado = ""
        if self.completado and self.fecha_terminado:
            fecha_finalizado = (f", Terminado: {self.fecha_terminado}")
        return (f"Titulo: {self.nombre}, Autor: {self.autor}, Estado: {estado}{fecha_finalizado}, Añadido el: {self.fecha_añadido}")

class Biblioteca():
    def __init__(self, nombre_archivo = "Biblioteca personal.json"):
        self.nombre_archivo = nombre_archivo
        self.lista = []
        self.cargar_libros()
    
    def guardar_libros(self):
        libros_guardados = []
        for libro in self.lista:
            libros_guardados.append({"Nombre": libro.nombre, "Autor": libro.autor, "Fecha añadido": libro.fecha_añadido, "Fecha terminado": libro.fecha_terminado, "Completado": libro.completado})
        try:
            with open(self.nombre_archivo, "w", encoding = "utf-8") as file: #Abrimos el archivo con para escirtura y con un formato que acepta la ñ
                json.dump(libros_guardados, file, indent = 4, ensure_ascii = False) #Hacemos que archivo sea mas legible
        except IOError as error:
            print("Ha habido un error al guardar el libro")
            print("")

    def cargar_libros(self):
        if os.path.exists(self.nombre_archivo) and os.path.getsize(self.nombre_archivo) > 0: #Comprobamos que el archivo exista y no haya nada
            try:
                 with open(self.nombre_archivo, "r", encoding = "utf-8") as file:
                     datos = json.load(file)
                     self.lista = []
                     for item in datos:
                         libro = Libro(item["Nombre"], item["Autor"], item["Fecha añadido"], item["Fecha terminado"], item["Completado"])
                         self.lista.append(libro)
            except json.JSONDecodeError as error:
                print("Ha habido un error al leer el archivo")
            except IOError as error:
                print("Ha habido un error al cargar los libros")
                self.lista = []
        else:
            self.lista = []
    
    def añadir_libro(self,):
        nombre = input("Añade tu libro aqui\n\n---> ")
        print("")
        if not nombre:
            print("Lo siento el nombre del libro no puede esta vacio")
            print("")
            return

        autor = input("Escribe el nombre del autor aqui\n\n---> ")
        print("")
        if not autor:
            print("Lo siento el autor no puede estar vacio")
            print("")
            return
        
        libro_nuevo = Libro(nombre, autor)
        self.lista.append(libro_nuevo)
        self.guardar_libros()
        print("Se ha añadido el libro")
        print("")

    def ver_biblioteca(self):
        recuento = 0
        if not self.lista:
            print("Lo siento no hay libros en tu biblioteca")
            print("")
            return
        print("Esta es tu biblioteca")
        print("")
        for i, libro in enumerate(self.lista):
            print(f"{i + 1}. {libro}")
        print("")


    def eliminar_libro(self):
        if not self.lista:
            print("Lo siento no hay libros en tu biblioteca")
            print("")
            return

        print("¿Que libro quieres eliminar?\n(Escriba el numero correspondiente)\n")
        self.ver_biblioteca()
        print("")
        eliminar = int(input("---> "))
        print("")
        try:
            self.lista.pop(eliminar - 1)
            self.guardar_libros()
            print("Se ha eliminado el libro")
            print("")
        except ValueError:
            print("Porfavor introduzca un numero valido")
            print("")
        except Exception as error:
            print("Lo siento ha ocurrido un error inesperado")
            print("")
    def menu(self):
        while True:
            opcion = input("¿Que quieres hacer?\n(Escriba el numero correspondiente)\n\n1. Añadir libro\n2. Eliminar libro\n3. Marcar como completado\n4. Ver biblioteca\n5. Salir\n\n---> ")
            print("")
            if opcion.isnumeric():
                if opcion == "1":
                    self.añadir_libro()
                elif opcion == "2":
                    self.eliminar_libro()
                elif opcion == "3":
                    if not self.lista:
                        print("No hay libros en la biblioteca")
                        print("")
                        continue
                    try:
                        print("Dime que libro quieres marcar como completado\n(Escribe el numero correspondiente)\n")
                        self.ver_biblioteca()
                        print("")
                        num = int(input("---> "))
                        print("")
                        if 1 <= num <= len(self.lista):
                            self.lista[num - 1].marcar_completado()
                            self.guardar_libros()
                        else:
                            print("Ese numero de libro no existe introduzca uno valido")
                            print("")
                    except ValueError:
                        print("Por favor introduzca un numero")
                        print("")
                    except Exception as error:
                        print("Lo siento se ha porducido un error inesperado")
                        print("")
                elif opcion == "4":
                    self.ver_biblioteca()
                elif opcion == "5":
                    print("Gracias, hasta luego")
                    print("")
                    return
                else:
                    print("Porfavor introduzca un numero valido")
                    print("")
            else:
                print("Porfavor introduzaca un numero")
                print("")

if __name__ == "__main__": #Sirve para que puedas ejecutarla directamente o importarla en otro programa
    mi_biblioteca = Biblioteca()
    mi_biblioteca.menu()
