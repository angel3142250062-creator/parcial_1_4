"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares (marca,color,modelo,velocidad,potencia,asientos) y con los operaciones de acelerar y frenar. Que los atributos y metodos sean publicos.
#Muestre el color de los coches
#Que los operaciones disminuyan o aumenten la velocidad segun sea el caso y hay jugar con los metodos e imprimes la velocidad final

print("\033c")
class Coches:
    marca=""
    color="blanco"
    modelo=""
    velocidad=100
    potencia=0
    asientos=0

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velocidad es: {self.velocidad}")

    def frenar(self):
        self.velocidad-=1
#Multiples objetos o instancias
coche1=Coches()
coche2=Coches()

print(f"El color del coche 1 es: {coche1.color}")
print(f"El color del coche 2 es: {coche2.color}")

for i in range(1,11):
    coche1.acelerar()

##################################################################################################################

class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

    def acelerar(self):
        print(f"El coche {self.__marca} está acelerando.")

    def frenar(self):
        print(f"El coche {self.__marca} está frenando.")
coche1 = Coches(
    marca='VW',
    color='Blanco',
    modelo='2022',
    velocidad=220,
    caballaje=150,
    plazas=5
)
coche2 = Coches(
    marca='Nissan',
    color='Azul',
    modelo='2020',
    velocidad=180,
    caballaje=150,
    plazas=6
)
print(f"Coche 1: Marca {coche1.__marca}, Color {coche1.__color}, Modelo {coche1.__modelo}, Velocidad máxima {coche1.__velocidad} km/h")
print(f"Coche 2: Marca {coche2.__marca}, Color {coche2.__color}, Modelo {coche2.__modelo}, Velocidad máxima {coche2.__velocidad} km/h")

coche1.acelerar()
coche2.frenar()































    