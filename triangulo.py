class Triangulo:
  def __init__(self, lado1, lado2, lado3):
    self.lado1=lado1
    self.lado2=lado2
    self.lado3=lado3

  def get_lado_mayor(self):
    return max(self.lado1, self.lado2, self.lado3)

  def get_tipo(self):
    if(self.lado1==self.lado2==self.lado3):
      print("equilatero")

