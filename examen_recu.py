class alumnos:
    _nombre=""
    _edad=0
    _calificacion=0

    def mostrarDatos(self,nombre,edad,calificacion):
        print("Nombre:",nombre)
        print("Edad:",edad)
        print("Calificacion:",calificacion)

    def estaAprobado(self,calificacion):
        if calificacion >= 7:
            return "Aprobado"
        else:
            return "Reprobado"

alumno1=alumnos()
alumno1._nombre="Angel Rivera"
alumno1._edad=19
alumno1._calificacion=8

alumno2=alumnos()
alumno2._nombre="Velarde ceniceros"
alumno2._edad=19
alumno2._calificacion=7