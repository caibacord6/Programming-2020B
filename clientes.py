import os
from logueo import *
Clientes = []

def clientes ():
  os.system('clear')
  print(":::: MENU CLIENTES ::::")
  print("[1.] INGRESAR NUEVO CLIENTE")
  print("[2.] LISTAR CLIENTES")
  print("[3.] BUSCAR CLIENTES")
  print("[4.] MODIFICAR CLIENTE")
  print("[5.] ELIMINAR CLIENTE")
  print("[6.] VOLVER AL MENU")
  
  op = input(".:: Digite una opción: ")

  if op == '1' :
    ingresar_cliente()
  elif op == '2' :
    listar_cliente()
  elif op == '3' :
    buscar_cliente()
  elif op == '4' :
    modificar_cliente()
  elif op == '5' :
    eliminar_cliente()
    
  elif op == '6':
    cliente()
  else :
    print("::: Vuelve pronto :::")
    
def ingresar_cliente():
  os.system('clear')
  print("::: INGRESO NUEVO CLIENTE ::: ")
  nomcliente = (input(" DIGITE CLIENTE A ALMACENAR: "))
  Clientes.append(nomcliente)
  key = input(" El producto ha sido almacenado . Presione cualquier tecla para volver al menú")
  clientes()

def listar_cliente():
  os.system('clear')
  print("::: LISTADO DE CLIENTES ::: ")
  if len(Clientes) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(Clientes)
    
  key = input("Presione cualquier tecla para volver al menú") 
  clientes()

def buscar_cliente():
  os.system('clear')
  buscar = 0
  print("::: BÚSQUEDA DE CLIENTES ::: ")
  if len(Clientes) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CLIENTE A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(Clientes) :#-1
      if buscar == Clientes[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: EL CLIENTE FUE ENCONTRADO EN LA LISTA")
    else :
      print("::: EL CLIENTE NO FUE ENCONTRADO EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  clientes()

def modificar_cliente():
  os.system('clear')
  print("::: MODIFICACIÓN DE CLIENTE ::: ")
  if len(Clientes) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CLIENTE A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(Clientes) :#-1
      if buscar == Clientes[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE EL CLIENTE")
      Clientes.insert(Clientes, modificar)
    else :
      print("::: EL CLIENTE NO FUE ENCONTRADO EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  clientes()

def eliminar_cliente():
	os.system('clear')
	print("::: CLIENTE A ELIMINAR::: ")
	elim = ("DIGITE CLIENTE A ELIMINAR: ")
	Clientes.remove(elim)
	clientes()