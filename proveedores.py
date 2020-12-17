import os
from logueo import *
Proveedores = []

def proveedores ():
  os.system('clear')
  print(":::: MENU PROVEEDORES ::::")
  print("[1.] INGRESAR NUEVO PROVEEDOR")
  print("[2.] LISTAR PROVEEDORES")
  print("[3.] BUECAR PROVEEDOR")
  print("[4.] MODIFICAR PROVEEDOR")
  print("[5.] ELIMINAR PROVEEDOR")
  print("[6.] VOLVER AL MENU")
  
  op = input(".:: DIGITE UNA OPCION: ")

  if op == '1' :
    ingresar_proveedor()
  elif op == '2' :
    listar_proveedor()
  elif op == '3' :
    buscar_proveedor()
  elif op == '4' :
    modificar_proveedor()
  elif op == '5' :
    eliminar_proveedor()
    
  elif op == '6':
    proveedores()
  else :
    print("::: VUELVE PRONTO :::")
    
def ingresar_proveedor():
  os.system('clear')
  print("::: INGRESO NUEVO PROVEEDOR ::: ")
  nomproveedor = (input(" DIGITE PROVEEDOR A ALMACENAR: "))
  Proveedores.append(nomproveedor) 
  key = input("EL PROVEEDOR HA SIDO ALMACENADO. Presione cualquier tecla para volver al menú")
  proveedores()

def listar_proveedor():
  os.system('clear')
  print("::: LISTADO DE PROVEEDOR ::: ")
  if len(Proveedores) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(Proveedores)
    
  key = input("Presione cualquier tecla para volver al menú") 
  proveedores()

def buscar_proveedor():
  os.system('clear')
  buscar = 0
  print("::: BÚSQUEDA DE PROVEEDORES ::: ")
  #Here we must to look for a number
  
  if len(Proveedores) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PROVEEDOR A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(Proveedores) :#-1
      if buscar == Proveedores[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: EL PROVEEDOR FUE ENCONTRADO EN LA LISTA")
    else :
      print("::: EL PROVEEDOR NO FUE ENCONTRADO EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  proveedores()

def modificar_proveedor():
  os.system('clear')
  print("::: MODIFICACIÓN DE PROVEEDOR ::: ")
  if len(Proveedores) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PROVEEDOR A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(Proveedores) :#-1
      if buscar == Proveedores[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE LA CATEGORIA")
      Proveedores.insert(Proveedores, modificar)
    else :
      print("::: EL PROVEEDOR NO FUE ENCONTRADA EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  proveedores()

def eliminar_proveedor():
	os.system('clear')
	print("ELIMINAR PROVEEDOR")
	elim = input("DIGITE PROVEEDOR A ELIMINAR")
	Proveedores.remove(elim)
	key = input("tecla")
	proveedores()
