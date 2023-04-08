class Alumno:
    def inicializador(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Tu nota:",self.nota)
        self.aprobado()

    def aprobado(self):
        if self.nota >= 5:
            return print("Aprobaste!")
        else:
            return print("No has aprobado.")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializador("Jorge",4)
alumno2.inicializador("Maria",8)

alumno1.imprimir()
alumno2.imprimir()