# diseño original con herencia

class Matricula:
    def costo(self):
        return 60.00

class Extemporanea(Matricula):
    def costo(self):
        return super().costo() + 15.00

class IndiceDesaprobatorio(Matricula):
    def costo(self):
        return super().costo() + 15.00

class Beca(Matricula): 
    def costo(self):
        return super().costo() / 2

class CombinadaA(Beca, IndiceDesaprobatorio, Extemporanea):
    pass

class CombinadaB(IndiceDesaprobatorio, Extemporanea, Beca):
    pass


a = CombinadaA()
b = CombinadaB()

print("MRO A:", [c.__name__ for c in CombinadaA.__mro__])
print("MRO B:", [c.__name__ for c in CombinadaB.__mro__])


print("Costo A:", a.costo())
print("Costo B:", b.costo())
print("Diferencia:", abs(a.costo() - b.costo()))


try:
    class Mala(Matricula, Beca):
        pass
except TypeError as e:
    print("Error:", e)


# rediseño con composición

def extemporanea(monto):
    return monto + 15

def desaprobatorio(monto):
    return monto + 15

def beca(monto):
    return monto / 2


class Estudiante:
    def __init__(self, nombre, reglas):
        self.nombre = nombre
        self.reglas = reglas  
      
    def costo(self):
        monto = 60
        for regla in self.reglas:
            monto = regla(monto)
        return monto


luis = Estudiante("Luis Huamaní Cárdenas",
                  [extemporanea, desaprobatorio, beca])   
rosa = Estudiante("Rosa Ccahuana Prado",
                  [beca, extemporanea, desaprobatorio])   

for e in (luis, rosa):
    orden = [r.__name__ for r in e.reglas]
    print(e.nombre, orden, "->", e.costo())

politica_oficial = [extemporanea, desaprobatorio, beca]
e1 = Estudiante("Estudiante 1", politica_oficial)
e2 = Estudiante("Estudiante 2", politica_oficial)
print("Política oficial:", e1.costo(), e2.costo())
