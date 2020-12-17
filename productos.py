import os
from logueo import *
Productos = []

def productos ():
  os.system('clear')
  print(":::: MENU PRODUCTOS ::::")
  print("[1.] INGRESAR NUEVO PRODUCTO")
  print("[2.] LISTAR PRODUCTOS")
  print("[3.] BUSCAR PRODUCTOS")
  print("[4.] MODIFICAR PRODUCTO")
  print("[5.] ELIMINAR PRODUCTO")
  print("[6.] VOLVER AL MENU")
  
  op = input(".:: Digite una opción: ")

  if op == '1' :
    ingresar_producto()
  elif op == '2' :
    listar_producto()
  elif op == '3' :
    buscar_producto()
  elif op == '4' :
    modificar_producto()
  elif op == '5' :
    eliminar_producto()
    
  elif op == '6':
    producto()
  else :
    print("::: Vuelve pronto :::")
    
def ingresar_producto():
  os.system('clear')
  print("::: INGRESO NUEVO PRODUCTO ::: ")
  nomproducto = (input(" DIGITE PRODUCTO A ALMACENAR: "))
  Productos.append(nomproducto)
  key = input(" El producto ha sido almacenado . Presione cualquier tecla para volver al menú")
  Productos()

def listar_producto():
  os.system('clear')
  print("::: LISTADO DE PRODUCTOS ::: ")
  if len(Productos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(Productos)
    
  key = input("Presione cualquier tecla para volver al menú") 
  Productos()

def buscar_producto():
  os.system('clear')
  buscar = 0
  print("::: BÚSQUEDA DE PRODUCTOS ::: ")
  if len(Productos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PRODUCTO A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(Productos) :#-1
      if buscar == Productos[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: EL PRODUCTO FUE ENCONTRADO EN LA LISTA")
    else :
      print("::: EL PRODUCTO NO FUE ENCONTRADO EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  Productos()

def modificar_producto():
  os.system('clear')
  print("::: MODIFICACIÓN DE PRODUCTO ::: ")
  if len(Productos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PRODUCTO A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(Productos) :#-1
      if buscar == Productos[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE EL PRODUCTO")
      Productos.insert(Productos, modificar)
    else :
      print("::: EL PRODUCTO NO FUE ENCONTRADO EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  productos()

def eliminar_productos():
	os.system('clear')
	print("ELIMINAR")
	elim = ("DIGITE")
	Productos.remove(elim)
	Productos()