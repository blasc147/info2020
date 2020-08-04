from pack1.clase1 import Contacto

class Agenda:

  def __init__(self):
    self.contactos=[]

  def anadir(self):
    nom=input("Ingresar nombre: ")
    tel=input("Ingresar telefono: ")
    mail=input("Ingresar mail: ")
    contacto=Contacto(nom,tel,mail)
    self.contactos.append(contacto)

  def __str__(self):
    str=""
    for i in self.contactos:
      str+=f"{i.nombre}\t{i.telefono}\n"

  def buscar(self, param)
    pass
    for i in self.contactos:
      if i.nombre==param:
        return contacto
    

  def editar(self, param,nombre)
    contacto = self.buscar(param)
    contacto.nombre=nombre
