import datetime

x = datetime.datetime.now()

class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"

    def calcular_precio(self):
      return self.pvp

class Lacteos(Producto):
    def __init__(self, referencia, nombre, pvp, descripcion, mes_ven, a_ven):
      super().__init__(referencia,nombre,pvp,descripcion)
      self.mes_ven=mes_ven
      self.a_ven=a_ven

    def __str__(self):
      return super().__str__()+f"Fecha Vencimiento\t {self.mes_ven}/{self.a_ven}"

    def calcular_precio(self):
      if (self.a_ven<=x.year or self.mes_ven<x.month):
        self.pvp=self.pvp*0.5


alimento=Lacteos(1, "Yogurt", 100, "con cereales", 5, 2020)
alimento2=Producto(1, "Arroz", 100, "integral")

lista_productos=[alimento,alimento2]

for a in lista_productos:
  a.calcular_precio()
  print(a,"\n")